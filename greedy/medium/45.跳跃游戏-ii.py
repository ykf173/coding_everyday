#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_step = 0
        ans = 0
        end = 0
        for i in range(n-1):
            max_step = max(max_step, i + nums[i])
            if i == end:
                if max_step == end: # 到不了 [2,0,0,0]
                    return -1
                ans += 1
                end = max_step
        return ans
            

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    nums = [
        [2,1],
        [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3],
        [0],
        [1],
        [1,1,2,1,1],
        [1,1,1,1],
        [0,1,2],
        [2,3,1,1,4],
        [2,3,0,1,4],
        [4,1,2,4,2]
    ]

    for i in range(len(nums)):
        print(s.jump(nums[i]))
