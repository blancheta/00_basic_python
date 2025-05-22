# Return the letter grade for a score between 0 and 100.

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

assert grade(92) == 'A'
assert grade(75) == 'C'
assert grade(59) == 'F'
