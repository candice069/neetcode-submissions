class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = float('-inf')
        cnt = Counter()

        left = 0
        for right in range(len(s)):
            cnt[s[right]] += 1
            while right - left + 1 - max(cnt.values()) > k:
                cnt[s[left]] -=1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans