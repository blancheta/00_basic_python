import re

text = "13:45 - meeting with team"
match = re.match(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "13:45"