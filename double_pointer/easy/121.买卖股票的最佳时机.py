#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List
import copy
class Solution:
    def dp_method(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        min_values = copy.deepcopy(prices)

        for i in range(1, n):
            min_values[i] = min(min_values[i-1], prices[i])

        for i in range(n-1, 0, -1):
            ans = max(prices[i] - min_values[i], ans)
        
        return ans

    def maxProfit(self, prices: List[int]) -> int:
        return self.dp_method(prices)


# s = Solution()
# x = [5,6,6,7,1,2,3,4,5]

# print(s.maxProfit(x))

        
# @lc code=end

