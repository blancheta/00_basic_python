import re

text = "Apples are amazing and awesome."
result = re.findall(r"<To replace with regex here>", text)

assert result == ['Apples', 'are', 'amazing', 'and', 'awesome']