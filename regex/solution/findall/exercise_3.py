import re

text = "Apples are amazing and awesome."
result = re.findall(r"\b[Aa]\w*", text)
assert result == ['Apples', 'are', 'amazing', 'and', 'awesome']