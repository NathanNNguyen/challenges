# Given two strings, determine the edit distance between them. The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

# Here's the signature:

# def distance(s1, s2):
#   # Fill this in.

# print distance('biting', 'sitting')
# # 2

def distance(s1, s2):
    cache = {}
    len1 = len(s1)
    len2 = len(s2)
    if len2 > len1:
        for i in range(len2):
            if s2[i] not in cache:
                cache[s2[i]] = 1
            else:
                cache[s2[i]] += 1
    for i in s1:
        if i in cache:
            if cache[i] >= 1:
                print(i, cache[i])
        else:
            print(i, 'not in cache')


s1 = 'biting'
s2 = 'sitting'

print(distance(s1, s2))
