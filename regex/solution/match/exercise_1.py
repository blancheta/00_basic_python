import re

text = "Hello, how are you?"
match = re.match(r"Hello", text)

result = match.group() if match else None
assert result == "Hello"
