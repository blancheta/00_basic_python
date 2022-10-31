# Write a Python program to convert a given dictionary into a list of lists.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]


dict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dict2 = {
    '1': 'Austin Little',
    '2': 'Natasha Howard',
    '3': 'Alfred Mullins',
    '4': 'Jamie Rowe',
}


def convert_dict_to_list(dict_to_convert):
    res = []
    [res.append([k, v]) for k, v in dict_to_convert.items()]
    return res


assert convert_dict_to_list(dict1) == [
    [1, 'red'],
    [2, 'green'],
    [3, 'black'],
    [4, 'white'],
    [5, 'black'],
]
assert convert_dict_to_list(dict2) == [
    ['1', 'Austin Little'],
    ['2', 'Natasha Howard'],
    ['3', 'Alfred Mullins'],
    ['4', 'Jamie Rowe'],
]
