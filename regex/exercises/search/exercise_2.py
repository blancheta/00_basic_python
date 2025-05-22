import re

text = "Contact us at 415-555-1234 or email info@example.com"
match = re.search(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "415-555-1234"
