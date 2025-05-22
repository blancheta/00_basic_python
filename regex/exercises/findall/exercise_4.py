import re

text = "Please contact us at support@example.com or sales@example.org."
result = re.findall(r"<To replace with regex here>", text)

assert result == ['support@example.com', 'sales@example.org']