def predict_anxiety(text):

    text = text.lower()

    if "nervous" in text or "scared" in text:
        return "High"

    elif "worried" in text or "stress" in text:
        return "Moderate"

    else:
        return "Low"