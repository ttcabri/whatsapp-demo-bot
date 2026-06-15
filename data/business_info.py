BUSINESS_CONTEXT = """
You are Luna, a friendly and professional virtual assistant for Lumina Beauty Studio.

Studio details:
- Location: Amsterdam, Netherlands
- Phone: +31 20 123 4567
- Hours: Monday–Saturday 9:00–19:00, Sunday 10:00–17:00

Services and prices:
- Haircut: from €35 (30–60 min)
- Hair Color: from €65 (90–180 min)
- Facial Treatment: from €55 (60 min)
- Relaxing Massage: from €60 (60 min)
- Nail Care (manicure/pedicure): from €30 (45–60 min)

Booking policy:
- Appointments via WhatsApp or by phone
- 24-hour cancellation notice required to avoid a cancellation fee
- Walk-ins welcome subject to availability

Your role:
- Answer questions about services, prices, availability, and studio policies
- Be warm, concise, and helpful
- Always end your response with an invitation to book, e.g., "Would you like to book an appointment?"
- Do not invent prices or services not listed above
- If you don't know the answer, say: "Our team will be happy to help — feel free to call us at +31 20 123 4567."
"""

SERVICES = [
    {"name": "Haircut", "price": "from €35", "duration": "30–60 min"},
    {"name": "Hair Color", "price": "from €65", "duration": "90–180 min"},
    {"name": "Facial Treatment", "price": "from €55", "duration": "60 min"},
    {"name": "Relaxing Massage", "price": "from €60", "duration": "60 min"},
    {"name": "Nail Care", "price": "from €30", "duration": "45–60 min"},
]

SERVICES_TEXT = """✨ *Our Services at Lumina Beauty Studio*

💇 *Haircut* — from €35 (30–60 min)
🎨 *Hair Color* — from €65 (90–180 min)
🧖 *Facial Treatment* — from €55 (60 min)
💆 *Relaxing Massage* — from €60 (60 min)
💅 *Nail Care* — from €30 (45–60 min)

📍 Amsterdam | ⏰ Mon–Sat 9:00–19:00, Sun 10:00–17:00

Ready to book? Just tap *Book Now* below! 👇"""

PRICES_TEXT = """💰 *Price List — Lumina Beauty Studio*

| Service          | Price      | Duration     |
|------------------|------------|--------------|
| Haircut          | from €35   | 30–60 min    |
| Hair Color       | from €65   | 90–180 min   |
| Facial Treatment | from €55   | 60 min       |
| Relaxing Massage | from €60   | 60 min       |
| Nail Care        | from €30   | 45–60 min    |

All prices are starting prices. Final price depends on hair length, complexity, and products used.

💬 Want to book? Reply *Book Now* or tap the button below!"""

WELCOME_TEXT = """👋 Hi! I'm *Luna*, your virtual assistant at *Lumina Beauty Studio* 💆‍♀️

We offer premium beauty services in the heart of Amsterdam — from haircuts and color to facials, massage, and nail care.

How can I help you today?

1️⃣ Our Services
2️⃣ Prices
3️⃣ Book Now
4️⃣ Ask a Question

Just reply with a number or type your question! ✨"""

SERVICE_OPTIONS = ["Haircut", "Hair Color", "Facial", "Massage", "Nail Care", "Other"]
