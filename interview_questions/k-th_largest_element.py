# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5
# Here is a starting point:

# def findKthLargest(nums, k):
#   # Fill this in.

# print findKthLargest([3, 5, 2, 4, 6, 8], 3)
# # 5

def findKthLargest(nums, k):
    nums.sort()
    # print(len(nums) - k)
    for i in nums[::-1]:
        if k == 1:
            return i
        k -= 1
    return None


nums = [3, 5, 2, 4, 6, 8]
nums = [0, 5, 10, 30, 12, 14, 16]
k = 3
print(findKthLargest(nums, k))
