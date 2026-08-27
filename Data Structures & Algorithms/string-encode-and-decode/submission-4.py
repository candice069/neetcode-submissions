class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            n = len(s)
            res += (str(n) + '#' + s)
        return res

    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            if s[j] == '#':
                #find the length of string
                length = int(s[i:j])
                #then use length to find the original string
                ans.append(s[j+1: j+1+length])

                #then, move the pointer to the next start
                i = j+1+length
        return ans
