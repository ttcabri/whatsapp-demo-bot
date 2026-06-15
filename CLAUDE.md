# CLAUDE.md — WhatsApp Lead Capture Bot (Portfolio Demo #2)

## WHO I AM

My name is Andrii. I'm a freelance AI developer building portfolio demos for Upwork.
This is my second portfolio project — a WhatsApp business bot demo.

## PROJECT GOAL

Build a working WhatsApp bot demo for a beauty salon / clinic.
Theme: "Lumina Beauty Studio" (fictional, universal for any service business).

The bot handles:
1. Greeting new clients with a welcome message + quick replies menu
2. Showing services and prices (static info)
3. Running a lead qualification flow (name → service → preferred time → phone)
4. Saving qualified leads to Google Sheets
5. Sending instant Telegram notification to the owner with lead summary
6. Answering free-text questions via Claude API (AI responses)

## WHY THIS DEMO WORKS FOR PORTFOLIO

- WhatsApp is the #1 messaging platform for small businesses globally
- Beauty/clinic niche is universally understood by clients
- Shows: AI responses + data capture + CRM integration
- Different from Bot #1 (Telegram + coach) — shows range

## TECH STACK

- Python 3.11+
- whatsapp-business-api (via Meta Cloud API / Twilio sandbox)
- anthropic (Claude API for AI responses)
- gspread + google-auth (Google Sheets)
- fastapi + uvicorn (webhook server for WhatsApp)
- python-dotenv
- ngrok (local dev tunnel) OR Railway.app (production)

## IMPORTANT NOTE ON WHATSAPP API

Two options (choose based on what's available):

### Option A — Twilio Sandbox (RECOMMENDED for demo)
- Free trial, fast setup
- Use Twilio WhatsApp Sandbox
- No Meta Business verification needed
- Perfect for portfolio demo screenshots

### Option B — Meta Cloud API (production-ready)
- Requires Meta Business verification
- More complex setup
- Use if Twilio not available

## PROJECT STRUCTURE

```
whatsapp-bot-demo/
├── CLAUDE.md               # this file
├── .env                    # tokens (never commit!)
├── .env.example            # template
├── .gitignore
├── requirements.txt
├── main.py                 # FastAPI webhook server
├── config.py               # settings from .env
├── handlers/
│   ├── __init__.py
│   ├── menu.py             # main menu logic
│   ├── services.py         # services & prices info
│   ├── booking.py          # lead capture flow (state machine)
│   └── ai_chat.py          # Claude API responses
├── services/
│   ├── __init__.py
│   ├── whatsapp.py         # send messages via API
│   ├── sheets.py           # Google Sheets integration
│   └── notifications.py    # Telegram notification to owner
├── data/
│   └── business_info.py    # salon info, services, prices
└── README.md
```

## ENV VARIABLES

```
# Twilio (Option A)
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886

# OR Meta Cloud API (Option B)
WHATSAPP_TOKEN=
WHATSAPP_PHONE_ID=
WHATSAPP_VERIFY_TOKEN=

# Common
ANTHROPIC_API_KEY=
OWNER_TELEGRAM_BOT_TOKEN=  # can reuse bot from Bot #1
OWNER_CHAT_ID=
GOOGLE_SHEET_ID=
```

## BOT CONVERSATION FLOW

```
[New message received]
  → Welcome: "Hi! I'm Luna, virtual assistant at Lumina Beauty Studio 💆"
  → Menu buttons:
    [Our Services] [Prices] [Book Now] [Ask a Question]

[Our Services]
  → List: Haircut, Color, Facial, Massage, Nails
  → Each with short description

[Prices]
  → Price list with ranges
  → "Book Now" button at end

[Book Now] → Lead capture flow:
  Step 1: "What's your name?"
  Step 2: "Which service are you interested in?"
         [Haircut] [Color] [Facial] [Massage] [Other]
  Step 3: "When would you prefer? (day + time)"
  Step 4: "Your phone number or WhatsApp?"
  → Save to Google Sheets
  → Notify owner via Telegram:
      "🆕 New booking request!
       Name: Sarah
       Service: Facial
       Time: Saturday 2pm
       Contact: +31612345678"
  → "Thank you Sarah! We'll confirm your appointment within 2 hours. ✨"

[Ask a Question]
  → Free text → Claude API responds based on business context
  → Fallback: "Our team will get back to you shortly!"
```

## BUSINESS INFO (for Claude API context)

```python
BUSINESS_CONTEXT = """
You are Luna, a friendly virtual assistant for Lumina Beauty Studio.
Location: Amsterdam, Netherlands
Hours: Mon-Sat 9am-7pm, Sun 10am-5pm
Services: Haircut (from €35), Color (from €65), Facial (from €55),
          Massage (from €60), Nail Care (from €30)
Booking: Via WhatsApp or phone +31 20 123 4567
Policy: 24h cancellation notice required
Tone: Warm, professional, helpful. Always end with an offer to book.
"""
```

## WHAT TO BUILD FIRST (priority order)

1. FastAPI webhook server that receives WhatsApp messages
2. Twilio setup + test "Hello World" response
3. Menu logic with quick reply buttons
4. services.py + prices (static text)
5. Lead capture state machine (booking.py)
6. Google Sheets integration
7. Telegram notification to owner
8. Claude API for free-text questions
9. Deploy to Railway

## PORTFOLIO SCREENSHOTS TO CAPTURE

1. Welcome message with menu buttons
2. Services list
3. Full booking conversation (all 4 steps)
4. Confirmation message to client
5. Telegram notification received by owner
6. Google Sheet with captured leads

## START COMMAND

When you run `claude` in this folder, say:
"Build the WhatsApp bot demo per CLAUDE.md. Start with the FastAPI webhook server and Twilio sandbox setup."
