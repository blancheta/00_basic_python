# Write a Python program to find the length of a set


def exercise_12(basket: set) -> int:
    return len(basket)


basket = {"🍪", "🍕", "🍔", "🍿"}

assert exercise_12(basket) == 4
