# Flatten a 2D list

def flatten(matrix):
    flat = []
    for row in matrix:
        for item in row:
            flat.append(item)
    return flat

assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
