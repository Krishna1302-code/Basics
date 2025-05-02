#Q-1 Write a function that counts the number of vowels in a string.
def count_vowels1(name):
    count=0
    for i in range(len(name)):
        if name[i].lower() in 'aeiou':
            count =+ 1
    print("No of vowels:",count)
name='Apple'
count_vowels1(name)
