#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List

class Solution:
    def direct(self, nums):
        zeros_num = 0
        i = 0

        while i < len(nums):
            if not nums[i]:
                zeros_num += 1
                del nums[i]
            else:
                i += 1
        nums += [0] * zeros_num

    def two_pointer(self, nums):
        """
        【非零】left【零】right
        """
        n = len(nums)
        left = right = 0

        while right < n:
            if nums[right] and not nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left]:
                left += 1
            right += 1


    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.direct(nums)
        self.two_pointer(nums)

# @lc code=end

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    # nums = [1,0,1,0,3,12,0]

    s = Solution()
    s.moveZeroes(nums)
    print(nums)
