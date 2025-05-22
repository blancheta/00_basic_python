import re

text = "The server IP is 192.168.1.1 and the backup is 10.0.0.254."
result = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
assert result == ['192.168.1.1', '10.0.0.254']