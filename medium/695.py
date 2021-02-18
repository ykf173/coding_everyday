from typing import List


class Solution:

    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        '''
        使用栈，非递归
        :param grid:
        :return:
        '''
        visited = set()
        stack = []
        row_num, col_num = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        max_area = 0

        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j]:
                    stack.append((i, j))
                    area = 0
                    while stack:
                        cur_i, cur_j = stack.pop()
                        if cur_i < 0 or cur_j < 0 or cur_i >= row_num or cur_j >= col_num or (
                                cur_i, cur_j) in visited or not grid[cur_i][cur_j]:
                            continue
                        visited.add((cur_i, cur_j))

                        area += 1

                        for a, b in directions:
                            next_i, next_j = cur_i + a, cur_j + b
                            stack.append((next_i, next_j))
                    max_area = max(max_area, area)

        return max_area

    def dfs(self, visited, grid, i, j):
        area = 0
        row_num, col_num = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        if i < 0 or j < 0 or i >= row_num or j >= col_num or (i, j) in visited or not grid[i][j]:
            return 0

        visited.add((i, j))
        area += 1
        for a, b in directions:
            next_i, next_j = i + a, j + b
            area += self.dfs(visited, grid, next_i, next_j)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        使用递归
        :param grid:
        :return:
        '''

        row_num, col_num = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j]:
                    max_area = max(self.dfs(visited, grid, i, j), max_area)

        return max_area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    # grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    # grid = [[1, 1, 1, 1]]
    s = Solution()
    print(s.maxAreaOfIsland(grid))
