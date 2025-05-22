import re

# Matching
text = "Hello, how are you"

# Not matching
# text = "What about youself?"

match = re.search(r"\byou\b", text)

result = match.group() if match else None
print(result)
assert result == "you"