# Write a Python program to create a shallow copy of sets


def exercise_8(animals: set) -> set:
    return animals.copy()


animals = {"Fox", "Cat", "Dog"}

assert id(exercise_8(animals)) != id(animals)