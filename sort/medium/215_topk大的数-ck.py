'''
215. 数组中的第K个最大元素
中等
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

常考题

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
 

提示：

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

from typing import List
import random

class Solution:

    def heaptop():
        pass

    def quickselect(self, nums, left, right, k):
        if left >= right:
            return nums[k]
        
        i, j = left, right
        pos = random.randint(left, right)

        while nums[j] > nums[pos] and i < j:
            j -= 1
        while nums[i] < nums[pos] and j > i:
            i += 1
        if i <= j:
            nums[i], nums[j] = nums[i], nums[j]
        
        self.quickselect(nums, i + 1, pos - 1, k)
        self.quickselect(nums, pos + 1, j - 1, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.quickselect(nums, 0, n - 1, n - k)
    

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1,5,6,4]
    k = 2

    # nums = [3,2,3,1,2,4,5,5,6]
    # k = 4
    
    print(s.findKthLargest(nums, k))
