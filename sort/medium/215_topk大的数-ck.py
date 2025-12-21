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

                if left < n and nums[left] < nums[largest]:
                    largest = left
                if right < n and nums[right] < nums[largest]:
                    largest = right

                if largest == i:
                    break
                i = largest
        
        n = len(nums)
        # 堆大小为n-k
        for i in range((n-k)//2+1, -1, -1):
            sift_root(i, n-k)
    
        # 调整堆
        for i in range(n-k-1, -1, -1):
            nums[i+k], nums[0] = nums[0], nums[i+k]
            sift_root(0, k)
        return nums[k]
        # pass

    def quickselect(self, nums, left, right, k):
        if left >= right:
            return nums[k]
        
        pos = random.randint(left, right)
        nums[left], nums[pos] = nums[pos], nums[left]
        pivot = nums[left]

        i, j = left, right
        while i < j and nums[j] >= pivot:
            j -= 1
        while j > i and nums[j] >= pivot:
            i += 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
        
        self.quickselect(nums, i + 1, pos - 1, k)
        self.quickselect(nums, pos + 1, j - 1, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # return self.quickselect(nums, 0, n - 1, n - k)
        return self.maxheaptop(nums, k)
    

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1,5,6,4]
    k = 2

    nums = [3,2,1,5,6,4]
    k = 2

    # nums = [3,2,3,1,2,4,5,5,6]
    # k = 4
    
    print(s.findKthLargest(nums, k))
    # print(s.maxheaptop(nums, k))

