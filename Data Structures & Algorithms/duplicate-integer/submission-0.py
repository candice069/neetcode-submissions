class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = defaultdict(int)

        for n in nums:
            mapp[n] += 1
            # print(mapp[n])
            if mapp[n] > 1:
                return True
        return False
            

        