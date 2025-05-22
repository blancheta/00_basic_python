import re

text = "apple\tbanana  orange\npear"
parts = re.split(r"[\s]+", text)
assert parts == ['apple', 'banana', 'orange', 'pear']