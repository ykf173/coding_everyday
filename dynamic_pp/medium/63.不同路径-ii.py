#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List
class Solution:
    def dynamic_program(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    continue
                elif i+j == 0:
                    dp[i][j] = 1
                # elif i*j == 0:
                #     dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.dynamic_program(obstacleGrid)

        
    
if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    # obstacleGrid = [[0,1],[0,0]]
    # obstacleGrid = [[0,0],[0,1]]
    obstacleGrid = [[1,0]]
    obstacleGrid = [[1]]

    s = Solution()
    print(s.uniquePathsWithObstacles(obstacleGrid))
# @lc code=end

