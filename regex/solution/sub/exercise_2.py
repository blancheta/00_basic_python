import re

text = "My phone number is 123-456-7890."
cleaned = re.sub(r"(\d{1,4}-?)", "-", text)

assert cleaned == "My phone number is ---."