import re

# Matching
text = "Hello, how are you?"
text = "Hecho, how are you?"
text = "how are you, Hello ?"

# Not matching
# text = "Helo, how are you?"

match = re.search(r"He..o", text)

result = match.group() if match else None
print(result)
assert result == "Hello" or result == "Hecho"