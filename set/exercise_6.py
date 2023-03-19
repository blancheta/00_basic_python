# Write a Python program to create a symmetric difference


def exercise_6(first_set: set, second_set: set):
    return first_set.symmetric_difference(second_set)


cars_1 = {"Ferrari", "Mercedes"}
cars_2 = {"Ferrari", "Mclaren"}

assert exercise_6(cars_1, cars_2) == {"Mclaren", "Mercedes"}
assert exercise_6(cars_1, cars_2) == {"Mercedes", "Mclaren"}