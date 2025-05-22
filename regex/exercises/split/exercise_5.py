import re

text = "getUserNameAndEmail"
parts = re.split(r"<To replace with regex here>", text)
assert parts == ['get', 'User', 'Name', 'And', 'Email']
