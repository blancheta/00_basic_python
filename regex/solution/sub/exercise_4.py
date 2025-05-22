import re

text = "Too     many    spaces"
normalized = re.sub(r"\s+", " ", text)

assert normalized == "Too many spaces"