from typing import List


class UF:
    def __init__(self):
        self.parent = list(range(10001))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1, x2):
        self.parent[self.find(x1)] = self.find(x2)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        weights = []

        for i in range(m):
            for j in range(n):
                index = i * n + j
                if j < n - 1:  # 计算下边的
                    weights.append((abs(heights[i][j] - heights[i][j + 1]), index, index + 1))

                if i < m - 1:  # 计算右边的
                    weights.append((abs(heights[i][j] - heights[i + 1][j]), index, index + n))

        weights.sort()
        uf = UF()
        for weight in weights:
            uf.union(weight[1], weight[2])
            if uf.find(0) == uf.find(n * m - 1):
                return weight[0]
        return 0


if __name__ == '__main__':
    s = Solution()
    heights0 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    heights1 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    heights2 = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    heights3 = [[3]]
    for i in range(4):
        heights = eval(f'heights{i}')
        print(s.minimumEffortPath(heights))
