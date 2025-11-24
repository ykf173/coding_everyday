#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    # def dfs(m,n):
    #     s = (0, 0)
    #     visited = [[0] * n for _ in range(m)] 
    #     ori = [(0,1), (1, 0)]
    #     stack = []
    #     for i in range(m):
    #         for j in range(n):

    def dynamic_pro(self, m, n):
        dp = [[0] * n for _ in range(m)] 
        for i in range(1, m):
            for j in range(1, n):
                if not i or not j:
                    dp[i][j] = 1
                else:
                    dp[i][j] =  dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
                
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dynamic_pro(m, n)


        
# @lc code=end

if __name__ == '__main__':
    m, n = 3, 7
    m, n = 3, 2
    m, n = 7, 3
    m, n = 3, 3
    # m, n = 1, 1
    # m, n = 2, 1
    # m, n = 1, 2
    # m, n = 2, 2



    s = Solution()
    print(s.dynamic_pro(m, n))
