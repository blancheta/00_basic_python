# TODO: Write a Python program
#       to return a dictionary containing
#       the frequency of elements found in a list.


def exercise_14(list1: list) -> dict:
    res = {}
    for item in list1:
        res[item] = res.get(item, 0) + 1
    return res


list1 = ["a", "a", "b", "b", "c", "d", "d", "d"]
assert exercise_14(list1) == {
    'a': 2,
    'b': 2,
    'c': 1,
    'd': 3
}
