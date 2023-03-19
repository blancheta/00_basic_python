# TODO: Write a Python program
#       to create a dictionary from two lists without losing duplicate values.

# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})

list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]


def exercise_6(first_list, second_list):
    res_dict = {}
    for key, value in zip(first_list, second_list):
        if key not in res_dict:
            res_dict[key] = set()
        res_dict[key].add(value)
    return res_dict


assert exercise_6(list1, list2) == {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}}