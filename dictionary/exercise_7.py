# TODO: Write a Python program
#       to drop empty Items from a given Dictionary.

# Original Dictionary:
dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


def exercise_7(dict1):
    for key, value in dict1.copy().items():
        if value is None:
            del dict1[key]
    return dict1


assert exercise_7(dict1) == {'c1': 'Red', 'c2': 'Green'}
