# Write a Python program to create an intersection of sets


def exercise_3(first_set: set, second_set: set) -> set:
    return first_set.intersection(second_set)


set_1 = {"Ferrari", "Mercedes"}
set_2 = {"Ferrari", "Mclaren"}

assert exercise_3(set_1, set_2) == {"Ferrari"}