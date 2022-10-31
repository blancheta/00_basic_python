# Write a Python program to check if a specific Key and a value exist in a dictionary.
# Original dictionary:
# [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
# {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
# {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
# {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
# {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Check if a specific Key 'class' and a value 'V' exist in the said dictionary:
# True
# True
# False
# False
# False


def check_specific_key_value(
    dict_to_check,
):
    if ('class', 'V') in dict_to_check.items():
        return True
    return False


assert (
    check_specific_key_value({'student_id': 1, 'name': 'Jean Castro', 'class': 'V'})
    is True
)
assert (
    check_specific_key_value({'student_id': 2, 'name': 'Lula Powell', 'class': 'V'})
    is True
)
assert (
    check_specific_key_value({'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'})
    is False
)
assert (
    check_specific_key_value({'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'})
    is False
)

assert (
    check_specific_key_value({'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'})
    is False
)
