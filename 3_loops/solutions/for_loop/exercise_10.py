# Sum of all consecutive pairs

def sum_consecutive_pairs(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i] + lst[i + 1])
    return result

assert sum_consecutive_pairs([1, 3, 5, 7]) == [4, 8, 12]
assert sum_consecutive_pairs([10, 20]) == [30]
assert sum_consecutive_pairs([5]) == []
