# agent.py

def generate_honeypot_reply(conversation_history, latest_message):
    """
    Generates a human-like honeypot reply based on conversation state.
    """

    # First response to scammer
    if not conversation_history:
        return (
            "This is strange… I just used my account yesterday. "
            "Can you explain what the issue is?"
        )

    # Follow-up responses
    last_text = latest_message.lower()

    if "verify" in last_text or "verification" in last_text:
        return (
            "I’m not very technical… what exactly do I need to do to verify?"
        )

    if "upi" in last_text or "payment" in last_text:
        return (
            "I don’t usually do payments like this. "
            "Can you guide me step by step?"
        )

    if "link" in last_text:
        return (
            "The link is not opening properly. "
            "Is there another way to complete this?"
        )

    # Default safe reply
    return "Sorry, I didn’t fully understand that. Can you explain again?"
