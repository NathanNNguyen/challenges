def products(nums):
    arr = []
    for i in nums:
        product = 1
        for j in nums:
            if i == j:
                continue
            product *= j
        arr.append(product)
    return arr


print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
