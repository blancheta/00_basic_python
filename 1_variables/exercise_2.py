# TODO: Swap values between two variables

first_word = "Car"
second_word = "Bike"

# Your code here
temp=first_word
first_word=second_word
second_word=temp
assert first_word == "Bike"
assert second_word == "Car"
