#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

# @lc code=start

from typing import List

class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)

        vals = [0] * n

        for i in range(len(nums)):
            vals[nums[i] - 1] += nums[i]

        before, current = vals[0], max(vals[:2])
        n = len(vals)
        for i in range(2, n):
            before, current = current, max(current, before + vals[i])
        
        return current

if __name__ == '__main__':       
    nums = [3,4,2]
    nums = [2,2,3,3,3,4]

    s = Solution()
    print(s.deleteAndEarn(nums))
# @lc code=end

