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
    def maxheaptop(self, nums, k):
        '''
        大根堆，时间复杂度，最坏接近O(nlogn)
        
        :param nums: 说明
        :param k: 说明
        '''
        def sift_root(i, n):
            while True:
                largest = i
                left = 2 * i + 1
                right = left + 1

                if left < n and nums[left] > nums[largest]:
                    largest = left
                if right < n and nums[right] > nums[largest]:
                    largest = right

                if largest == i:
                    break
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest
        
        n = len(nums)
        # 堆大小为n-k
        for i in range(n//2+1, -1, -1):
            sift_root(i, n)
    
        # 调整堆
        for i in range(n-1, n-k-1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            sift_root(0, i)
        print(nums)
        return nums[n-k]
    
    def min_heap_top(self, nums, k):
        def sift_root(i, n):
            while True:
                smallest = i
                left = 2 * i + 1
                right = left + 1

                if left < n and nums[left] < nums[smallest]:
                    smallest = left
                if right < n and nums[right] < nums[smallest]:
                    smallest = right

                if smallest == i:
                    break
                nums[smallest], nums[i] = nums[i], nums[smallest]
                i = smallest

        n = len(nums)
        # k = n - k
        for i in range(k // 2 + 1, -1, -1):
            sift_root(i, n-k)

        for i in range(k, n):
            if nums[i] > nums[0]:
                nums[0], nums[i] = nums[i], nums[0]
                sift_root(0, k)

        return nums[0]

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
        # return self.quich_select(0, n - 1, nums, n - k)
        return s.maxheaptop(nums, k)

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    # nums = [1]
    # k = 1

    # nums = [3,2,3,1,2,4,5,5,6]
    # k = 4
    s = Solution()
    # print(s.findKthLargest(nums, k))

    # print(s.maxheaptop(nums, k))

    print(s.min_heap_top(nums, k))

        
# @lc code=end

