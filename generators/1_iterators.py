

class Iter:

    def __init__(self, n):
        self.n = n
        self.current = -1
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            self.current += 1
        else:
            raise StopIteration

        return self.current


iterr = Iter(4)

print(next(iterr))
print(next(iterr))
print(next(iterr))
print(next(iterr))
print(next(iterr))
