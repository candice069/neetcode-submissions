class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_distance = nums[0]
        current_end = 0
        cnt = 0
        i = 0

        while i < len(nums):
            max_distance = max(max_distance, nums[i] + i)
            if i == current_end:
                cnt += 1
                current_end = max_distance
                if current_end >= len(nums) - 1:
                    return cnt
            i += 1
        return cnt

        