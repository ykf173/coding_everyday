#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        num_set = set(nums)

        for num in num_set:
            if num - 1 in num_set:
                continue

            y = num + 1
            while y in num_set:
                y += 1
            res = max(res, y - num)
            
        return res
        
# @lc code=end

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    # nums = [-1,1,0,1,2]
    # nums = []
    # nums = [0]


    s = Solution()
    print(s.longestConsecutive(nums))