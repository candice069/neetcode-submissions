class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = nums[0]
        i = 0

        while i < len(nums):
            if max_distance < i:
                return False
            max_distance = max(max_distance, nums[i] + i)
            if max_distance >= len(nums) - 1:
                return True
            i += 1