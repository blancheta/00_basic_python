import re

# Matching
text = "Hello, how are you"

# Not matching
# text = "how are you?, Hello"

match = re.search(r"you\Z", text)
# match = re.search(r"you$", text)

result = match.group() if match else None

assert result == "you"