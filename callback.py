import requests

CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"


def send_final_callback(payload: dict):
    try:
        response = requests.post(
            CALLBACK_URL,
            json=payload,
            timeout=10
        )
        print("Callback status:", response.status_code)
        print("Callback response:", response.text)
    except Exception as e:
        print("Callback failed:", str(e))
