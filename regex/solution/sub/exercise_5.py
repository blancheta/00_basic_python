import re

text = "Card: 1234-5678-9012-3456"
masked = re.sub(r"\d{4}(?=-)", "****", text)
print(masked)

assert masked == "Card: ****-****-****-3456"