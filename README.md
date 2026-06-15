# 💬 WhatsApp Business Bot — Lumina Beauty Studio

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-webhook-green)
![Claude AI](https://img.shields.io/badge/Claude-AI-orange)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-integrated-brightgreen)
![Deploy](https://img.shields.io/badge/Deploy-Railway-purple)

A production-ready WhatsApp bot for a beauty salon business. Built as a portfolio demo showcasing WhatsApp Business API integration with AI responses and lead capture.

**Live demo:** message +1 415 523 8886 on WhatsApp and type `join [sandbox-word]`

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 Welcome Menu | Quick reply buttons on first message |
| 💅 Services & Prices | Full service catalog with pricing |
| 📋 Lead Capture | 4-step booking flow with state machine |
| 📊 Google Sheets | Leads saved to spreadsheet in real time |
| 🔔 Owner Notifications | Instant Telegram alert on every new lead |
| 🤖 AI Assistant | Claude-powered Q&A for free-text questions |

## 🏗️ Architecture

Built on FastAPI webhook server receiving WhatsApp messages via Twilio sandbox.
Each message goes through a state machine that tracks conversation stage per user.

## 🛠️ Tech Stack

Python 3.11 · FastAPI · Twilio WhatsApp API · Claude API · Google Sheets API · Railway
