# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
# 
# 如果符合下列情况之一，则数组 A 就是 锯齿数组：
# 
# 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
# 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 返回将数组 nums 转换为锯齿数组所需的最小操作次数。
# 
#  
# 
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。
#
# 示例 2：
# 输入：nums = [9,6,1,6,2]
# 输出：4
#  
# 
# 提示：
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        odd_op = 0
        even_op = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if i % 2 == 0:
                d1 = nums[i] - nums[i - 1] + 1 if i and nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < len_nums - 1 and nums[i] >= nums[i + 1] else 0
                even_op += max(d1, d2)
            else:
                d1 = nums[i] - nums[i - 1] + 1 if nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < len_nums - 1 and nums[i] >= nums[i + 1] else 0
                odd_op += max(d1, d2)

        return min(even_op, odd_op)


if __name__ == '__main__':
    s = Solution()
    nums = [
        [9, 6, 1, 6, 2],
        [1, 2, 3],
        [1, 2, 1],
        [7, 4, 8, 9, 7, 7, 5],
        [2, 7, 10, 9, 8, 9]
    ]

    for numbers in nums:
        print(s.movesToMakeZigzag(numbers))