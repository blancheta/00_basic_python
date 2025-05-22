import re

text = "notes_2025.txt is saved"
match = re.match(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "notes_2025.txt"