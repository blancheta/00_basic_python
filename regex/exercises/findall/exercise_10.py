import re

password = "Str0ng@Pass!"
match = re.fullmatch(r"<To replace with regex here>", password)
# In regex, (?=...) is called a positive lookahead.
# What it does:
# It checks if a pattern follows at a certain point without including it in the match.
assert match is not None