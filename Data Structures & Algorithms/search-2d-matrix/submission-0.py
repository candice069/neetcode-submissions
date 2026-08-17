class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = m - 1
        col = 0

        while row >= 0 and col < n:
            x = matrix[row][col]

            if target == x:
                return True

            if target > x:
                col += 1
            else:
                row -= 1
        return False