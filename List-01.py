'''Q-1 Write a function to find the second largest number in a list.

nums = [22, 34, 66, 100]
print(f"All the values of list: {nums}")

f_large = float('-inf')
s_large = float('-inf')

def Second_large():
    global f_large, s_large  # Fix scope issue
    for num in nums:
        if num > f_large:
            s_large = f_large
            f_large = num
        elif num > s_large and num != f_large:
            s_large = num

Second_large()  # Call the function
print(f"Second highest in list: {s_large}")

'''
'''
Q-2 Remove all occurrences of a specific element from a list.

nums=[1,2,3,4]
x=2
print(f"Original list{nums}")
replace=[]
print(f"Original list {nums}")
def remove(nums,x):
    for num in nums:
        if num != x:
            replace.append(num)
remove(nums,x)
print(f"Updated list (without {x}): {replace}")


'''
'''
Q-3 Flatten a nested list (e.g., [[1,2], [3,4]] → [1,2,3,4]).   

nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]
print(flat)

Outer loop (for sublist in nested): Iterates over each sublist in nested.
Inner loop (for item in sublist): Iterates over each item inside the current sublist.
Collect all items into a single list (flat).
'''

'''
Q-4 Rotate a list to the right by k steps.

def rotate_list(nums, k):
    # Ensure k is within the bounds of the list length
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5]
k = 2
rotated = rotate_list(nums, k)
print(rotated)  # ➝ [4, 5, 1, 2, 3]

'''
''' Q-5 '''
'''
Q-6 Count the number of even and odd numbers in a list.


count_even = 0
count_odd = 0

def total_even_odd(nums):
    global count_even, count_odd  # Use 'global' to modify the variables outside the function
    for num in nums:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f"Total even numbers in list: {count_even}")
    print(f"Total odd numbers in list: {count_odd}")

# Example usage
nums = [22, 55, 3, 2, 1]
total_even_odd(nums)
'''
'''
Q-7 find the common elements between two lists.
ist1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = list(set(list1) & set(list2))  # Set intersection
print(f"Common elements: {common_elements}")

'''
'''
Q-8 Sort a list of tuples by the second element.
tuples_list = [(1, 9), (2, 5), (3, 7)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)

'''
'''
Q-9 Write a function to merge two sorted lists into one sorted list.
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0

    # Compare elements and merge
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

a = [1, 3, 5]
b = [2, 4, 6]
print(merge_sorted_lists(a, b))
'''
'''
Q-10 Group elements of a list into a dictionary based on their first letter.

def group_by_first_letter(words):
    grouped = {}
    for word in words:
        first_letter = word[0].lower()  # Get the first letter in lowercase
        if first_letter not in grouped:
            grouped[first_letter] = [word]
        else:
            grouped[first_letter].append(word)
    return grouped
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
result = group_by_first_letter(words)
print(result)
'''
