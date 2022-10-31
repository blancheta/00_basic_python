# Write a Python program to print all unique values in a dictionary.

dict1 = {1: 3, 2: 3, 4: 70, 67: 9888, 5: 5, 7: 5}


def exercise_4(dict1):
    temp = []
    duplicates = []
    for value in dict1.values():
        if value not in temp:
            temp.append(value)
        else:
            duplicates.append(value)
    for value in dict1.values():
        if value in duplicates:
            continue
        print(value)


exercise_4(dict1)
