from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #use greedy + binary search
        tail = [] #maintain the array to add the current minimum last element

        for x in nums:
            #find the insert position
            index = bisect_left(tail, x)
            if index == len(tail):
                tail.append(x)
            else:
                tail[index] = x
        return len(tail)
