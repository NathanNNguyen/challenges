# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        # make a dict to keep input from string
        cache = {}
        for i in s:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
        # make a result empty string
        result = ''

        # loop through the dict based on the sorted reverse values
        sort_cache = sorted(cache.items(), key=lambda x: x[1], reverse=True)

        # add the char to the result string
        # with value being the amound of that char
        for i in sort_cache:
            if i[1] > 1:
                result = result + i[1] * i[0]
            else:
                result += i[0]
        return result


s = 'tree'
s = 'aaaccc'
s = 'bbAa'
print(Solution().frequencySort(s))
