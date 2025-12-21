#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
import copy
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cur_max = 0
        i = 0

        while i < n:
            cur_max = max(cur_max - 1, nums[i])
            next_step = i + cur_max

            if not nums[0]:
                return not n - 1
            if not cur_max:
                return False
            if next_step >= n - 1:
                return True
            i += 1

        return False
# @lc code=end


if __name__ == '__main__':
   nums = [
        [0,2,3],
        [0],
        [2,3,1,1,4],
        [3,2,1,0,4],
        [3,2,1,0,4,1,2,1,1,1,0,0,1],
        [3,4,2,0,2,0,2,1,1,1,0,0,1],
        [1,1,1,1,1],
        [1,1,1,1,1,0,1]
     ]
   
   s = Solution()
   for i in range(len(nums)):
       print(s.canJump(nums[i]))
