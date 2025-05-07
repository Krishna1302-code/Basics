'''

# 1. Find repeated tuples in a list 
from collections import Counter
tuples = [(1, 2), (3, 4), (1, 2), (5, 6)]
repeated = [item for item, count in Counter(tuples).items() if count > 1]
print("Repeated Tuples:", repeated) '''

'''# 2. Swap two tuples
a = (1, 2)
b = (3, 4)
a, b = b, a
print("Swapped Tuples: a =", a, ", b =", b)''' 

'''# 3. Sort a list of tuples based on the first element
tuples_list = [(3, 'c'), (1, 'a'), (2, 'b')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[0])
print("Sorted Tuples by First Element:", sorted_tuples)'''

'''# 4. Convert a list to a tuple and vice versa 
lst = [1, 2, 3]
converted_tuple = tuple(lst)
converted_list = list(converted_tuple)
print("List to Tuple:", converted_tuple)
print("Tuple to List:", converted_list) '''

'''# 5. Unpack a tuple of arbitrary length
t = (10, 20, 30, 40)
print("Unpacked Tuple:")
for item in t:
    print(item)''' 

'''# 6. Check if a given element exists in a tuple
t = (1, 2, 3, 4)
element = 3
exists = element in t
print("Element Exists in Tuple?", exists)'''

'''# 7. Concatenate two tuples
t1 = (1, 2)
t2 = (3, 4)
concatenated = t1 + t2
print("Concatenated Tuple:", concatenated)''' 

'''# 8. Find the index of an element in a tuple
t = (10, 20, 30, 40)
index = t.index(30)
print("Index of Element in Tuple:", index)'''

'''# 9. Remove duplicates from a list of tuples
tuples_list = [(1, 2), (3, 4), (1, 2), (5, 6)]
unique_tuples = list(set(tuples_list))
print("Unique Tuples:", unique_tuples) '''

'''# 10. Return the longest tuple from a list of tuples 
tuples_list = [(1,), (1, 2, 3), (2, 3)]
longest = max(tuples_list, key=len)
print("Longest Tuple:", longest) '''

