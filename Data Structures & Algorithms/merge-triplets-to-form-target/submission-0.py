class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        unavail = set()
        for i, [x, y, z] in enumerate(triplets):
            if x > target[0] or y > target[1] or z > target[2]:
                unavail.add(i)
        
        a, b, c = 0, 0, 0
        for i, [x, y, z] in enumerate(triplets):
            if i not in unavail:
                a, b, c = max(a,x), max(b,y), max(c,z)
        return [a, b ,c] == target