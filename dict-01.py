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
Q-2

'''