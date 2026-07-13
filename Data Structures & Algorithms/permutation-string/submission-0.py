class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        
        cnt1 = Counter(s1)
        record = defaultdict(int)
        left = 0

        for right in range(m):
            record[s2[right]] += 1
            while right - left + 1 > n:
                record[s2[left]] -= 1
                if record[s2[left]] == 0:
                    del record[s2[left]]
                left += 1
            
            if right - left + 1 == n:
                if record == cnt1:
                    return True
            
        return False
