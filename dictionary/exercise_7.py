# Write a Python program to drop empty Items from a given Dictionary.

# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

sample = {'c1': 'Red', 'c2': 'Green', 'c3': None}

new_dict = {k: v for k, v in sample.items() if v is not None}

assert new_dict == {'c1': 'Red', 'c2': 'Green'}
