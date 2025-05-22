import re

text = "one1two22three333four"
parts = re.split(r"<To replace with regex here>", text)
assert parts == ['one', 'two', 'three', 'four']