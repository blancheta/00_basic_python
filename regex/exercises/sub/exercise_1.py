import re

text = "The movie was bad, the acting was ugly, but the music was good."
censored = re.sub(r"<To replace with regex here>", "***", text, flags=re.IGNORECASE)

assert censored == "The movie was ***, the acting was ***, but the music was good."