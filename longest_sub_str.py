class Solution:
    def lengthOfLongestSubstring(self, s):
        cache = set()
        for i in s:
            cache.add(i)
        cache = list(cache)
        return len(cache)


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
