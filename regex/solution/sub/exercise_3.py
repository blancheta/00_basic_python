import re

text = "convert_this_string"
converted = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

assert converted == "convertThisString"