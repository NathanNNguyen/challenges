# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:

# Input: "A"
# Output: 1
# Example 2:

# Input: "AB"
# Output: 28
# Example 3:

# Input: "ZY"
# Output: 701

import string


class Solution:
    def titleToNumber(self, s):
        cache = {}
        count = 1
        for i in string.ascii_uppercase:
            cache[i] = count
            count += 1
        result = 0
        exponent = 0
        for i in range(len(s) - 1, -1, -1):
            val = cache[s[i]] * 26**exponent
            result += val
            exponent += 1
        return result


print(Solution().titleToNumber('ZY'))
