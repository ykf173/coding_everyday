#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
from typing import List
import random

class Solution:
    def quick_sort1(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        middles = [num for num in nums if num == nums[mid]]
        left = [num for num in nums if num < nums[mid]]
        right = [num for num in nums if num > nums[mid]]
        return self.quick_sort1(left) + middles + self.quick_sort1(right)
    
    def quick_sort2(self, nums: List[int]) -> List[int]:
        
        def position(nums, low, high):
            if low >= high:
                return
            
            pos = random.randint(low, high)
            nums[pos], nums[low] = nums[low], nums[pos]
            pivot = nums[low]

            left, right = low, high
            while left < right:
                while left < right and pivot <= nums[right]:
                    right -= 1
                while left < right and  pivot >= nums[left]:
                    left += 1
                if left < right:
                    nums[right], nums[left] = nums[left], nums[right]

            nums[low], nums[left] = nums[left], nums[low]

            position(nums, low, left - 1)
            position(nums, left + 1, high)

        position(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums: List[int]) -> List[int]:
        """
        merge_sort，归并排序

        分开，每次二分，分到没法分
        然后合起来，类似链表合并
        """
        def merge(nums1, nums2):
            n1, n2 = len(nums1), len(nums2)
            ans = []
            i = j = 0
            while i < n1 and j < n2:
                if nums1[i] <= nums2[j]:
                    ans.append(nums1[i])
                    i += 1
                else:
                    ans.append(nums2[j])
                    j += 1
                    
            ans.extend(nums1[i:])
            ans.extend(nums2[j:])
            return ans        
        
        n = len(nums)
        if n < 2:
            return nums        
        
        mid = n // 2
        nums1 = self.merge_sort(nums[:mid])
        nums2 = self.merge_sort(nums[mid:])

        return merge(nums1, nums2)

    
    def heap_sort(self, nums: List[int]) -> List[int]:
        def sift_root(i: int, n: int):
            while True:
                left = 2 * i + 1
                right = left + 1
                largest = i

                if left < n and nums[left] > nums[largest]:
                    largest = left
                if right < n and nums[right] > nums[largest]:
                    largest = right

                if largest == i:
                    break
                
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest                
        # 构建堆
        n = len(nums)
        for i in range(n//2-1, -1, -1): # 最后一个非叶节点
            sift_root(i, n)
        
        # 模拟排序，倒排，取堆顶
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            sift_root(0, i)
        

    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.quick_sort1(nums)
        # return self.quick_sort2(nums)
        # return self.merge_sort(nums) # 归并
        self.heap_sort(nums)
        return nums
    
    
# if __name__ == '__main__':
#     nums = [[83,3,4,6,7,8,1,2,3,4,5,6,7,7,8,89,0]]
#     s = Solution()

#     for num in nums:
#         # print(s.quick_sort1(num))
#         # print(s.quick_sort2(num))
#         print(s.merge_sort(num))


# @lc code=end

