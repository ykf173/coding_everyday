"""
215. 数组中的第K个最大元素
中等
相关标签
premium lock icon
相关企业
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
 

提示：

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import random
from typing import List
import heapq

class Solution:
    def heapq_select(self, nums, k):
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        n = len(nums)

        for i in range(k, n):
            if nums[i] < min_heap[0]:
                min_heap.heapreplace(nums[i])
                min_heap.heappop()
        return min_heap[0]

    def quick_select(self, nums, left, right, k):
        if left >= right:
            return nums[k]

        pos = random.randint(left, right)
        nums[pos], nums[left] = nums[left], nums[pos]
        pivot = nums[left]

        i, j = left, right

        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1

            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i], nums[left] = nums[left], nums[i]

        if i == k:
            return nums[k]
        if j > k:
            return self.quick_select(nums, left, j, k)
        if j < k:
            return self.quick_select(nums, j + 1, right, k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_k = self.quick_select(nums, 0, n-1, n - k)        
        return max_k
        

if __name__ == '__main__':
    nums = [3,4,5,6,8,9,2,4,6,1]
    k = 4
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4

    # nums = [3,2,1,5,6,4]
    # k = 2
    s = Solution()
    print(s.findKthLargest(nums, k))

    print(s.heapq_select(nums, k))