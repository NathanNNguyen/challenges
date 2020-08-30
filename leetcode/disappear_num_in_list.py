# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


class Solution:
    def findDisappearedNumbers(self, nums):
        arr = []
        s = set(nums)
        for num in range(1, len(nums) + 1):
            if num not in s:
                arr.append(num)
        return arr

        # num_set = set(nums)
        # theory_set = set(range(1, len(nums) + 1))
        # return theory_set - num_set

        # return set(nums) - set(range(1, len(nums) + 1))


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(nums))
