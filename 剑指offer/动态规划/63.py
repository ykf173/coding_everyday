'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        profit, curMin = 0, float('inf')
        for i in range(size):
            curMin = min(curMin, prices[i])
            profit = max(profit, prices[i] - curMin)

        return profit

    def maxProfitX(self, prices: List[int]) -> int:
        size = len(prices)
        dp = [0] * size
        if not size:
            return 0

        curMin = prices[0]
        for i in range(1, size):
            if curMin > prices[i]:
                curMin = prices[i]

            dp[i] = prices[i] - curMin
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(eval(input()))
        print(s.maxProfit(nums))
'''
[7,1,5,3,6,4]
[7,6,4,3,1]
[7,1,1,10,6,4]

ans； 【5, 0, 10】
'''
