#
# @lc app=leetcode.cn id=688 lang=python3
#
# [688] 骑士在棋盘上的概率
#

# @lc code=start
class Solution:
    def bfs(self, n: int, k: int, row: int, column: int) -> float:
        x = {-1, 1, 2, -2}
        y = {2, -2, -1, 1}

        if k == 0:
            return 1
        if n == 1:
            return 0
        
        total = 8 ** k // 2
        visited_count = 0
        
        i, j = row, column
        quen = [(i, j)]
        visited = [[0] * n for _ in range(n)]
        visited[i][j] = 1
        while quen or k >= 0:
            i, j = quen.pop()
            k -= 1

            for i_x in x:
                for j_y in y:
                    if abs(i_x) != abs(j_y) and 0 <= i + i_x < n and 0 <= j + j_y < n and not visited[i + i_x][j + j_y]:
                        tmp_i, tmp_j = i + i_x, j + j_y
                        quen.insert(0, (tmp_i, tmp_j))
                        visited[tmp_i][tmp_j] = 1
                        if not k and visited[tmp_i][tmp_j]:
                            visited_count += 1

        
        # visited_count = sum(sum(_) for _ in visited) // k

        return visited_count / total if visited_count else 0

                    
    def dfs(self, n: int, k: int, row: int, column: int) -> float: # 超时
        x = [-1, 1, 2, -2, -1, 1, -2, 2]
        y = [2, -2, -1, 1, -2, 2, -1, 1]

        if k == 0:
            return 1
        if n == 1:
            return 0
        
        total = 8 ** k // 2
        visited_count = 0
        
        i, j = row, column
        quen = [(i, j)]
        visited = [[0] * n for _ in range(n)]
        # visited[i][j] = 1
        while quen or k >= 0:
            visited[i][j] = 1
            k_tmp = k 
            while k_tmp and 0 <= i < n and 0 <= j < n and not visited[i][j]:
                for i_x, j_y in zip(x, y):
                    if k_tmp and 0 <= i + i_x < n and 0 <= j + j_y < n and not visited[i+i_x][j+j_y]:
                        tmp_i, tmp_j = i + i_x, j + j_y
                        i, j = tmp_i, tmp_j
                        quen.append((tmp_i, tmp_j))
                        visited[tmp_i][tmp_j] = 1
                        k_tmp -= 1
                        break
                if not k_tmp:
                    visited_count += 1
                    if quen:
                        quen.pop()
                if quen:
                    i, j = quen.pop()

        return visited_count / total if visited_count else 0

    def dynamic_programing(self, n: int, k: int, row: int, column: int) -> float:
        """
        状态转移方程：dp[step][i][j] = 1/8 * sum(dp[step-1][i+di][j+dj])
        当前概率为上一步在棋盘上，再走一步还在棋盘上的概率
        """


        dp = [[[0] * n for i in range(n)] for _ in range(k+1)]

        pos = [(-1,-2), (-1, 2), (-2, -1), (-2, 1), (1, 2), (1, -2), (2, -1), (2, 1)]
        
        for p in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if not p:
                        dp[p][i][j] = 1
                        continue
                    for x_i, y_j in pos:
                        x_tmp, y_tmp = i + x_i, j + y_j
                        if 0 <= x_tmp < n and 0 <= y_tmp < n:
                            dp[p][i][j] += dp[p - 1][x_tmp][y_tmp] / 8
        return dp[p][row][column]


    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # return self.bfs(n, k, row, column)
        # return self.dfs(n, k, row, column)
        return self.dynamic_programing(n, k, row, column)
    

if __name__ == '__main__':
    s = Solution()

    n = 1
    k = 0
    row = 0
    column = 0
    n, k, row, column = 3, 2, 0, 0

    print(s.knightProbability(n, k, row, column))


        
# @lc code=end

