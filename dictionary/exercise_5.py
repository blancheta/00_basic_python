# Write a Python program to remove spaces from dictionary keys.

dict1 = {" a": 1, "b b b": 2, "e  ": 3}


def format_string(string):
    return string.replace(" ", "")


def exercise_5(dict1):
    result = {}
    for k, v in dict1.items():
        result[format_string(k)] = v
    return result


assert exercise_5(dict1) == {"a": 1, "bbb": 2, "e": 3}
