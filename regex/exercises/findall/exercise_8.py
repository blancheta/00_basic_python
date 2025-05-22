import re


text = 'He said "hello" and then she replied \'hi\'.'
result = re.findall(r'<To replace with regex here>', text)
# \1 matches the group 1 character
assert [match[1] for match in result] == ['hello', 'hi']
