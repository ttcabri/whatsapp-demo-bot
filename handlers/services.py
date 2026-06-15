from data.business_info import SERVICES_TEXT, PRICES_TEXT
from services.whatsapp import send_message


def send_services(to: str) -> None:
    """Send the list of services."""
    send_message(to, SERVICES_TEXT)


def send_prices(to: str) -> None:
    """Send the price list."""
    send_message(to, PRICES_TEXT)
