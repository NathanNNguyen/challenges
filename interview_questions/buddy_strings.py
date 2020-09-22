# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
# Input: A = "", B = "aa"
# Output: false

class Solution:
    def buddyStrings(self, a, b):
        c = {}
        for i in range(len(a)):
            if a[i] != b[i]:
                c[i] = a[i]
        if len(c) != 2:
            return False
        r = ''
        for i in range(len(b)):
            if i in c:
                r += c[i]
                continue
            r += b[i]
        if r == a:
            return True


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
