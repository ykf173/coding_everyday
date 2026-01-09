#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
from typing import List

class Solution:
    def baili(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    ans += n - j
                    break
        return ans
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def bisearch_right(nums, low, high):
            while low < high:
                mid = (low + high) // 2
                if nums[mid] >= 0:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        ans = 0
        for i in range(m):
            pos = bisearch_right(grid[i], 0, n - 1)
            ans += n - pos

            if grid[i][pos] >= 0:
                ans -= 1
        return ans


if __name__ == '__main__':
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    grid = [[3,2],[1,0]]
    s = Solution()
    print(s.countNegatives(grid))
# @lc code=end

