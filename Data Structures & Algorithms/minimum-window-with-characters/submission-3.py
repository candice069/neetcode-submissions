from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        left = 0
        best_length = float("inf")
        best_left = 0

        for right, char in enumerate(s):
            window[char] += 1

            # 该字符刚好达到需求数量
            if char in need and window[char] == need[char]:
                formed += 1

            # 当前窗口已经包含 t 的所有字符
            while formed == required:
                length = right - left + 1

                if length < best_length:
                    best_length = length
                    best_left = left

                left_char = s[left]
                window[left_char] -= 1

                # 删除后，该字符数量不再满足需求
                if (
                    left_char in need
                    and window[left_char] < need[left_char]
                ):
                    formed -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]