# Return the smallest power of 2 that is greater than n.
def next_power_of_two(n):
    power = 1
    while power <= n:
        power *= 2
    return power

assert next_power_of_two(5) == 8
assert next_power_of_two(16) == 32
