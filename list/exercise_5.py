# TODO: Write a Python program to count the number of elements
#       containing a string where length is 2 or more
#       and the first and last character of this string are the same


def exercise_5(strings: list) -> int:
    counter = 0
    for item in strings:
        list_length = len(item)
        if list_length > 1 and item[0] == item[list_length - 1]:
            counter += 1
    return counter


string_list = ['abc', 'xyz', 'aba', '1221']
assert exercise_5(string_list) == 2
