import re

# Matching
text = "Discount %10"

# Not matching
# text = "%&"
# text = "-A"

# match = re.match(r"\w", text)
match = re.findall(r"\w", text)
result = match if match else None

print(result)

assert result is not None