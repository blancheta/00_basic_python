# Write a Python program to filter even numbers from a given dictionary values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}


original_dict = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
original_dict2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}


def pop_even_number(dict_to_filter):
    result = {}
    for k, v in dict_to_filter.items():
        filtered = [i for i in v if i % 2 == 0]
        result[k] = filtered
    return result


assert pop_even_number(original_dict) == {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
assert pop_even_number(original_dict2) == {'V': [], 'VI': [], 'VII': [2]}
