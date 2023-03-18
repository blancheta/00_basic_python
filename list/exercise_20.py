# TODO: Write a Python program
#       to count integer in a given mixed list.


def exercise_20(list1: list) -> int:
    res = 0
    for item in list1:
        if isinstance(item, int):
            res += item
    return res


list1 = [1, 2, 'a', 'b', 50]

assert exercise_20(list1) == 53
