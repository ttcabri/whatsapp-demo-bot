import anthropic
from data.business_info import BUSINESS_CONTEXT
from services.whatsapp import send_message
from config import ANTHROPIC_API_KEY

_client = None


def _get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    return _client


def handle_question(to: str, question: str) -> None:
    """Answer a free-text question using Claude API."""
    try:
        client = _get_client()
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            system=BUSINESS_CONTEXT,
            messages=[{"role": "user", "content": question}],
        )
        answer = response.content[0].text
    except Exception:
        answer = (
            "Our team will get back to you shortly! 😊\n\n"
            "You can also reach us directly at +31 20 123 4567."
        )

    send_message(to, answer)
