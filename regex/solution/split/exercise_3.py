import re

text = "one1two22three333four"
parts = re.split(r"\d+", text)
assert parts == ['one', 'two', 'three', 'four']