'''
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
'''
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        totalTime = len(customers)
        left = 0
        satisfy = extra = tmp = 0
        for right in range(totalTime):
            satisfy += (1 - grumpy[right]) * customers[right]
            tmp += grumpy[right] * customers[right]
            extra = max(tmp, extra)
            if right - left == X - 1:
                tmp -= grumpy[left] * customers[left]
                left += 1
        return satisfy + extra

    def maxSatisfiedx(self, customers: List[int], grumpy: List[int], X: int) -> int:
        totalTime = len(customers)
        left = right = 0
        satisfy = 0
        ans = float('-inf')
        dp = []
        for i in range(totalTime):
            satisfy += customers[i] * (1 - grumpy[i])
            dp.append(satisfy)

        satisfy = 0
        while right < totalTime:
            satisfy += customers[right]
            maxValue = satisfy
            if right - left == X - 1:
                if right < totalTime:
                    maxValue += dp[-1] - dp[right]
                if left > 0:
                    maxValue += dp[left - 1]
                satisfy -= customers[left]
                left += 1
            ans = max(ans, maxValue)
            right += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        customers = list(map(int, input().split(',')))
        grumpy = list(map(int, input().split(',')))
        X = int(input())
        print(s.maxSatisfied(customers, grumpy, X))

'''
1,0,1,2,1,1,7,5
0,1,0,1,0,1,0,1
3
1,0,1,2,1,1,7,5
1,1,1,1,1,1,1,1
3
1,0,1,2,1,1,7,5
0,0,0,0,0,0,0,0
3
'''
