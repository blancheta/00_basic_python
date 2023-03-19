# TODO: Write a Python program
#       to remove the duplicate in the list.


def exercise_7(sample_list: list) -> list:
    res = []
    for item in sample_list:
        if item not in res:
            res.append(item)
    return res


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_7(string_list) == ['abc', 'xyz', '1221']