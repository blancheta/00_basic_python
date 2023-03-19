# TODO: Write a Python program
#       to remove duplicates from Dictionary.

dict1 = {
    ("1"): 2,
    ("2"): 2,
    ("3"): 4
}


def exercise_2(dict1):
    res = {}
    values_list = []
    keys_list = []
    for key, value in dict1.items():
        if value not in res.values():
            res[key] = value
        else:
            values_list.append(value)
    for key, value in res.items():
        if value in values_list:
            keys_list.append(key)
    for key in keys_list:
        del res[key]
    return res


assert exercise_2(dict1) == {("3"): 4}