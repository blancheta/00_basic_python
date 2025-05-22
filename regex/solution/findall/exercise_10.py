import re

password = "Str0ng@Pass!"
match = re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}", password)
# In regex, (?=...) is called a positive lookahead.
# What it does:
# It checks if a pattern follows at a certain point without including it in the match.
assert match is not None