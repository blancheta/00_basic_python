import re

text = "Today's date is 2025-05-16."
result = re.findall(r"<To replace with regex here>", text)
assert result == ['2025-05-16']