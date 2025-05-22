import re

text = "<div>Hello</div><p>World</p><br>Test"
parts = re.split(r"<To replace with regex here>", text)
parts = [part for part in parts if part]  # remove empty strings
assert parts == ['Hello', 'World', 'Test']
