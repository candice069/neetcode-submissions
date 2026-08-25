class Solution:
    def rob(self, nums: List[int]) -> int:
        #the key is select the last one or not
        n = len(nums)
        if n <= 3:
            return max(nums)
        def rob_line(arr):
            m = len(arr)
            if m <= 2:
                return max(arr)
            
            dp = [0] *(m+1)
            dp[1] = arr[0]
            dp[2] = max(arr[0], arr[1])

            for i in range(3, m+1):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i-1])
            return dp[m]
        return max(rob_line(nums[:n-1]),rob_line(nums[1:]))
        