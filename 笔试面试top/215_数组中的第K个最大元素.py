# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 
#  
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
#  
# 
# 提示：
# 
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104
import random
from typing import List


class Solution:
    def get_position(self, nums: List[int], left: int, right: int):
        low, high = random.randint(left, right), right
        cur = nums[low]
        while low < high:
            while low < high and nums[high] >= cur:
                high -= 1
            if low < high:
                nums[low] = nums[high]
            while low < high and nums[low] <= cur:
                low += 1
            if low < high:
                nums[low] = nums[high]

        nums[low] = cur

        return low

    def get_left(self, nums, left, right):
        cur_pos = random.randint(left, right)
        nums[cur_pos], nums[left] = nums[left], nums[cur_pos]
        return self.get_position(nums, left, right)

    def get_cur_k(self, nums, left, right, k):
        cur_pos = self.get_left(nums, left, right)
        # cur_pos = self.get_position(nums, left, right)
        if cur_pos == k - 1:
            return nums[cur_pos]
        elif cur_pos < k - 1:
            return self.get_cur_k(nums, cur_pos + 1, right, k)
        else:
            return self.get_cur_k(nums, 0, cur_pos - 1, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.get_cur_k(nums, 0, n - 1, n - k + 1)


if __name__ == '__main__':
    nums = [4, 56, 6, 30, 7, 8, 5, 9, 20]

    s = Solution()
    print(s.findKthLargest(nums, 2))
