import re

text = "john_doe123 logged in"
match = re.match(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "john_doe123"