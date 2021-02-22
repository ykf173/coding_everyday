'''
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
'''
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        思想：先比较对角线+上三角，再比较下三角O(M*N*2)
        :param matrix:
        :return:
        '''
        row, column = len(matrix), len(matrix[0])
        if row == 1 or column == 1:
            return True
        for j in range(column):
            curI, curJ = 0, j
            curValue = matrix[curI][curJ]
            while curI < row:
                curI, curJ = curI + 1, curJ + 1
                if curI >= row or curJ >= column:
                    break
                if matrix[curI][curJ] != curValue:
                    return False

        for i in range(1, row):
            curI, curJ = i, 0
            curValue = matrix[curI][curJ]
            while curJ < column:
                curI, curJ = curI + 1, curJ + 1
                if curI >= row or curJ >= column:
                    break
                if matrix[curI][curJ] != curValue:
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    while 1:
        matrix = []
        n = int(input())
        for _ in range(n):
            matrix.append(list(map(int, input().split(','))))

        print(s.isToeplitzMatrix(matrix))

'''
3
1,2,3,4
5,1,2,3
9,5,1,2
2
1,2
2,2
3
1,2,3,4
5,1,2,3
9,5,1,3
1
1
1
1,2,3,4,5
5
1
2
3
4
5
2
11,74,0,93
40,11,74,7
3
36,59,71,15,26,82,87
56,36,59,71,15,26,82
15,0,36,59,71,15,26
'''
