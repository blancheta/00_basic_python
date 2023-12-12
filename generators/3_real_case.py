import re
from sys import getsizeof


def itersplit(s, sep=None):
    exp = re.compile(r'\s+' if sep is None else re.escape(sep))
    pos = 0
    while True:
        m = exp.search(s, pos)
        if not m:
            if pos < len(s) or sep is not None:
                yield s[pos:]
            break
        if pos < m.start() or sep is not None:
            yield s[pos:m.start()]
        pos = m.end()


if __name__ == "__main__":
    with open("text_to_read.txt") as f:
        words = f.read().split(" ")
        print("Words size (bytes):", getsizeof(words))

        words_with_generators = itersplit(f.read(), " ")
        print("Words with generators size (bytes):", getsizeof(words_with_generators))
