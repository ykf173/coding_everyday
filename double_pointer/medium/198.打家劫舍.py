#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums[0:1] + [0] * (n - 1)
        if n >= 2:
            dp[1] = max(nums[0:2])
        for i in range(2, n):
            dp[i] = max(dp[i - 2]+nums[i], dp[i-1])
        return dp[-1]
# @lc code=end

if __name__ == '__main__':
    nums = [1,1]
    s = Solution()
    print(s.rob(nums))

