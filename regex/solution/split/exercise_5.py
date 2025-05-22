import re

text = "getUserNameAndEmail"
parts = re.split(r"(?=[A-Z])", text)
assert parts == ['get', 'User', 'Name', 'And', 'Email']
