from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        min_price = 10 ** 5 + 1
        for price in prices:
            max_pro = max(price - min_price, max_pro)
            min_price = min(price, min_price)

        return max_pro

    def median_maxProfit(self, prices: List[int]) -> int:
        len_price = len(prices)
        max_pro = 0
        if len_price < 2:
            return max_pro
        for i in range(1, len_price):
            max_val = max(prices[i:])
            min_val = min(prices[:i])
            pro = max_val - min_val
            if max_pro < pro:
                max_pro = pro
        return max_pro

    def easy_maxProfit(self, prices: List[int]) -> int:
        len_price = len(prices)
        max_pro = 0
        for i in range(len_price):
            for j in range(i, len_price):
                pro = prices[j] - prices[i]
                if pro > max_pro:
                    max_pro = pro
        return max_pro


if __name__ == '__main__':
    s = Solution()
    while 1:
        x = list(map(int, input().split()))
        print(s.maxProfit(x))

'''
7 1 5 3 6 4
'''
