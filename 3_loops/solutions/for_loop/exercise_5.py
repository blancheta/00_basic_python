# Given a list of integers,
# return the index of the first negative number.
# If no negative number exists, return -1.

def first_negative_index(lst):
    for index, value in enumerate(lst):
        if value < 0:
            return index
    return -1

assert first_negative_index([4, 2, -7, 3]) == 2
assert first_negative_index([1, 2, 3]) == -1
assert first_negative_index([-5]) == 0