class Solution:
    def rob(self, nums):
        # if nums is undefined, return 0
        if not nums:
            return 0
        # if len(nums) < 3, get the max value
        if len(nums) < 3:
            return max(nums)

        # create a dynamic array equal to the len of nums
        dp = [0] * len(nums)

        # first dynamic array item will equal to first item in nums
        dp[0] = nums[0]

        # second item will be max of first and sencond item in nums
        dp[1] = max(nums[0], nums[1])

        # now we can start looping through the array at the 3rd index
        for i in range(2, len(nums)):

            # we can't rob houses adjacent to eachother so it has to skip 1 house
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]


nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
