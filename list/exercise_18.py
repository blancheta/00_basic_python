# TODO: Write a Python program
#       to generate all permutations of a list in Python.


def exercise_18(list1: list) -> list:
    if len(list1) == 0:
        return []

    if len(list1) == 1:
        return [tuple(list1)]

    permutations = []

    for i in range(len(list1)):
        current = list1[i]
        remaining = list1[:i] + list1[i+1:]

        for permutation in exercise_18(remaining):
            permutations.append((current,) + permutation)

    return permutations


list1 = [1, 2, 3]
assert exercise_18(list1) == [
    (1, 2, 3),
    (1, 3, 2),
    (2, 1, 3),
    (2, 3, 1),
    (3, 1, 2),
    (3, 2, 1)
]

