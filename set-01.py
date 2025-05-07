
'''# 1. Remove duplicates from a list using a set

a = {1, 2, 3}
b = {3, 4, 5}

print("Set A:", a)
print("Set B:", b)
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (A - B):", a - b)'''


'''# 2. Find union, intersection, and difference of two sets
a = {1, 2, 3}
b = {3, 4, 5}

print("Set A:", a)
print("Set B:", b)
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (A - B):", a - b)'''

'''# 3. Check if one set is a subset or superset of another
a = {1, 2}
b = {1, 2, 3, 4}

print("Set A:", a)
print("Set B:", b)
print("Is A subset of B?", a.issubset(b))
print("Is B superset of A?", b.issuperset(a))'''

'''# 4. Count the number of unique elements in a list using sets 
lst = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(lst)
print("Original List:", lst)
print("Unique elements:", unique_elements)
print("Number of unique elements:", len(unique_elements)) '''

'''# 5. Return all common elements in three sets
a = {1, 2, 3, 4}
b = {2, 3, 5}
c = {2, 3, 6}

common = a & b & c
print("Set A:", a)
print("Set B:", b)
print("Set C:", c)
print("Common elements:", common)'''

'''# 6. Check if two sets have no elements in common
a = {1, 2}
b = {3, 4}

print("Set A:", a)
print("Set B:", b)
print("Are sets disjoint (no common elements)?", a.isdisjoint(b)) '''

'''# 7. Convert a list of strings to a set of unique words
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_words = set(words)
print("Original list:", words)
print("Unique words:", unique_words) '''

'''# 8. Create a set of all characters in a string 
text = "hello world"
char_set = set(text)
print("Original string:", text)
print("Unique characters:", char_set)'''

'''# 9. Remove an arbitrary element from a set and return it
s = {10, 20, 30}
print("Original set:", s)
popped = s.pop()
print("Popped element:", popped)
print("Set after pop:", s) '''

'''# 10. Find elements present in only one of two sets
a = {1, 2, 3}
b = {3, 4, 5}

unique_elements = a ^ b
print("Set A:", a)
print("Set B:", b)
print("Elements in only one set:", unique_elements) '''





