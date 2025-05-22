# Return True if a year is a leap year, else False.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

assert is_leap_year(2024) == True
assert is_leap_year(1900) == False
assert is_leap_year(2000) == True
