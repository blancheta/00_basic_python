# Write a Python program to create set difference.


def exercise_5(first_set: set, second_set: set) -> set:
    return first_set.difference(second_set)


cars_1 = {"Ferrari", "Mercedes"}
cars_2 = {"Ferrari", "Mclaren"}

assert exercise_5(cars_1, cars_2) == {"Mercedes"}