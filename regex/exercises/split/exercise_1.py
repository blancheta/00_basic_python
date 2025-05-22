import re

text = "Apples, bananas; oranges. Grapes"
parts = re.split(r"<To replace with regex here>", text)

assert parts == ['Apples', 'bananas', 'oranges', 'Grapes']
