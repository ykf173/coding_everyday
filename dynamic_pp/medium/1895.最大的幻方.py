#
# @lc app=leetcode.cn id=1895 lang=python3
#
# [1895] 最大的幻方
#

# @lc code=start
from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def judge_hf(i, j, side):
            # 判断行
            total = pre_sum_row[i][j+side-1] - pre_sum_row[i][j-1]
            for ix in range(i+1, i+side):
                a = pre_sum_row[ix][j+side-1] - pre_sum_row[ix][j-1]
                if a != total:
                    return False

            # 判断列
            for jx in range(j, j+side):
                a = pre_sum_col[i+side-1][jx] - pre_sum_col[i-1][jx]
                if a != total:
                    return False
                
            # 判断正对角线
            a = sum(grid[i+x-1][j+x-1] for x in range(side))

            if a != total:
                return False

            # 判断负对角线
            return total == sum(grid[i+x-1][j+side-x-2] for x in range(side))
                

        m, n = len(grid), len(grid[0])
        ans = 1

        k = min(m, n)
        if k < 2:
            return ans
        
        pre_sum_row, pre_sum_col = [[0] * (n+1) for _ in range(m+1)], [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                pre_sum_row[i][j] = pre_sum_row[i][j-1] + grid[i-1][j-1]
                pre_sum_col[i][j] = pre_sum_col[i-1][j] + grid[i-1][j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                t = min(m-i+1, n-j+1)
                for side in range(t, 1, -1):
                    if judge_hf(i, j, side):
                        ans = max(ans, side)
                        break
        return ans

if __name__ == '__main__':        
    grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
    # grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]

    s = Solution()

    print(s.largestMagicSquare(grid))

# @lc code=end

