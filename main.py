from fastapi import FastAPI, Form, Response
from fastapi.responses import PlainTextResponse

from handlers.menu import send_main_menu
from handlers.services import send_services, send_prices
from handlers.booking import start_booking, handle_booking_step, is_in_booking, clear_session
from handlers.ai_chat import handle_question
from services.whatsapp import send_message

app = FastAPI(title="Lumina Beauty Studio WhatsApp Bot")

MENU_TRIGGERS = {
    "services": ["1", "our services", "services", "service"],
    "prices": ["2", "prices", "price", "price list", "how much"],
    "booking": ["3", "book", "book now", "booking", "appointment"],
    "question": ["4", "ask", "ask a question", "question", "help"],
}

GREETING_TRIGGERS = ["hi", "hello", "hey", "start", "hola", "привет", "aloha"]

# Escape commands — cancel booking and return to menu
ESCAPE_TRIGGERS = ["menu", "cancel", "stop", "back", "quit", "exit", "0"]


@app.get("/webhook")
async def verify():
    return PlainTextResponse("OK")


@app.post("/webhook")
async def receive_message(
    Body: str = Form(default=""),
    From: str = Form(default=""),
):
    text = Body.strip().lower()
    sender = From.strip()

    if not sender:
        return Response(status_code=200)

    # Escape commands — always work, even mid-booking
    if text in ESCAPE_TRIGGERS:
        clear_session(sender)
        send_main_menu(sender)
        return Response(status_code=200)

    # If user is mid-booking flow, continue it
    if is_in_booking(sender):
        handle_booking_step(sender, Body.strip())
        return Response(status_code=200)

    # Greeting → show main menu
    if text in GREETING_TRIGGERS or text == "":
        send_main_menu(sender)
        return Response(status_code=200)

    # Menu routing
    if text in MENU_TRIGGERS["services"]:
        send_services(sender)
    elif text in MENU_TRIGGERS["prices"]:
        send_prices(sender)
    elif text in MENU_TRIGGERS["booking"]:
        start_booking(sender)
    elif text in MENU_TRIGGERS["question"]:
        handle_question(sender, Body.strip())
    else:
        handle_question(sender, Body.strip())

    return Response(status_code=200)
