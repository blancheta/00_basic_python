# Return a list counting down from n to 1 using a while loop.

def countdown(n):
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result

assert countdown(5) == [5, 4, 3, 2, 1]
