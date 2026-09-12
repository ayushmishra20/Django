'''
Low-Level Warm-Up: Count Unique Adjacent Elements
Before modifying an array in-place, practice identifying when an element changes in a sorted list.

Task:
Given a sorted list nums, count how many unique numbers exist by comparing each element only to the element before it.

Input: nums = [1, 1, 2, 2, 2, 3]

Expected Output: 3 (the unique numbers are 1, 2, and 3)

Rule:
Do not use set() or len(). Use a single for loop starting from index 1.
'''

lst = [1,1,2,2,2,3]

unique_count = 1

for i in range(1, len(lst)):
    if lst[i] != lst[i-1]:
        unique_count += 1
    pass

print(unique_count)



