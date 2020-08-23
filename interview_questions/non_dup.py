# Given a list of numbers, where every number shows up twice except for one number, find that one number.

# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1
# Here's the function signature:


# def singleNumber(nums):
#   # Fill this in.


# print singleNumber([4, 3, 2, 4, 1, 3, 2])
# # 1

def singleNumber(nums):
    cache = {}
    for i in nums:
        if i not in cache:
            cache[i] = 1
        else:
            cache[i] += 1
    for item in cache.items():
        if item[1] == 1:
            return item[0]
    return None


arr = [4, 3, 2, 4, 1, 3, 2]
print(singleNumber(arr))
