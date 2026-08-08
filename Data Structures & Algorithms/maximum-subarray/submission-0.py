class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        current_max = 0

        for x in nums:
            current_max = max(current_max + x, x)
            if current_max < 0:
                current_max =x
            ans = max(current_max, ans)
        return ans
        