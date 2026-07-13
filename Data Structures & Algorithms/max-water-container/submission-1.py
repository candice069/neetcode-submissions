class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        ans = 0

        while left <= right:
            area = min(heights[left], heights[right]) * (right - left)
            ans = max(area, ans)
            if heights[right] > heights[left]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
        return ans