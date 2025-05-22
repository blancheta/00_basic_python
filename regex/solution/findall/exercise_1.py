import re

text = "There are 24 apples, 13 bananas, and 7 oranges."
result = re.findall(r"\d+", text)
assert result == ['24', '13', '7']