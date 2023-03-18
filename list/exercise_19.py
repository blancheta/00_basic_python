# TODO: Write a Python program
#       to create a multidimensional list (lists of lists) with zeros.
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

def exercise_19(col, row) -> list:
    return [[0] * row for i in range(col)]


assert exercise_19(2, 3) == [
    [0, 0, 0],
    [0, 0, 0]
]
assert exercise_19(4, 4) == [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]