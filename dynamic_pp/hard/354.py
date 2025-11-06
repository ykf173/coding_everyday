'''
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式(w, h)出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
说明:
不允许旋转信封。

示例:
输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
'''
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        size = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # 为了解决第一个元素相同，第二元素可以组成子序列的情况,第一元素相同情况下，第二元素降序
        maxLength = [envelopes[0][1]]

        for i in range(1, size):
            if envelopes[i][1] > maxLength[-1]:
                maxLength.append(envelopes[i][1])
            elif envelopes[i][1] < maxLength[-1]:
                low, high, pos = 0, len(maxLength), -1
                while low <= high:
                    mid = (low + high) >> 1
                    if maxLength[mid] < envelopes[i][1]:
                        pos = mid
                        low = mid + 1
                    else:
                        high = mid - 1

                maxLength[pos + 1] = envelopes[i][1]

        return len(maxLength)

    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        size = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # 为了解决第一个元素相同，第二元素可以组成子序列的情况
        maxLength = [1] * size
        for i in range(1, size):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:  # 第一元素相同时，第二个元素降序排列，即前边的元素都比后边的大
                    maxLength[i] = max(maxLength[i], maxLength[j] + 1)
        return max(maxLength)

    def quickSorted(self, envelopes: List[List[int]], left, right):
        if left < right:
            low, high = left, right
            curEle = envelopes[low]
            while low < high:
                while low < high and curEle[0] <= envelopes[high][0] and curEle[1] <= envelopes[high][1]:
                    high -= 1
                if low < high:
                    envelopes[low] = envelopes[high]
                while low < high and curEle[0] >= envelopes[low][0] and curEle[1] >= envelopes[low][1]:
                    low += 1
                if low < high:
                    envelopes[high] = envelopes[low]
            envelopes[low] = curEle
            self.quickSorted(envelopes, left, low - 1)
            self.quickSorted(envelopes, low + 1, right)

    def maxEnvelopesX(self, envelopes: List[List[int]]) -> int:
        '''
        方法有问题，没找到原因
        :param envelopes:
        :return:
        '''
        n = len(envelopes)
        if not n:
            return 0
        self.quickSorted(envelopes, 0, n - 1)
        maxEnvelopes = [1] * n
        cuMaxValue = envelopes[0]
        for i in range(1, n):
            if envelopes[i][0] > cuMaxValue[0] and envelopes[i][1] > cuMaxValue[1]:
                maxEnvelopes[i] = maxEnvelopes[i - 1] + 1
                cuMaxValue = envelopes[i]
            else:
                maxEnvelopes[i] = maxEnvelopes[i - 1]

        return max(maxEnvelopes)


if __name__ == '__main__':
    s = Solution()
    while 1:
        evelopes = list(eval(input()))
        print(s.maxEnvelopes(evelopes))

'''
[[5,4],[6,4],[1,2],[2,3]]
[[5,5],[5,6],[1,2],[2,3]]
[[2,5],[5,6],[1,2],[2,3],[6,8]]
[[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
[[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]


[3,3,4,7,5]
'''
