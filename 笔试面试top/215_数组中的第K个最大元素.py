'''
Author: yankaifeng ykf_173@163.com
Date: 2023-03-24 00:54:27
LastEditors: yankaifeng ykf_173@163.com
LastEditTime: 2023-09-26 19:58:10
FilePath: \coding_everyday\笔试面试top\215_数组中的第K个最大元素.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums: List[int], k: int) -> int:
            cur = random.choice(nums)
            big, equal, small = [], [], []
            for num in nums:
                if num > cur:
                    big.append(num)
                elif num < cur:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                return quick_select(small, k + len(small) - len(nums))
            return cur



        return quick_select(nums, k)


if __name__ == '__main__':
    numss = [[4, 56, 6, 30, 7, 8, 5, 9, 20],
        [3,2,3,1,2,4,5,5,6],
        [3,2,1,5,6,4]]
    ks = [2, 4, 2]
    s = Solution()
    for nums, k in zip(numss, ks):
        print(nums, k)
        print(s.findKthLargest(nums, 2))
