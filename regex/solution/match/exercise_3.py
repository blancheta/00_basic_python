import re

text = "john_doe123 logged in"
match = re.match(r"[A-Za-z]\w*", text)

result = match.group() if match else None
assert result == "john_doe123"