class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        record = set(s[left])
        longest = 1

        for right in range(1, len(s)):
            while s[right] in record:
                record.remove(s[left])
                left += 1
            
            record.add(s[right])
            longest = max(longest, right-left+1)
        return longest