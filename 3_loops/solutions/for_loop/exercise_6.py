# Find the largest number in a list

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

assert find_max([4, 1, 9, 3]) == 9
assert find_max([-5, -2, -10]) == -2
