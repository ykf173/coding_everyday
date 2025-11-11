#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from typing import List
import heapq
import random

# @lc code=start
class Solution:

    def build_heap(nums):
        n = len(nums)
        mid = int(n / 2)
        for i in range(n):
            


    def replace_heap(): 
        

    def heap_large(self, nums, k):
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]


    def quich_select(self, left, right, nums, k):
        if left >= right:
            return nums[k]
        
        i, j = left, right
        pos = random.randint(i, j)

        nums[pos], nums[left] = nums[left], nums[pos]
        pivot = nums[left]

        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1

            while i < j and nums[i] <= pivot:
                i += 1
            
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i], nums[left] = nums[left], nums[i]
    
        if i == k:
            return nums[k]
        
        elif i > k:
            return self.quich_select(left, i, nums, k)
        
        else:
            return self.quich_select(i + 1, right, nums, k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.heap_large(nums, k)
        n = len(nums)
        return self.quich_select(0, n - 1, nums, n - k)

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    s = Solution()
    print(s.findKthLargest(nums, k))
        
# @lc code=end

