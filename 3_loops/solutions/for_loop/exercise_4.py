# Count vowels in a string

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in 'aeiou':
            count += 1
    return count

assert count_vowels("Hello") == 2
assert count_vowels("sky") == 0
