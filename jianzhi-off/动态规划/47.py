'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，
并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
'''
import copy
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        rowNum, colNum = len(grid), len(grid[0])
        # dp = [[0] * colNum for _ in range(rowNum)]
        #
        # dp[0][0] = grid[0][0]
        for i in range(1, rowNum):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for i in range(1, colNum):
            grid[0][i] = grid[0][i - 1] + grid[0][i]

        for i in range(1, rowNum):
            for j in range(1, colNum):
                grid[i][j] = max(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]

        return grid[-1][-1]


if __name__ == '__main__':
    s = Solution()
    while 1:
        grid = list(eval(input()))
        print(s.maxValue(grid))

'''
[[1,3,1],[1,5,1],[4,2,1]]
'''
