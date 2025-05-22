import re

text = "The background color is set to #ff5733 in the CSS."
match = re.search(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "#ff5733"