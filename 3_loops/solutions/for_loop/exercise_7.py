# Generate multiplication table for a number


def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(n * i)
    return table

assert multiplication_table(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
