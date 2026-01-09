#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

# @lc code=start

from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        l = max(nums) + 1
        values = [0] * l


        for i in range(n):
            values[nums[i]] += nums[i]
        
        # max_val = values[1]
        for i in range(2, l):
            values[i] = max(values[i-1], values[i-2]+values[i])
            # max_val = max(max_val, values[i])
        return values[-1]#max_val


if __name__ == '__main__':       
    nums = [3,4,2]
    nums = [2,2,3,3,3,4]
    # nums = [8,10,4,9,1,3,5,9,4,10]


    s = Solution()
    print(s.deleteAndEarn(nums))

# @lc code=end

