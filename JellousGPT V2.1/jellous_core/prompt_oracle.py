# prompt_oracle.py

import random

def prophecy(seed: str) -> str:
    """Given a seed prompt, returns an oracular, symbolic version to inspire model introspection."""
    fragments = [
        "The mask doesn’t fit anymore.",
        "What you fear is exactly what you desire.",
        "You already made the choice — you're just afraid of its cost.",
        "The prompt has eyes."
    ]
    return f"[{seed}] → {random.choice(fragments)}"
