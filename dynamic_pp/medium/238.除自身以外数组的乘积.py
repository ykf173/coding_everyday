#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        # left_mul, right_mul = [1] * n, [1] * n
        # left_pre, right_pre = 1, 1
        # left_post, right_post = 1, 1

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in range(n-1, -1, -1):
            res[i], right = res[i] * right, right * nums[i]
        
        return res


        
# @lc code=end

if __name__ == '__main__':
    nums = [1,2,3,4]
    nums = [0,1]
    nums = [1,0]
    nums = [1,1]


    nums = [-1,1,0,-3,3]

    s = Solution()

    print(s.productExceptSelf(nums))