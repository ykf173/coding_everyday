#
# @lc app=leetcode.cn id=2975 lang=python3
#
# [2975] 移除栅栏得到的正方形田地的最大面积
#

# @lc code=start
from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def get_diff(fences, n):
            res = set()

            fences = sorted([1] + fences + [n])
            k = len(fences)
            for i in range(k):
                for j in range(i+1, k):
                    res.add(fences[j] - fences[i])

            return res
        
        max_val = 10 ** 9 + 7
        hf = get_diff(hFences, m)
        vf = get_diff(vFences, n)

        side = max(hf & vf, default=0)

        return (side ** 2) % max_val if side else -1


if __name__ == '__main__':
    m, n = 4, 3
    hFences, vFences = [2,3], [2]

    m, n = 6, 7
    hFences, vFences = [2], [4]

    s = Solution()   
    print(s.maximizeSquareArea(m, n, hFences, vFences))
# @lc code=end

