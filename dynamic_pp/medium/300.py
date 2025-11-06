'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        maxLenList = [0, nums[0]]  # dp[i]代表前i个元素的最小子序列中最小的元素
        for i in range(size):
            if nums[i] > maxLenList[-1]:
                maxLenList.append(nums[i])
            elif nums[i] < maxLenList[-1]:  # 二分查找，第一个小于dp[i]的元素
                low, high, pos = 1, len(maxLenList) - 1, 0  # pos位置没找到的话，就是最小的
                while low <= high:
                    mid = (low + high) // 2
                    if maxLenList[mid] < nums[i]:
                        pos = mid
                        low = mid + 1
                    else:  # 只找小于的第一个，等于时会替换
                        high = mid - 1
                maxLenList[pos + 1] = nums[i]

        return len(maxLenList) - 1

    def lengthOfLISX(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(eval(input()))
        print(s.lengthOfLIS(nums))

'''
[10,9,2,5,3,7,101,18]
[0,1,0,3,2,3]
[7,7,7,7,7,7,7]

'''
