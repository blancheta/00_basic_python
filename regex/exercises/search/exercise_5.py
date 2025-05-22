import re

text = "Send your resume to jobs@company.org"
match = re.search(r"<To replace with regex here>", text)

result = match.group() if match else None
assert result == "jobs@company.org"
