# TODO: Write a Python program
#       to sort a list of dictionaries.
#       by qty


def exercise_17(list1: list) -> list:
    return sorted(list1, key=lambda x: x["qty"])


list1 = [
    {"fruit": "Apple", "qty": 4},
    {"fruit": "Peach", "qty": 10},
    {"fruit": "Plum", "qty": 5},
    {"fruit": "Banana", "qty": 8},
]

assert exercise_17(list1) # there is no assertion
