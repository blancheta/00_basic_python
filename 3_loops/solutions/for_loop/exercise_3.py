# Create a list of even numbers from a list

def extract_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

assert extract_evens([1, 2, 3, 4, 5]) == [2, 4]
