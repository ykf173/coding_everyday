from typing import List


class UF:
    def __init__(self):
        self.parent = list(range(2501))

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1: int, x2: int):
        self.parent[self.find(self.parent[x1])] = self.find(x2)


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        values = []
        n = len(grid)
        if n < 2:
            return -1

        for i in range(n):
            for j in range(n):
                pos = i * n + j
                if i < n - 1:
                    values.append((max(grid[i][j], grid[i + 1][j]), pos, pos + n))
                if j < n - 1:
                    values.append((max(grid[i][j], grid[i][j + 1]), pos, pos + 1))

        values.sort()

        uf = UF()
        for idx in range(len(values)):
            uf.union(values[idx][1], values[idx][2])
            if uf.find(0) == uf.find(n ** 2 - 1):
                return values[idx][0]


if __name__ == '__main__':
    s = Solution()
    grid0 = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    grid1 = [[0, 2], [1, 3]]
    grid2 = [[10, 12, 4, 6], [9, 11, 3, 5], [1, 7, 13, 8], [2, 0, 15, 14]]
    for i in range(3):
        print(s.swimInWater(eval(f'grid{i}')))

# import time
#
# s = time.perf_counter()
# grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6],
#         [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6],
#         [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6],
#         [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6], [10, 9, 8, 7, 6]]
# # grid = [weight for weights in grid for weight in weights]
# grid = sum(grid, [])
# print(time.perf_counter() - s)
# print(grid)
