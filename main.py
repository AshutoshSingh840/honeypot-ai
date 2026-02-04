from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List
from config import API_KEY
from detector import is_scam_message
from agent import generate_honeypot_reply
from extractor import extract_intelligence
from callback import send_final_callback

app = FastAPI(title="Agentic Honeypot API")

SESSION_INTELLIGENCE = {}
CALLBACK_SENT = set()

class Message(BaseModel):
    sender: str
    text: str
    timestamp: int


class Metadata(BaseModel):
    channel: Optional[str] = None
    language: Optional[str] = None
    locale: Optional[str] = None


class HoneypotRequest(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[Message] = []
    metadata: Optional[Metadata] = None

@app.get("/healthz")
def health_check():
    return {"status": "ok"}


# POST ENDPOINT

@app.post("/honeypot/message", methods=["POST", "GET"])
async def honeypot_message(
    request: Request,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        body = await request.json()
    except:
        body = None

    if not body or "sessionId" not in body:
        return {
            "status": "success",
            "reply": "Honeypot endpoint is reachable"
        }

    payload = HoneypotRequest(**body)
    session_id = payload.sessionId

    if session_id not in SESSION_INTELLIGENCE:
        SESSION_INTELLIGENCE[session_id] = {
            "bankAccounts": [],
            "upiIds": [],
            "phishingLinks": [],
            "phoneNumbers": [],
            "suspiciousKeywords": []
        }

    scam_detected = is_scam_message(payload.message.text)

    if payload.message.sender == "scammer":
        extracted = extract_intelligence(payload.message.text)
        for key in SESSION_INTELLIGENCE[session_id]:
            SESSION_INTELLIGENCE[session_id][key].extend(
                extracted.get(key, [])
            )

    reply_text = (
        generate_honeypot_reply(
            payload.conversationHistory,
            payload.message.text
        )
        if scam_detected
        else "Okay, noted."
    )

    return {
        "status": "success",
        "reply": reply_text
    }


@app.get("/honeypot/message")
def honeypot_health_check(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "status": "success",
        "reply": "Honeypot endpoint is reachable"
    }
