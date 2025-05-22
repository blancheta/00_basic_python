import re

text = "Apples, bananas; oranges. Grapes"
parts = re.split(r"[;,\.]\s*", text)

assert parts == ['Apples', 'bananas', 'oranges', 'Grapes']
