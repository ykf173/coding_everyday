#
# @lc app=leetcode.cn id=2943 lang=python3
#
# [2943] 最大化网格图中正方形空洞的面积
#

# @lc code=start
from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_continues_len(sides):
            if not sides:
                return 0
            
            sides.sort()

            n = len(sides)
            max_len = cur = 1
            for i in range(1, n):
                if sides[i] == sides[i-1] + 1:
                    cur += 1

                else:
                    max_len = max(max_len, cur)
                    cur = 1

            return max(max_len, cur)

        lh = get_continues_len(hBars) + 1
        lv = get_continues_len(vBars) + 1

        return min(lh, lv) ** 2
    
if __name__ == '__main__':
    m, n = 1, 1
    hBars, vBars = [2],[2]

    # m, n = 2, 1
    # hBars, vBars = [2,3], [2]

    s = Solution()
    print(s.maximizeSquareHoleArea(n, m, hBars, vBars))
# @lc code=end

