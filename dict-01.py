'''
 Q-1  Count the frequency of each word in a string using a dictionary.

 def word_frequency(text):
    freq = {}
    words = text.split()  # Split string into words
    
    for word in words:
        word = word.lower()  # Optional: make lowercase for uniformity
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
sentence = "This is a test. This test is only a test."
import string
# Remove punctuation
cleaned = sentence.translate(str.maketrans('', '', string.punctuation))
print(word_frequency(cleaned))

'''
'''
Q-2 # 1. Invert a dictionary (keys become values and values become keys)

original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print("Inverted Dictionary:", inverted)'''


'''Q-3. Merge two dictionaries. If a key exists in both, sum the values
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}
print("Merged Dictionary with Summed Values:", merged)'''

'''Q-4 Find the key with the maximum value in a dictionary
d = {'a': 5, 'b': 9, 'c': 3}
max_key = max(d, key=d.get)
print("Key with Maximum Value:", max_key)'''

'''Q-5 Filter a dictionary to keep only items with values greater than n
n = 4
d = {'a': 3, 'b': 6, 'c': 1}
filtered = {k: v for k, v in d.items() if v > n}
print("Filtered Dictionary (values > n):", filtered)
'''

'''Q-6 Create a nested dictionary from a list of tuples
tuples = [('a', 1), ('b', 2), ('c', 3)]
nested = {k: {'value': v} for k, v in tuples}
print("Nested Dictionary from Tuples:", nested)'''

'''Q-7 Sort a dictionary by its values
d = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print("Dictionary Sorted by Values:", sorted_dict) '''

'''Q-8 Check if two dictionaries are equal
d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}
are_equal = d1 == d2
print("Are Dictionaries Equal?", are_equal)'''

'''Q-9 Create a dictionary with keys from 1 to n and values as their squares
n = 5
squares = {i: i**2 for i in range(1, n+1)}
print("Squares Dictionary:", squares)'''

'''#Q-10. Convert a list of tuples into a dictionary
tuple_list = [('a', 1), ('b', 2), ('c', 3)]
converted_dict = dict(tuple_list)
print("Dictionary from Tuple List:", converted_dict)
 '''   
