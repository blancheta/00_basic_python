import re

text = "Hello, how are you?"
match = re.match(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "Hello"
