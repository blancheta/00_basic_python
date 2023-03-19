# TODO: Write a Python program
#       to create a flat list from values in a dictionary


def exercise_15(dict1):
    flat_list = []
    for value in dict1.values():
        flat_list.append(value)
    return flat_list

dict1 = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
assert exercise_15(dict1) == [19, 20, 21, 20]
