''''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i = j = 0
        while matrix[i][j] != 101:
            while j < n and matrix[i][j] != 101:
                ans.append(matrix[i][j])
                matrix[i][j] = 101
                j += 1

            j -= 1
            i += 1
            while i < m and matrix[i][j] != 101:
                ans.append(matrix[i][j])
                matrix[i][j] = 101
                i += 1

            j -= 1
            i -= 1
            while j > -1 and matrix[i][j] != 101:
                ans.append(matrix[i][j])
                matrix[i][j] = 101
                j -= 1

            j += 1
            i -= 1
            while i > -1 and matrix[i][j] != 101:
                ans.append(matrix[i][j])
                matrix[i][j] = 101
                i -= 1

            if i == j and i + 1 < m and j + 1 < n and matrix[i + 1][j + 1] != 101:
                i += 1
                j += 1

            m -= 1
            n -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        matrix = list(eval(input()))
        print(s.spiralOrder(matrix))

'''
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
[[1,2,3,4,5], [6,7,8,9,10], [10,11,12, 13, 14]]
[[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]
[[3],[2]]
[[3,2]]
'''
