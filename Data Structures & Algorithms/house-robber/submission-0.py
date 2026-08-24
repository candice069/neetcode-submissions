class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i]:consider the first i houses, the money that we can rob at most.
        #at ith house, we can choose: rob or not rob, it depends on max(dp[i-1], dp[i-2] + money[i])
        n = len(nums)
        if n <= 2:
            return max(nums)
        #for dp[i], we just consider the most money till now.
        dp = [0] * (n+1)
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(3, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[n]
