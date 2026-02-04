# Agentic Honeypot for Scam Detection & Intelligence Extraction

An AI-powered **agentic honeypot system** that detects scam attempts, autonomously engages scammers with human-like responses, extracts actionable intelligence, and reports results via a mandatory callback API.

This project is built **strictly according to the hackathon problem statement** and focuses on correctness, autonomy, and evaluation readiness.

---

## 🚀 Key Features

- Scam intent detection from incoming messages
- Autonomous honeypot agent with human-like, multi-turn conversation handling
- Real-time extraction of scam intelligence:
  - UPI IDs
  - Phone numbers
  - Phishing links
  - Suspicious keywords
- Secure REST API with API key authentication
- Mandatory final callback reporting to evaluation endpoint
- Lightweight, reliable, and demo-friendly design

---

## 🧠 Why This Is Agentic

Once scam intent is detected, the system **autonomously decides**:
- how to respond like a real user,
- how to probe the scammer for more information,
- when enough intelligence is collected,
- and when to trigger the final callback.

No external orchestration is required.

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server
- **Requests** — outbound callback
- **Regex-based extraction** — deterministic and reliable

(No database, no frontend — backend-only as required)

---

## 📂 Project Structure

ai_honeypot/
│
├── main.py # Main FastAPI application
├── detector.py # Scam detection logic
├── agent.py # Honeypot agent (human-like replies)
├── extractor.py # Intelligence extraction logic
├── callback.py # Mandatory final callback sender
├── config.py # API key configuration
├── requirements.txt
└── README.md

## 🔐 API Authentication

All requests must include an API key:
    Header: x-api-key: <YOUR_API_KEY>


---

## 📡 API Endpoint

### POST `/honeypot/message`

Handles incoming messages and returns a honeypot reply.

#### Example Request Body

```json
{
  "sessionId": "demo-session-1",
  "message": {
    "sender": "scammer",
    "text": "Your bank account will be blocked. Verify now.",
    "timestamp": 1770005528731
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}

Example Response

{
  "status": "success",
  "reply": "This is strange… I just used my account yesterday. Can you explain what the issue is?"
}

📦 Intelligence Extracted

The system aggregates intelligence across conversation turns:

    1. bankAccounts
    2. upiIds
    3. phishingLinks
    4. phoneNumbers
    5. suspiciousKeywords

🔔 Mandatory Final Callback

Once scam intent is confirmed and sufficient engagement is completed, the system automatically sends the extracted intelligence to the official evaluation endpoint:
POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult

Callback Payload Structure:
    {
    "sessionId": "abc123-session-id",
    "scamDetected": true,
    "totalMessagesExchanged": 5,
    "extractedIntelligence": {
        "bankAccounts": [],
        "upiIds": ["scammer@upi"],
        "phishingLinks": ["http://fake-link.com"],
        "phoneNumbers": ["+919999999999"],
        "suspiciousKeywords": ["urgent", "verify"]
    },
    "agentNotes": "Scammer used urgency and attempted payment redirection"
    }

▶️ Running the Project
    Install dependencies
        pip install -r requirements.txt

    Start the server
        python -m uvicorn main:app --reload
