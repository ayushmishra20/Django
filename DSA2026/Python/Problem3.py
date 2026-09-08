'''
On to Problem 3: Move Target to End
This bridges directly into LeetCode #283 (Move Zeroes).

Task:
Given a list nums and a target integer, return a new list where all non-target numbers come first, and all occurrences of target are moved to the end. Keep the relative order of the other numbers unchanged.

Input: nums = [0, 1, 0, 3, 12], target = 0

Expected Output: [1, 3, 12, 0, 0]
'''

nums = [0,1,0,3,12]
new_list = []
target = 0

for num in nums:
    if num != target:
        new_list.append(num)
        
missing_count = len(nums) - len(new_list)

for i in range(missing_count):
    new_list.append(target)

print(new_list)