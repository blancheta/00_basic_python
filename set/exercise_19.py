# Write a Python program to create a set


def exercise_20(elements: list) -> set:
    return set(elements)


elements_to_add = ["Fox", "Fox", "Cat", "Cat", "Dog"]

assert len(exercise_20(elements_to_add)) == 3
assert exercise_20(elements_to_add) == {"Fox", "Cat", "Dog"}
assert exercise_20(elements_to_add) == {"Dog", "Fox", "Cat"}
