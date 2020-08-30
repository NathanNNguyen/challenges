# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1

class Solution:
    def firstMissingPositive(self, nums):
        if len(nums):
            max_val = max(nums)
            if max_val <= 0:
                max_val = 1
            s = set(nums)
            for i in range(1, max_val + 2):
                if i not in s:
                    return i
        else:
            return 1


nums = [0, 1, 2]
nums = [-5]
nums = [-1, -2]
print(Solution().firstMissingPositive(nums))
