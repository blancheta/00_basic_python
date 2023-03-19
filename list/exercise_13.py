# TODO: Write a Python program
#       to print the numbers of a specified list
#       after removing even numbers from it.


def exercise_13(list1: list) -> bool: # it is uncleared to me how method should return bool?
    res = []
    for item in list1:
        if item % 2 != 0:
            res.append(item)
    return res


list1 = [1, 2, 46, 7, 8, 9, 56]
assert exercise_13(list1) == [1, 7, 9]

list1 = [1, 78, 26, 7, 56, 27, 304]
assert exercise_13(list1) == [1, 7, 27]

list1 = [1, -78, 26, 7, -56, 27, -304]
assert exercise_13(list1) == [1, 7, 27]