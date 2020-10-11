def isAlienSorted(Words, Order):
    Order_index = {c: i for i, c in enumerate(Order)}
    # c = {}
    # for index, val in enumerate(Order):
    #     c[index] = val

    for i in range(len(Words) - 1):
        word1 = Words[i]
        word2 = Words[i + 1]

        # Find the first difference word1[k] != word2[k].
        for k in range(min(len(word1), len(word2))):

            # If they compare false then it's not sorted.
            if word1[k] != word2[k]:
                if Order_index[word1[k]] > Order_index[word2[k]]:
                    return False
                break
        else:

            # If we didn't find a first difference, the
            # Words are like ("add", "addition").
            if len(word1) > len(word2):
                return False

    return True


words = ["zyx", "zyxw", "zyxwy"]
order = "zyxwvutsrqponmlkjihgfedcba"
print(isAlienSorted(words, order))
