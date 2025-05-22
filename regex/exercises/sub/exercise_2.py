import re

text = "My phone number is 123-456-7890."
cleaned = re.sub(r"(<To replace with regex here>", "-", text)

assert cleaned == "My phone number is ---."