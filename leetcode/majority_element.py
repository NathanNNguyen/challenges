# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums):
        cache = {}
        for i in nums:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
        for k, v in cache.items():
            if v > len(nums) / 2:
                return k


nums = [3, 2, 3]

print(Solution().majorityElement(nums))

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         result = []
#         cache = {}
#         for i in nums:
#             if i not in cache:
#                 cache[i] = 1
#             else:
#                 cache[i] += 1
#         for k, v in cache.items():
#             if v > len(nums) / 3:
#                 result.append(k)
#         return result
