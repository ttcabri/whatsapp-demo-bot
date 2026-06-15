import re
from services.whatsapp import send_message
from services.sheets import save_lead
from services.notifications import send_telegram_notification
from data.business_info import SERVICE_OPTIONS

# In-memory state machine: {phone_number: {"step": str, "data": dict}}
_sessions: dict[str, dict] = {}

STEPS = ["name", "service", "time", "phone"]


def get_session(user_id: str) -> dict:
    return _sessions.get(user_id, {})


def clear_session(user_id: str) -> None:
    _sessions.pop(user_id, None)


def is_in_booking(user_id: str) -> bool:
    return user_id in _sessions


def start_booking(to: str) -> None:
    """Initiate the booking flow."""
    _sessions[to] = {"step": "name", "data": {}}
    send_message(
        to,
        "Great! Let's book your appointment 📅\n\n"
        "Step 1/4 — What's your name?\n\n"
        "_Type *menu* anytime to go back to the main menu._",
    )


def _is_valid_name(name: str) -> bool:
    """Name must be at least 2 chars and contain only letters/spaces."""
    name = name.strip()
    return len(name) >= 2 and bool(re.match(r"^[A-Za-zÀ-ÿ\s\-']+$", name))


def _is_valid_phone(text: str) -> bool:
    """Must contain at least 7 digits."""
    digits = ''.join(filter(str.isdigit, text))
    return len(digits) >= 7


def handle_booking_step(to: str, text: str) -> None:
    """Process the current booking step."""
    session = _sessions.get(to)
    if not session:
        return

    step = session["step"]
    data = session["data"]

    if step == "name":
        if not _is_valid_name(text):
            send_message(
                to,
                "Please enter your real name (letters only, at least 2 characters) 😊"
            )
            return
        data["name"] = text.strip().title()
        session["step"] = "service"
        options = "\n".join(f"{i+1}. {s}" for i, s in enumerate(SERVICE_OPTIONS))
        send_message(
            to,
            f"Nice to meet you, {data['name']}! 😊\n\n"
            f"Step 2/4 — Which service are you interested in?\n\n"
            f"{options}\n\n"
            f"Reply with a number or type the service name.",
        )

    elif step == "service":
        choice = text.strip()
        if choice.isdigit():
            idx = int(choice) - 1
            service = SERVICE_OPTIONS[idx] if 0 <= idx < len(SERVICE_OPTIONS) else choice
        else:
            service = choice.title()
        data["service"] = service
        session["step"] = "time"
        send_message(
            to,
            f"Step 3/4 — When would you prefer to come in?\n\n"
            f"Please tell us the day and time, e.g.:\n"
            f"• Saturday at 2pm\n"
            f"• Tomorrow morning\n"
            f"• Any weekday after 5pm",
        )

    elif step == "time":
        data["preferred_time"] = text.strip()
        session["step"] = "phone"
        send_message(
            to,
            f"Step 4/4 — What's the best phone number or WhatsApp to reach you?\n\n"
            f"Example: +31612345678",
        )

    elif step == "phone":
        if not _is_valid_phone(text):
            send_message(
                to,
                "Please enter a valid phone number (at least 7 digits) 📱\n\n"
                "Example: +31612345678"
            )
            return
        data["phone"] = text.strip()
        name = data["name"]
        service = data["service"]
        preferred_time = data["preferred_time"]
        phone = data["phone"]

        try:
            save_lead(name, service, preferred_time, phone)
        except Exception:
            pass

        try:
            send_telegram_notification(name, service, preferred_time, phone)
        except Exception:
            pass

        clear_session(to)

        send_message(
            to,
            f"✨ Thank you, {name}!\n\n"
            f"Your booking request has been received:\n"
            f"💅 Service: {service}\n"
            f"🕐 Preferred time: {preferred_time}\n"
            f"📱 Contact: {phone}\n\n"
            f"We'll confirm your appointment within 2 hours. "
            f"See you soon at Lumina Beauty Studio! 💆‍♀️\n\n"
            f"_Type *menu* to return to the main menu._",
        )
