# Find all the pairs of two integers in an unsorted array that sum up to a given S.
# For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7,
# your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7. 


arr = [3, 5, 2, -4, 8, 11]
s = 7


def pairs(arr, s):
    c = {}
    r = []

    for i in range(len(arr)):
        diff = s - arr[i]
        c[diff] = i

    for i in arr:
        if i in c:
            if [i, arr[c[i]]] in r or [arr[c[i]], i] in r:
                continue
            r.append([i, arr[c[i]]])
    return r
    # r = []
    # for i in arr:
    #     for j in arr:
    #         # check if i + j == total and i and j not in result arr
    #         if [i, j] in r or [j, i] in r:
    #             continue
    #         if i + j == s:
    #             r.append([i, j])

    # return r


print(pairs(arr, s))
