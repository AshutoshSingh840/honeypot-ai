# extractor.py

import re

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "blocked",
    "suspended",
    "payment",
    "upi",
    "account"
]


def extract_intelligence(text: str) -> dict:
    intelligence = {
        "bankAccounts": [],
        "upiIds": [],
        "phishingLinks": [],
        "phoneNumbers": [],
        "suspiciousKeywords": []
    }

    lower_text = text.lower()

    # UPI IDs
    upi_matches = re.findall(r"[\w.-]+@[\w.-]+", text)
    intelligence["upiIds"].extend(upi_matches)

    # Phone numbers (India focused)
    phone_matches = re.findall(r"\+91\d{10}", text)
    intelligence["phoneNumbers"].extend(phone_matches)

    # URLs
    url_matches = re.findall(r"https?://[^\s]+", text)
    intelligence["phishingLinks"].extend(url_matches)

    # Suspicious keywords
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in lower_text:
            intelligence["suspiciousKeywords"].append(keyword)

    return intelligence
