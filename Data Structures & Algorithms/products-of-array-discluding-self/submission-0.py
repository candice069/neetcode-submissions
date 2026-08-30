class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #use prefix and suffix to solve
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        
        answer = [0] * n
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]
        return answer