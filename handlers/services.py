from data.business_info import SERVICES_TEXT, PRICES_TEXT
from services.whatsapp import send_message

BACK_TO_MENU = "\n\n_Reply *Book Now* to book an appointment or *menu* to go back._"


def send_services(to: str) -> None:
    send_message(to, SERVICES_TEXT + BACK_TO_MENU)


def send_prices(to: str) -> None:
    send_message(to, PRICES_TEXT + BACK_TO_MENU)
