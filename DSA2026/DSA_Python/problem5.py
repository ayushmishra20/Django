'''
Given a list nums and a target, determine if there exist any two distinct numbers that add up to target. Return True if a pair exists, otherwise False.Input: nums = [2, 7, 11, 15], target = 9
Expected Output: True (since $2 + 7 = 9$)The Hash Set / Map PatternFor any number $x$, the required partner to reach the target is:

The Hash Set / Map PatternFor any number $x$, the required partner to reach the target is:$$\text{complement} = \text{target} - x$$Instead of checking every other number with nested loops ($O(N^2)$), store numbers you have already seen in a set or dictionary:Create an empty set seen = set().Loop through each num in nums.Compute complement = target - num.If complement is already in seen, return True.Otherwise, add num to seen and keep going.If the loop ends without finding a pair, return False.
'''

lst = [2,7,11,15]
target = 9

seen = set()

for num in lst:
    complement = target - num
    if complement in seen:
        print("True")
    else:
        num
    print("Notfound")
