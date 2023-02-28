# 给你一个非负整数数组 nums 。在一步操作中，你必须：
# 
# 选出一个正整数 x ，x 需要小于或等于 nums 中 最小 的 非零 元素。
# nums 中的每个正整数都减去 x。
# 返回使 nums 中所有元素都等于 0 需要的 最少 操作数。
#
# 
# 示例 1：
# 输入：nums = [1,5,0,3,5]
# 输出：3
# 解释：
# 第一步操作：选出 x = 1 ，之后 nums = [0,4,0,2,4] 。
# 第二步操作：选出 x = 2 ，之后 nums = [0,2,0,0,2] 。
# 第三步操作：选出 x = 2 ，之后 nums = [0,0,0,0,0] 。
# 示例 2：
# 输入：nums = [0]
# 输出：0
# 解释：nums 中的每个元素都已经是 0 ，所以不需要执行任何操作。
#
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
import copy
from typing import List


class Solution:
    def minimumOperations1(self, nums: List[int]) -> int:
        min_vals = copy.deepcopy(nums)
        min_vals.sort()
        while not all(min_vals):
            min_vals.remove(0)

        n = len(nums)
        res = 0
        while sum(nums):
            for i in range(n):
                if nums[i]:
                    nums[i] -= min_vals[0]
            min_vals = [min_val - min_vals[0] for min_val in min_vals]
            while not all(min_vals):
                min_vals.remove(0)
            res += 1
        return res

    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})



if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 0, 3, 5]
    # nums = [0, 0, 0, 0]
    # nums = [0]
    # nums = [1, 1, 1, 2, 2, 2, 3, 3]
    print(s.minimumOperations(nums))
