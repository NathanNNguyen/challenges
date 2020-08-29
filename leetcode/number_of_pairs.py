# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0

class Solution:
    def numIdenticalPairs(self, nums):
        output = 0
        cache = {}
        for i in range(len(nums)):
            for k in range(len(nums)):
                if i == k:
                    continue
                else:
                    if nums[i] == nums[k]:
                        if (i, k) not in cache:
                            cache[k, i] = 1
                            output += 1
                        else:
                            continue
        return output


nums = [1, 2, 3, 1, 1, 3]
print(Solution().numIdenticalPairs(nums))
