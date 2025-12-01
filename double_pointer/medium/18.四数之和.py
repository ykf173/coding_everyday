#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from random import randint
from typing import List
from collections import defaultdict


class Solution:
    def quick_sort_v0(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        left_nums = [num for num in nums[1:] if num <= pivot]
        right_nums = [num for num in nums[1:] if num > pivot]

        return self.quick_sort_v0(left_nums) + [pivot] + self.quick_sort_v0(right_nums)
    
    def quick_sort(self, nums, low, high):
        def position(nums, low, high):
            pos = randint(low, high)
            nums[low], nums[pos] = nums[pos], nums[low]
            tmp = nums[low]
            left, right = low, high

            while left < right:
                while nums[right] >= tmp and left < right:
                    right -= 1
                while nums[left] <= tmp and left < right:
                    left += 1
                if left < right:
                    nums[right], nums[left] = nums[left], nums[right]
            
            nums[low], nums[left] = nums[left], nums[low]
            return left
        
        if low < high:
            pos = position(nums, low, high)
            self.quick_sort(nums, low, pos-1)
            self.quick_sort(nums, pos+1, high)


    def method_memory(self, nums: List[int], target: int) -> List[List[int]]:
        """ 最坏情况，n^4，现有方案只是通过加了裁剪，解决该问题"""
        n = len(nums)
        self.quick_sort(nums, 0, n-1)
        res = set()
        sums = defaultdict(set)
        max_val, min_val = sum(nums[-2:]), sum(nums[:2])

        for i in range(n):
            for j in range(i+1, n):
                s = target - nums[i] - nums[j]
                if s < min_val:
                    continue
                if s > max_val:
                    break
                # if target // 4 == nums[i] and nums[i] == nums[j] and not flag:
                #     flag = True
                #     continue
                sums[s].add((nums[i], nums[j], i, j))

        for i in range(n):
            for j in range(i+1, n):
                cur_sum = nums[i] + nums[j]

                if cur_sum < min_val:
                    continue
                if cur_sum > max_val:
                    break

                flag = False
                for cur in sums.get(cur_sum,[]):
                    # cur_l = list(cur) + [nums[i], nums[j]]
                    # if len(cur_l) == len(set(cur_l)):
                    if flag:
                        break

                    if target // 4 == nums[i] and (nums[i] == nums[j] == cur[0] or nums[i] == nums[j] == cur[1]) and not flag:
                        flag = True

                    if cur[2] != i and cur[3] != i and cur[2] != j and cur[3] != j:
                        four_nums = (cur[0], cur[1], nums[i], nums[j]) #tuple(sorted(list(cur[:2]) + [nums[i], nums[j]]))
                        res.add(four_nums)
        result = set()
        for nu in res:
            result.add(tuple(sorted(nu)))
                        
        return [list(nu) for nu in result]


    def method_two_pointer(self, nums: List[int], target: int) -> List[List[int]]:
        """排序+双指针，n^3"""
        n = len(nums)
        self.quick_sort(nums, 0, n-1)

        res = []

        max_val, min_val = sum(nums[-4:]), sum(nums[:4])
        if n < 4 and target > max_val or target < min_val:
            return res
        
        for i in range(n):
            for j in range(i+1, n):
                l, r = 0, n - 1
                while l < r:
                    if j == r or j == l:
                        r -= 1
                        continue

                    if i == l or i == r:
                        l += 1
                        continue  

                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        res.append([nums[l], nums[i], nums[j], nums[r]])
                        l, r = l + 1, r - 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        res = set([tuple(sorted(nums)) for nums in res])

        return [list(nums) for nums in res]


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # return self.two_pointer(nums, target)
        # return self.method_memory(nums, target)
        return self.method_two_pointer(nums, target)

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0

    nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2] 
    target = 8
    print(s.fourSum(nums, target))
    # print(s.two_pointer(nums))
    # s.quick_sort(nums, 0, len(nums) - 1)
    # print(nums)
    # print(s.quick_sort_v0(nums))
    # print(randint(0, 10))
