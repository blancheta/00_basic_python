# Write a Python program to remove item(s) from a given set.


def exercise_2(set_2: set) -> set:
    set_2.remove("Fox")
    set_2.remove("Cat")
    return set_2


animals_set = set(["Fox", "Eagle", "Dog", "Cat"]) # not set("Fox", "Eagle", "Dog", "Cat")

assert exercise_2(animals_set) == {"Eagle", "Dog"}