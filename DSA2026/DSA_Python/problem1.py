'''
Problem 1: Manual Reverse
Write a function reverse_list(nums) that reverses an array in-place using two pointers (one at index 0, one at index len(nums) - 1) and returns it.

Input: [1, 2, 3, 4, 5]

Expected Output: [5, 4, 3, 2, 1]

'''

lst = [1,2,3,4,5]
left = 0
right = len(lst) - 1

while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1
    
print(lst)
    