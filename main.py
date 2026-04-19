import requests
from bs4 import BeautifulSoup
import time
import os

# =========================
# 🔐 RAILWAY VARIABLES
# =========================
TOKEN = os.getenv("TOKEN")      # Telegram Bot Token
CHAT_ID = os.getenv("CHAT_ID")  # Your Chat ID

# =========================
# 🎯 GOETHE LINK (YOU GAVE)
# =========================
URL = "https://www.goethe.de/ins/pk/en/spr/prf/gzb1.cfm"

# =========================
# 📩 SEND MESSAGE FUNCTION
# =========================
def send_telegram(msg):
    try:
        requests.get(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            params={"chat_id": CHAT_ID, "text": msg}
        )
    except:
        print("Telegram error")

# =========================
# 🔍 CHECK WEBSITE
# =========================
def check_seat():
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(URL, headers=headers, timeout=10)

        text = r.text.lower()

        # Simple detection logic
        if "available" in text or "book now" in text or "anmelden" in text:
            send_telegram("🚨 GOETHE ALERT: Possible seat update! Check B1 page NOW!")
            print("ALERT SENT")
        else:
            print("No seat yet...")

    except Exception as e:
        print("Error:", e)

# =========================
# 🚀 MAIN LOOP
# =========================
print("Bot started...")

while True:
    check_seat()
    time.sleep(60)
