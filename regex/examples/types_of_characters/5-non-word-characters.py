import re

# Matching
text = "Discount %10"


# Not matching
# text = "123"

# match = re.match(r"\w", text)
match = re.findall(r"\W", text)
result = match if match else None

print(result)

assert result is not None