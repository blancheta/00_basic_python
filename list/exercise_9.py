# TODO: Write a Python program
#       to clone or copy a list


def exercise_9(sample_list: list) -> bool:
    res = []
    for item in sample_list:
        res.append(item)
    return res


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_9(string_list) is not string_list
assert exercise_9(string_list) == string_list