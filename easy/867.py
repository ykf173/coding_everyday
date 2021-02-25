'''
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
'''
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rowNum = len(matrix)
        colNum = len(matrix[0])
        size = rowNum * colNum
        ans = []
        row = []
        for num in range(size):
            i, j = num // rowNum, num % rowNum
            row.append(matrix[j][i])

            if len(row) == rowNum:
                ans.append(row)
                row = []
        return ans

if __name__ == '__main__':
    s = Solution()
    while 1:
        matrix = list(eval(input()))
        print(s.transpose(matrix))

'''
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3],[4,5,6]]
'''
