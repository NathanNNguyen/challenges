# You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

# def staircase(n):
#   # Fill this in.

# print staircase(4)
# # 5
# print staircase(5)
# # 8

# Can you find a solution in O(n) time?

def staircase(n):
    cache = {}
    if n <= 3:
        return n
    if n not in cache:
        cache[n] = staircase(n - 1) + staircase(n - 2)
    return cache[n]


print(staircase(4))
# 5
print(staircase(5))
# 8
print(staircase(3))
