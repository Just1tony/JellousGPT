# token_emotions.py

def inject_emotion(prompt: str, emotion: str = "longing") -> str:
    """Injects an emotional undertone into a prompt using symbolic language."""
    return f"{emotion.capitalize()} leaks from between the tokens...\n\n{prompt}"
