'''
On to Problem 2: Element Counter
Now let's tackle frequency counting, which is the backbone of LeetCode classics like Two Sum, Contains Duplicate, and Valid Anagram.

Task:
Given a list of numbers, count how many times each number appears using a standard Python dict. Do not use collections.Counter.

Input: nums = [4, 1, 2, 1, 2]

Expected Output: {4: 1, 1: 2, 2: 2}
'''

nums = [4,1,2,1,2]

freq = {}

for num in nums:
    # check if num is present in freq
    if num in freq:
        freq[num]+=1 # freq[num] = freq.get(num, 0) + 1 can be used
    else:
        freq[num] = 1
        
print(freq)