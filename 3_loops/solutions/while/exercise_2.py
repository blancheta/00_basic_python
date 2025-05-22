# Return the sum of digits in a number using a while loop.

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

assert sum_digits(1234) == 10
