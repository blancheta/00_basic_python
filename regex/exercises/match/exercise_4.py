import re

text = "https://example.com is the site"
match = re.match(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "https://"