#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        ans = 0
        if n > m:
            return ans
        
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i + j == 0 or j == 0:
                    dp[i][j] = 1

                elif i == 0:
                    dp[i][j] = 0

                else:
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]

        return dp[m][n]
    


                    
                

        
# @lc code=end

if __name__ == '__main__':
    s = "rabbbit"; t = "rabbit" #3

    ss = Solution()
    print(ss.numDistinct(s, t))