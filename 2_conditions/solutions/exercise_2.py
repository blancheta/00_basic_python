# Return 'greater' if a > b, 'equal' if a == b, otherwise 'less'.

def compare(a, b):
    if a > b:
        return 'greater'
    elif a == b:
        return 'equal'
    else:
        return 'less'

assert compare(4, 2) == 'greater'
assert compare(5, 5) == 'equal'
assert compare(1, 10) == 'less'
