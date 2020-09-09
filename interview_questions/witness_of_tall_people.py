# There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?

# Example:
# Input: [3, 6, 3, 4, 1]
# Output: 3
# Explanation: Only [6, 4, 1] were able to see in front of them.
#  #
#  #
#  # #
# ####
# ####
# #####
# 36341                                 x (murder scene)
# Here's your starting point:

# def witnesses(heights):
#   # Fill this in.

# print witnesses([3, 6, 3, 4, 1])
# # 3

# first pass solution
def witnesses(heights):
    # make a list to keep track of which index
    # can't see the crim scene
    r = []

    # loop through the list
    for i in range(len(heights)):

        # if the value at current index is greater
        # than the value before
        if heights[i] > heights[i - 1]:

            # except the first one, because it will
            # check the last item as the item before it
            if heights[i - 1] == heights[-1]:
                continue

            # otherwise, append the index of the previous value
            else:
                r.append(i - 1)

    # then we can loop through the index list
    # in reverse
    for i in r[::-1]:

        # then start popping out the smaller
        # value in the original list
        heights.pop(i)

    # return the length as of how many are witnesses
    return len(heights)


# double for loop solution
def witnesses(heights):
    r = []
    count = 1
    for i in range(len(heights)):
        for j in heights[count:]:
            if heights[i] < j:
                r.append(i)
                break
        count += 1
    for i in r[::-1]:
        heights.pop(i)

    return len(heights)


heights = [3, 6, 3, 4, 1]
print(witnesses(heights))
