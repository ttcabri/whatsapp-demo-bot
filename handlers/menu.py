from data.business_info import WELCOME_TEXT
from services.whatsapp import send_message


def send_main_menu(to: str) -> None:
    """Send the main welcome message with menu options."""
    send_message(to, WELCOME_TEXT)
