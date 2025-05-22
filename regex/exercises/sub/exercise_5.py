import re

text = "Card: 1234-5678-9012-3456"
masked = re.sub(r"<To replace with regex here>", "****", text)
print(masked)

assert masked == "Card: ****-****-****-3456"