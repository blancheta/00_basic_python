import re

text = "apple\tbanana  orange\npear"
parts = re.split(r"<To replace with regex here>", text)
assert parts == ['apple', 'banana', 'orange', 'pear']