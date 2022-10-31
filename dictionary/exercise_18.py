# Write a Python program to find the key of the maximum value in a dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')

dict_original = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

maximum = max(dict_original.values())
minimum = min(dict_original.values())

keys = tuple([x for x, v in dict_original.items() if v in [minimum, maximum]])
assert keys[::-1] == ('Roxanne', 'Theodore')
