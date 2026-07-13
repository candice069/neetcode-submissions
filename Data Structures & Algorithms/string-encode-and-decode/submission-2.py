class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        for s in strs:
            res += (str(len(s)) + '#' + s)

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            tmp = s[j+1 : j+1+n]
            res.append(tmp)
            i = j+1+n
        return res




        return s.split(',')


