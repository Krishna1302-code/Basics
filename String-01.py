#Q-1 Write a function that counts the number of vowels in a string.
'''def count_vowels1(name):
    count = 0
    for char in name:# char is storing the actual characters of name[Nidhi]
        if char.lower() in 'aeiou':
            count += 1
    print("No of vowels:", count)
name = "Nidhi"
print("Input name:", name)
count_vowels1(name)'''

'''
-------------------------------------------------------------
### 🔹 1. **Loop through values only**

name = "Nidhi"
for char in name:
    print(char)

**Output:**

N
i
d   
h
i

✅ `char` stores **each character (value)**, not the index.
-------------------------------------------------------------

### 🔹 2. **Loop through indexes only**

name = "Nidhi"
for i in range(len(name)):
    print(i)

**Output:**
0
1
2
3
4
✅ `i` stores the **index** only — not the character.
-----------------------------------------------------------

-----------------------------------------------------------
### 🔹 3. **Loop through both index and value**

name = "Nidhi"
for i, char in enumerate(name):
    print(i, char)

**Output:**
0 N
1 i
2 d
3 h
4 i
```
✅ `i` = index, `char` = character at that index.
-----------------------------------------------------------------------------------------------------------------------------------------
'''

'''Q-2 Reverse a string without using built-in functions.
def reverse(name):
    reversed_string=''
    for i in range(len(name)-1 ,-1 ,-1 ):
        reversed_string += name[i]
    print("Reversed-string",reversed_string)
name="Krishna"
print("Name=:",name)
reverse(name)
'''

'''
### `range(start, stop, step)`
Used to loop with a start point, an endpoint (exclusive), and a step (how much to increase or decrease each time).
-----------------------------------------------------------------------------------------------------------------------------
### For `range(len(string)-1, -1, -1)`:

1. **First `-1` (in `len(string)-1`)**: This gives the **last positive index** of the string.
   👉 Example: For `"hello"`, `len("hello") - 1 = 4`.

2. **Second `-1` (stop value)**: This is the **end point**, but exclusive.
   👉 It tells the loop to **stop before reaching index -1**, so the last index included is `0`.

3. **Third `-1` (step)**: This means the index is **decreased from the last positive index (e.g., 4 → 3 → 2 → 1 → 0)**.
   👉 It moves **backwards through the positive indices** of the string.
------------------------------------------------------------------------------------------------------------------------------------------
'''

'''Q-3 Check if a given string is a palindrome.

Palindrome**: A string that reads the same forward and backward.
Example**:   `"madam"` is a palindrome because reversing it gives `"madam"`.
Non-palindrome**: A string like `"hello"` that changes when reversed.


def reverse(name):
    reversed_string=''
    for i in range(len(name)-1 ,-1 ,-1 ):
        reversed_string += name[i]
    print("Reversed-string",reversed_string)
    if(reversed_string==name):
        print("its palindrome")
    else:
        print("no, its not plaindrome")
name="krishna"
print("Name=:",name)
reverse(name)
------------------------------------------------------------------------------------------------------------------------------------------

'''
''' Q-4 Remove all duplicate characters from a string.
def remove_dupes(original):
    result="" #""-> initializing empty and " "-> means initializing a space
    for char in original:
        if char not in result:result += char            
    print("Here are the unique characters",result)
original="Krishna"
print("Original string:",original)
remove_dupes(original)


✅ not in works with:
Strings → 'a' not in 'hello'
Lists → 3 not in [1, 2, 3]
Tuples → 'x' not in ('a', 'b', 'c')
Sets → 5 not in {1, 2, 3}
Dictionaries → 'key' not in {'key': 'value'} (checks keys only)
------------------------------------------------------------------------------------------------------------------------------------------
'''
'''Q-5 Count the frequency of each character in a string.
-Gonna learn new topic which is collections.counter 
*`Counter`*(from `collections` module) is a dictionary-like class that counts the frequency of elements in an iterable, 
returning a mapping of elements to their counts.

from collections import Counter
string="Hello"
count=Counter(string)
print(count)
------------------------------------------------------------------------------------------------------------------------------------------
'''
'''Q-6 Capitalize the first letter of each word in a string.

name="my name is krishna"
print(name.title())


->To capitalize the first letter of each word in a string means converting the first character of each word to uppercase,
while keeping the rest of the word in lowercase.
->This is often done using .title() or by splitting the string and capitalizing each word manually.
--------------------------------------------------------------------------------------------------------------------------------------------
'''
'''Q-7 Find the longest word in a sentence.

Sentence="My name is Krishna and i'm fashion designer"
longest=max(Sentence.split(),key=len)
print(longest)

To find the longest word in a sentence:
Use .split() to break the sentence into words.
Use max(words, key=len) to get the word with the most characters.
key=len tells Python to compare words based on their length.
--------------------------------------------------------------------------------------------------------------------------------------------
'''

''' Q-8 Replace all spaces in a string with underscores.
sentence="My name is Krishna"
print(sentence.replace(" ","_"))
--------------------------------------------------------------------------------------------------------------------------------------------
'''

'''Q-9 Write a function to find all substrings of a string.
--------------------------------------------------------------------------------------------------------------------------------------------
'''

'''Q-10 Check if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))    
--------------------------------------------------------------------------------------------------------------------------------------------
'''

