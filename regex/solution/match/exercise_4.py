import re

text = "https://example.com is the site"
match = re.match(r"https?://", text)

result = match.group() if match else None
assert result == "https://"