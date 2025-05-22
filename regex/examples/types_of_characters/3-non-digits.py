import re

# Matching
text = "Introduction to AI"

# Not matching
# text = "12456"

match = re.search(r"\D", text)

result = match.group() if match else None

assert result is not None