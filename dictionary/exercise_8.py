# Write a Python program to check all values are same in a dictionary.
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
original_dict = {
    'Cierra Vega': 12,
    'Alden Cantrell': 12,
    'Kierra Gentry': 12,
    'Pierre Cox': 12,
}


def check_values(dict1, original_value):
    if all(value == original_value for value in dict1.values()):
        return True
    return False


assert check_values(original_dict, 12) is True
assert check_values(original_dict, 10) is False
