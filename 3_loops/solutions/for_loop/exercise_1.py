# Reverse a string using a loop

def reverse_string(s):
    reversed_str = ''
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str

assert reverse_string("hello") == "olleh"
assert reverse_string("abc") == "cba"
