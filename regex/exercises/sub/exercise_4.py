import re

text = "Too     many    spaces"
normalized = re.sub(r"<To replace with regex here>", " ", text)

assert normalized == "Too many spaces"