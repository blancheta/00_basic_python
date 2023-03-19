# TODO: Write a Python program
#       to find all keys in the provided dictionary
#       that have the given value.

# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Find all keys in the said dictionary that have the specified value:
# ['Roxanne', 'Betty']

def exercise_14(dict1, number):
    dict_list = []
    for key, value in dict1.items():
        if value == number:
            dict_list.append(key)
    return dict_list


dict1 = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

# 1st test
assert exercise_14(dict1, 20) == ['Roxanne', 'Betty']
# 2nd test
assert exercise_14(dict1, 21) == ['Mathew']
# 3rd test
assert exercise_14(dict1, 19) == ["Theodore"]
