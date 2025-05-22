import re

# Matching
text = "manufacturer"

# Not matching
# text = "fact"

match = re.search(r"\Bfact\B", text)

result = match.group() if match else None
print(result)
assert result == "fact"