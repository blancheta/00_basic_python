import re

# Matching
text = "1 - Introduction to AI"

# Not matching
text = "Introduction 1 to AI"

match = re.search(r"\d", text)

result = match.group() if match else None
assert result == "1"