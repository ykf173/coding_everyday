#
# @lc app=leetcode.cn id=688 lang=python3
#
# [688] 骑士在棋盘上的概率
#

# @lc code=start
class Solution:
    def bfs(self, n, k, row, column):
        dp = [[0] * n for _ in range(n)]
        orin_x, ori_y = {-2, -1, 1, 2}, {-1, -2, 1, 2}

        que = []
        while row < n and column < n and k > 0:
            if 


    def get_prob(self, count, total):
        return count / total if count else 0

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        
# @lc code=end

