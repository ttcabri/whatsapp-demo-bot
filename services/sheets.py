import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from config import GOOGLE_SHEET_ID, GOOGLE_CREDENTIALS_JSON

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

_sheet = None


def _get_sheet():
    global _sheet
    if _sheet is None:
        creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_JSON, scopes=SCOPES)
        gc = gspread.authorize(creds)
        spreadsheet = gc.open_by_key(GOOGLE_SHEET_ID)
        _sheet = spreadsheet.sheet1
        # Add headers if sheet is empty
        if not _sheet.get_all_values():
            _sheet.append_row(["Timestamp", "Name", "Service", "Preferred Time", "Phone", "Status"])
    return _sheet


def save_lead(name: str, service: str, preferred_time: str, phone: str) -> None:
    """Save a new booking lead to Google Sheets."""
    sheet = _get_sheet()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, name, service, preferred_time, phone, "New"])
