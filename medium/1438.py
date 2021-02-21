'''
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
如果不存在满足条件的子数组，则返回 0 。
'''
from typing import List

from sortedcontainers import SortedList


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        size = len(nums)
        left = right = 0
        ans = 0
        curList = SortedList()
        while right < size:
            curList.add(nums[right])
            if curList[-1] - curList[0] > limit:
                curList.remove(nums[left])
                left += 1
            ans = max(ans, len(curList))
            right += 1
        return ans

    ans = 0

    def updateAns(self, nums: List[int], limit: int):
        size = len(nums)
        flag = True
        for i in range(0, size):
            for j in range(i + 1, size):
                if abs(nums[i] - nums[j]) > limit:
                    self.ans = max(self.ans, j, size - j - 1)
                    flag = False
                    break
        if flag:
            self.ans = max(self.ans, size)

    def longestSubarrayx(self, nums: List[int], limit: int) -> int:
        '''
        不通过，思想有问题，O(N^3)
        :param nums:
        :param limit:
        :return:
        '''
        size = len(nums)
        left = right = 0
        flag = True
        while right < size:
            if abs(nums[left] - nums[right]) > limit:
                flag = False
                self.updateAns(nums[left: right + 1], limit)
                left += 1
            right += 1

        curPos = left
        while abs(nums[left] - nums[curPos]) > limit and not flag:
            curPos += 1
        left = curPos

        if right - left + 1 > self.ans:
            self.updateAns(nums[left: right], limit)

        return max(self.ans, right - left) if flag else self.ans


if __name__ == '__main__':
    while 1:
        s = Solution()
        cards = list(map(int, input().split(',')))
        k = int(input())
        print(f'{k}', s.longestSubarray(cards, k))

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
10,1,2,4,7,2
5
4,2,2,2,4,4,2,2
0
8,2,4,7
4
1,5,6,7,8,10,6,5,6
4
2,2,2,4,4,2,5,5,5,5,5,2
2

ans:[4,3,7,1,3,4,3,2,5,6]
'''
