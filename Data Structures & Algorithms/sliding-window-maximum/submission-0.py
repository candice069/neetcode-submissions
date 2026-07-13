class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for right in range(len(nums)):
            while q and q[0] < right - k + 1:
                q.popleft()
            while q and nums[right] >= nums[q[-1]]:
                q.pop()
        
            q.append(right)
            if right >= k-1:
                ans.append(nums[q[0]])
        return ans