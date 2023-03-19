# Write a Python program to find maximum and the minimum value in a set.


def exercise_11(prices: set):
    return {min(prices), max(prices)}


prices = {20000, 400, 30, 72000}

assert exercise_11(prices) == {72000, 30} # I think this is the correct answer, not == 7200, 30
