from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        ans = []
        size = len(nums)
        left = 0
        sortedList = SortedList()

        for right in range(size):
            sortedList.add(nums[right])
            if right - left == k - 1:
                ans.append(sortedList[-1])
                sortedList.remove(nums[left])
                left += 1
        return ans

    def maxSlidingWindowx(self, nums: List[int], k: int) -> List[int]:
        '''
        O(N*k)
        :param nums:
        :param k:
        :return:
        '''
        if not nums:
            return []
        ans = []
        size = len(nums)
        left = 0
        for right in range(k, size + 1):
            if right - left == k:
                ans.append(max(nums[left:right]))
                left += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        k = int(input())
        print(s.maxSlidingWindow(nums, k))

'''
1,3,-1,-3,5,3,6,7
3
1,3,-1,-3,5,3,6,7
1
1,1,1,1
2
'''
