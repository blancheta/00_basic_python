# TODO: Write a Python program
#       to print all unique values in a dictionary.

dict1 = {
    1: 3,
    2: 3,
    4: 70,
    67: 9888
}


def exercise_3(dict1):
    unique_values_dict = {}
    for key, value in dict1.items():
        if value not in unique_values_dict.values():
            unique_values_dict[key] = value
    for value in unique_values_dict.values():
        print(value)


exercise_3(dict1)
