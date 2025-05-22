import re

text = "The deadline is 25/12/2025, please submit on time."
match = re.search(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "25/12/2025"
