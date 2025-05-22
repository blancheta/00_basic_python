import re

text = "13:45 - meeting with team"
match = re.match(r"\d{2}:\d{2}", text)

result = match.group() if match else None
assert result == "13:45"