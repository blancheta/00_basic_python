import re

text = "Today's date is 2025-05-16."
result = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
assert result == ['2025-05-16']