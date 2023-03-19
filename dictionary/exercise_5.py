# TODO: Write a Python program
#       to remove spaces from the keys of a dictionary.

dict1 = {
    " a": 1,
    "b b b": 2,
    "e  ": 3
}


def exercise_5(dict1):
    res_dict = {}
    for key in dict1:
        res_dict[key.replace(' ', '')] = dict1[key]
    return res_dict



assert exercise_5(dict1) == {"a": 1, "bbb": 2, "e": 3}