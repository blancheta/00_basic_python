# Sum numbers from 1 to n

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
