class Solution:
    def check (self, d1, d2):
        for k in d1:
            if d2[k] < d1[k]:
                return False
        return True
            
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        
        ans = ""
        cnt = Counter(t)
        record = defaultdict(int)
        left = 0
        min_l = m+1


        for right in range(m):
            record[s[right]] += 1
            while self.check(cnt, record):
                l = right - left + 1
                if l < min_l:
                    min_l = l
                    ans = s[left : right + 1]
                record[s[left]] -= 1
                left += 1
        return ans
            
            

            