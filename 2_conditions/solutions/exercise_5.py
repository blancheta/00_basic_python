# Return 'Fizz' if divisible by 3, 'Buzz' if divisible by 5, 'FizzBuzz' if divisible by both, or the number itself otherwise.
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

assert fizzbuzz(15) == 'FizzBuzz'
assert fizzbuzz(9) == 'Fizz'
assert fizzbuzz(10) == 'Buzz'
assert fizzbuzz(7) == '7'
