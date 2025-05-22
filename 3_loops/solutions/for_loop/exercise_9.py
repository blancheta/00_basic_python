# Count word frequency in a list

def word_count(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

assert word_count(["apple", "banana", "apple", "orange"]) == {'apple': 2, 'banana': 1, 'orange': 1}
