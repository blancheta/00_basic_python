import re

tweet = "Loving the new features in #Python3.10 and #Regex!"
result = re.findall(r"#\w+", tweet)
assert result == ['#Python3', '#Regex']