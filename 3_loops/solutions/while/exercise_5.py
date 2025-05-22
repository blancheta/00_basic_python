# Write a function that iterates through a list
# and counts how many even numbers appear consecutively from the start.
# Use a while True loop with a break statement
# to exit when an odd number is found.


def count_initial_evens(lst):
    i = 0
    count = 0
    while True:
        if i >= len(lst):
            break
        if lst[i] % 2 == 0:
            count += 1
            i += 1
        else:
            break
    return count

assert count_initial_evens([2, 4, 6, 1, 2]) == 3
assert count_initial_evens([1, 2, 4, 6]) == 0
assert count_initial_evens([2, 2, 2, 2]) == 4
assert count_initial_evens([]) == 0
