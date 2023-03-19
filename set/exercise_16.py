# Write a Python program to find the elements in a given set that are not in another set


def exercise_16(first_set: set, second_set: set) -> str:
    return first_set.symmetric_difference(second_set).pop()


cars_1 = {"Ferrari"}
cars_2 = {"Ferrari", "Mclaren"}

assert exercise_16(cars_1, cars_2) == "Mclaren"
