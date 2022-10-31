# Write a Python script to merge two Python dictionaries.

dict1 = {"type": "dog"}
dict2 = {"name": "Waouf"}


def exercise_1(dict1, dict2):
    return dict1 | dict2


# Another way that i remebered
def exercise_2(dict1, dict2):
    return {**dict1, **dict2}


# 3
def exercise_3(dict1, dict2):
    return dict1.update(dict2)


assert exercise_1(dict1, dict2) == {"type": "dog", "name": "Waouf"}
