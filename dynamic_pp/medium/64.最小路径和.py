#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
from typing import List
from copy import deepcopy

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = deepcopy(grid)

        for i in range(m):
            for j in range(n):
                if not i and not j:
                    continue
                elif not i:
                    dp[i][j] += dp[i][j-1]
                elif not j:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
                
# @lc code=end


if __name__ == '__main__':
    grid = [[1,2,3],[4,5,6]]
    # grid = [[1,3,1],[1,5,1],[4,2,1]]
    grid = [[1,2],[1,1]]

    s = Solution()
    print(s.minPathSum(grid))