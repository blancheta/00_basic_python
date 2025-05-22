# Print all prime numbers up to n


def primes_up_to(n):
    primes = []
    for i in range(2, n+1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

assert primes_up_to(10) == [2, 3, 5, 7]
