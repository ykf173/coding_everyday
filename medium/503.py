'''
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:
输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。
'''
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        单调栈，记录最大值所在位置
        :param nums:
        :return:
        '''
        size = len(nums)
        ans = [-1] * size
        stack = []
        for i in range(2 * size - 1):
            while stack and nums[stack[-1]] < nums[i % size]:
                ans[stack.pop()] = nums[i % size]
            stack.append(i % size)
        return ans

    def nextGreaterElementsx(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        ans = []
        size = len(nums)
        maxValue = max(nums)
        # sortNums = list(set(sorted(nums)))
        for i in range(size):
            if nums[i] == maxValue:
                ans.append(-1)
                continue
            nums2 = nums[i:] + nums[:i]
            for num in nums2:
                if num > nums[i]:
                    ans.append(num)
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(eval(input()))
        print(s.nextGreaterElements(nums))

'''
[1,2,1]
[2,3,4,5,6,76,7,7,7,8]
[3,2,4,6,6,76,8,7,7,8]
'''
