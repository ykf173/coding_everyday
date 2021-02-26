'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''
import copy
from typing import List


class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        size = len(nums)
        for i in range(size):
            ansSize = len(ans)
            for j in range(ansSize):
                tmp = copy.deepcopy(ans[j])
                tmp.append(nums[i])
                ans.append(tmp)
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        size = len(nums)
        for mask in range(1 << size):
            t = []
            for i in range(size):
                if mask & (1 << i):
                    t.append(nums[i])
            ans.append(t)

        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(eval(input()))
        print(s.subsets(nums))

'''
[1,2,3]
[0]
'''
