import re

html = "<html><head><title>Test</title></head><body>Hello</body></html>"
result = re.findall(r"<To replace with regex here>", html)
assert result == ['<html>', '<head>', '<title>', '</title>', '</head>', '<body>', '</body>', '</html>']