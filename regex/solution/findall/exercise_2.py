import re

text = "The quick brown fox jumps over the lazy dog."
result = re.findall(r"\b\w+\b", text)
assert result == ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']