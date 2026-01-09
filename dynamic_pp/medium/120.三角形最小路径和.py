#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[0] + [float('inf')] * (n - 1)
        last_dp = triangle[0] + [float('inf')] * (n - 1)
        # cur_min = dp

        for i in range(1, n):
            for j in range(i+1):
                dp[j] = min(dp[j] + triangle[i][j], last_dp[j-1] + triangle[i][j])
            last_dp = dp[:]
        return min(dp)

if __name__ == '__main__':
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # triangle = [[-10]]
    triangle = [[-1],[2,3],[1,-1,-3]]


    s = Solution()
    print(s.minimumTotal(triangle))
# @lc code=end

