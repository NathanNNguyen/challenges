# Example:
# Input: "banana"
# Output: "anana"

# Input: "million"
# Output: "illi"
# class Solution:
#     def longestPalindrome(self, s):
#       # Fill this in.

# # Test program
# s = "tracecars"
# print(str(Solution().longestPalindrome(s)))
# # racecar

# Brute force solution

class Solution:
    def longestPalindrome(self, s):
        r = ''
        for i in s[::-1]:
            r += i
        result = ''
        for i in range(len(s)):
            if s[i] == r[i]:
                result += r[i]
        return result


s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
