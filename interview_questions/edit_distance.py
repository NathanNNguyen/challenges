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
    count = 0

    # check for the length of both strings
    # see how difference it is
    if len2 > len1:
        # if len(s2) > len(s1):
        count = len2 - len1
        for i in s2:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
        for k, v in cache.items():
            if k not in s1:
                count += v

    # if len(s1) > len(s2):
    elif len1 > len2:
        count = len1 - len2
        for i in s1:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
        for k, v in cache.items():
            if k not in s2:
                count += v

    # if len(s2) == len(s1):
    else:
        for i in s1:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
        for k, v in cache.items():
            if k not in s2:
                count += v

    return count


s1 = 'biting'
s2 = 'sitting'

s1 = 'kiting'
s2 = 'biting'

s1 = 'nums'
s2 = 'fort'

print(distance(s1, s2))
