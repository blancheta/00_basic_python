import re

# Matching
text = "Hello, how are you?"

# Not matching
# text = "how are you?, Hello"

match = re.match(r"\AHello", text)
# match = re.match(r"^Hello", text)

result = match.group() if match else None
assert result == "Hello"