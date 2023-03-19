# TODO: Write a Python program
#       which returns the list of keys
#       where the value equals the maximum value found.


def exercise_17(dict1):
    res_list = []
    for key, value in dict1.items():
        if value == max(dict1.values()):
            res_list.append(key)
    return res_list

# 1st test
dict1 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 22}
assert exercise_17(dict1) == ['Roxanne', 'Betty']

# 2nd test
dict1 = {'Theodore': 25, 'Roxanne': 25, 'Mathew': 21, 'Betty': 20}
assert exercise_17(dict1) == ['Theodore', 'Roxanne'] # should be not ['Roxanne', 'Theodore']
