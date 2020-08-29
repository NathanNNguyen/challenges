# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums):
        # for i in nums:
        #     if nums.count(i) == 1:
        #         return i

        cache = {}
        for i in nums:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
        for k, v in cache.items():
            if v == 1:
                return k


nums = [4, 1, 2, 1, 2]

print(Solution().singleNumber(nums))
