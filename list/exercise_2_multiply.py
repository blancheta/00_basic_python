# TODO: Write a Python program
#       to multiply all the items in a list.


def exercise_2(numbers: list) -> int:
    res = 1
    for item in numbers:
        res *= item
    return res


numbers = [1, 2, 3, 4]
total = exercise_2(numbers)
assert total == 24
