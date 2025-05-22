import re

text = "convert_this_string"
converted = re.sub(r"<To replace with regex here>", lambda m: m.group(1).upper(), text)

assert converted == "convertThisString"