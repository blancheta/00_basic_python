# TODO: Write a Python program
#       which removes the 0th, 4th and 5th elements of the list passed in input
#       and returns the same list updated

def exercise_12(list_colors: list) -> bool:
    for item in (5, 4, 0):
        list_colors.pop(item)
    return list_colors


list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

assert exercise_12(list1) == ['Green', 'White', 'Black']
