# TODO: Write a Python program
#       to get the largest number from a list.


def exercise_3(numbers: list) -> int:
    return max(numbers)


numbers = [1, 2, 3, 4]
largest_number = exercise_3(numbers)
assert largest_number == 4
