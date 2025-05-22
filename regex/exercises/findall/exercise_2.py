import re

text = "The quick brown fox jumps over the lazy dog."
result = re.findall(r"<To replace with regex here>", text)
assert result == ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']