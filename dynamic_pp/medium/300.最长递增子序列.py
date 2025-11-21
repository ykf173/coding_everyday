#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
from typing import List

class Solution:
    def get_LIS(self, n, nums, dp, max_len):

        res = []
        i = n - 1
        while i > -1 and max_len:
            if max_len == dp[i]:
                res.append(nums[i])
                max_len -= 1
            i -= 1      

        return res[::-1]          

                
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            dp[i] = 1
            for j in range(i+1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_len = max(dp)
        # res = self.get_LIS(n, nums, dp, max_len)
        # print(f'其中一个最长递增子序列为：', res)
        return max_len

        
# @lc code=end

if __name__ == '__main__':
    s = Solution()


    nums = [10,9,2,5,3,7,101,18]
    # nums = [3,2,1]

    print(s.lengthOfLIS(nums))


