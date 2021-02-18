from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        可以通过转化思路，获取区间最小值，取代两头获取最大值的思想
        :param cardPoints:
        :param k:
        :return:
        '''
        cardsNums = len(cardPoints)
        left, right = 0, cardsNums - k
        sumValue = sum(cardPoints)
        minValue = sumValue
        curSum = sum(cardPoints[left:right])
        while right < cardsNums:
            minValue = min(minValue, curSum)
            curSum = curSum - cardPoints[left] + cardPoints[right]
            left, right = left + 1, right + 1
        return sumValue - min(minValue, curSum)

    def maxScoreX(self, cardPoints: List[int], k: int) -> int:
        '''
        此方法不可行，不能取到最大值
        :param cardPoints:
        :param k:
        :return:
        '''
        cardsNums = len(cardPoints) - 1
        left, right = 0, cardsNums
        maxValue = 0
        while k > 0 and right >= 0 and left <= cardsNums:
            k -= 1
            if cardPoints[left] > cardPoints[right]:
                maxValue = max(maxValue, cardPoints[left])
                left += 1
            else:
                maxValue = max(maxValue, cardPoints[right])
                right -= 1
        return maxValue


if __name__ == '__main__':
    s = Solution()
    while 1:
        cards = list(map(int, input().split(',')))
        k = int(input())
        print(s.maxScore(cards, k))

'''
1,2,3,4,5,6,1
3
2,2,2
2
9,7,7,9,7,7,9
7
1,1000,1
1
1,79,80,1,1,1,200,1
3
'''
