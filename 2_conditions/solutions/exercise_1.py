# Write a condition to check if a number is positive and return 'positive' or 'not positive'.

def check_positive(n):
    if n > 0:
        return 'positive'
    else:
        return 'not positive'

assert check_positive(5) == 'positive'
assert check_positive(-3) == 'not positive'
