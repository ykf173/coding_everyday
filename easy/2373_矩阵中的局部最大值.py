# 给你一个大小为 n x n 的整数矩阵 grid 。
# 
# 生成一个大小为 (n - 2) x (n - 2) 的整数矩阵  maxLocal ，并满足：
# 
# maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
# 换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。
# 
# 返回生成的矩阵。
from typing import List

import numpy as np

from scipy import signal


class Solution:
    def largestLocal1(self, grid: List[List[int]]) -> List[List[int]]:
        row_n, col_n = len(grid), len(grid[0])
        res = [[0] * (col_n - 2) for _ in range(row_n - 2)]
        for i in range(row_n - 2):
            for j in range(col_n - 2):
                res[i][j] = max([max(sub[j:j + 3]) for sub in grid[i:i + 3]])

        return res

    def largestLocal2(self, grid: List[List[int]]) -> List[List[int]]:
        arr = np.array(grid)
        row_n = len(grid)
        res = np.array([], dtype=int)
        for i in range(row_n - 2):
            for j in range(row_n - 2):
                res = np.append(res, np.max(arr[i:i + 3, j:j + 3]))
        res = res.reshape(row_n - 2, row_n - 2).tolist()
        return res

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # 定义卷积核
        row_n = len(grid)
        kernel = np.ones((3, 3))
        # # kernel[1, 1] = 1
        # kernel = -np.inf * np.ones_like(kernel) + kernel
        #
        # # 进行矩阵卷积
        # max_values = signal.convolve2d(grid, kernel, mode="valid")
        # 定义卷积核
        # 对原始矩阵进行边缘填充
        grid_padded = np.pad(grid, pad_width=1, mode="constant", constant_values=-np.inf)

        # 进行矩阵卷积
        max_values = signal.pool(grid_padded, kernel, mode="valid")
        max_values = max_values.reshape(row_n - 2, row_n - 2).tolist()
        return max_values


if __name__ == '__main__':
    grids = [[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]],
             [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]]

    s = Solution()

    for grid in grids:
        print(s.largestLocal(grid))
