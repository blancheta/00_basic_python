# TODO: Write a Python program
#       to find the list of words that are longer
#       than n from a given list of words.


def exercise_10(sample_list: list, n: int) -> bool:
# Your code here
	x_word=[]
	for x in sample_list:
		if(len(x)>n):
			x_word.append(x)
	return x_word


sample_list = ["train", "bike", "cat", "do", "I"]
assert exercise_10(sample_list, 3) == ["train", "bike"]
assert exercise_10(sample_list, 1) == ["train", "bike", "cat", "do"]
