import httpx
from config import OWNER_TELEGRAM_BOT_TOKEN, OWNER_CHAT_ID


def send_telegram_notification(name: str, service: str, preferred_time: str, phone: str) -> None:
    """Send a lead notification to the owner via Telegram."""
    if not OWNER_TELEGRAM_BOT_TOKEN or not OWNER_CHAT_ID:
        return

    text = (
        f"🆕 *New Booking Request!*\n\n"
        f"👤 Name: {name}\n"
        f"💅 Service: {service}\n"
        f"🕐 Time: {preferred_time}\n"
        f"📱 Contact: {phone}\n\n"
        f"_Please confirm within 2 hours_ ✅"
    )

    url = f"https://api.telegram.org/bot{OWNER_TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": OWNER_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
    }

    with httpx.Client(timeout=10) as client:
        client.post(url, json=payload)
