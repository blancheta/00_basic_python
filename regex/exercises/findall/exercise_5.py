import re

tweet = "Loving the new features in #Python3.10 and #Regex!"
result = re.findall(r"<To replace with regex here>", tweet)
assert result == ['#Python3', '#Regex']