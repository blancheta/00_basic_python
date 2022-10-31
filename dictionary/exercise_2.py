# Write a Python program to remove duplicates from Dictionary.

dict1 = {("1"): 2, ("2"): 2, ("3"): 4}


# This one is a bit messy. I think there is more elegant ways to solve this.
def exercise_2(dict1):
    temp = []
    duplicate_value = []
    new_dict = {}
    for value in dict1.values():
        if value not in temp:
            temp.append(value)
        else:
            duplicate_value.append(value)
    for duplicate in duplicate_value:
        for key, value in dict1.items():
            if duplicate == value:
                continue
            new_dict[key] = value
    return new_dict


assert exercise_2(dict1) == {("3"): 4}
