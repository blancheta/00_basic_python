import re

text = "Hello there!"
match = re.search(r"<To replace with regex here>", text)

result = bool(match)
assert result == True
