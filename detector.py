SCAM_KEYWORDS = [
    "account blocked",
    "verify immediately",
    "urgent",
    "upi",
    "click link",
    "share otp",
    "suspended",
    "verify now",
    "bank account",
    "payment"
]


def is_scam_message(text: str) -> bool:
    text = text.lower()

    for keyword in SCAM_KEYWORDS:
        if keyword in text:
            return True

    return False
