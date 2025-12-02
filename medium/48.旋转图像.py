#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
from typing import List
import copy

class Solution:
    def new_matrix_method(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        new_matrix = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                new_matrix[j][n - i - 1] = matrix[i][j]
        # print(new_matrix)
        matrix[:] = new_matrix


    def inplace_method(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

        print(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # self.new_matrix_method(matrix)
        self.inplace_method(matrix)



            
# @lc code=end

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    s.rotate(matrix)

    # s.rotate(matrix)
    print(matrix)