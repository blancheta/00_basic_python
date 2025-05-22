import re

text = "The movie was bad, the acting was ugly, but the music was good."
censored = re.sub(r"\b(bad|ugly)\b", "***", text, flags=re.IGNORECASE)

assert censored == "The movie was ***, the acting was ***, but the music was good."