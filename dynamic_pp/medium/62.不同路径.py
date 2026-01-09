#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i*j == 0:
                    dp[i][j] = 1
                
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    m = 3; n = 7 #输出：28
    # m = 3; n = 3 #输出：6
    # m = 3; n = 2 #输出：6
    # m = 1; n = 2
    # m = 2; n = 1

    m = 1; n = 1

    s = Solution()
    print(s.uniquePaths(m, n))


# @lc code=end

