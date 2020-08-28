# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 52 + 122 = 132.

# def findPythagoreanTriplets(nums):
#   # Fill this in.

# print findPythagoreanTriplets([3, 12, 5, 13])
# # True

def findPythagoreanTriplets(nums):
    for i in range(len(nums)):
        if nums[i] ** 2 + nums[i + 1] ** 2 == nums[i + 2] ** 2:
            return True
    return False


findPythagoreanTriplets([3, 12, 5, 13])
