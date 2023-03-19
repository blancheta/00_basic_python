# Write a Python program to check if a given set is superset of itself and superset of another given set


def exercise_15(big_set, small_set):
    big_set_check = big_set.issuperset(big_set)
    small_set_check = big_set.issuperset(small_set)
    return big_set_check and small_set_check


big_set = {"Pear", "Apple", "Peach"}
small_set = {"Peach"}

assert exercise_15(big_set, small_set) is True
assert exercise_15(small_set, big_set) is False
