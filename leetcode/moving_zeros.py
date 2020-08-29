# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


def moveZeroes(nums):
    cache = {}
    for i in range(len(nums)):
        if nums[i] == 0:
            cache[i] = nums[i]
    for k in sorted(cache.keys(), reverse=True):
        nums.pop(k)
        nums.append(0)
    print(nums)


nums = [0, 0, 1]

print(moveZeroes(nums))
