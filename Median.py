import numpy as np
from typing import List

def nums_median(nums):
    len_nums = len(nums)
    if len_nums % 2 == 0:
        return float((nums[len_nums//2-1]+nums[len_nums//2])/2)
    else:
        return float(nums[len_nums//2])


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len(nums1)!=0 and len(nums2)!=0 and len_nums1 > len_nums2:
            nums1, nums2 = nums2, nums1
            len_nums1, len_nums2 = len_nums2, len_nums1

        if len_nums1 == 0:
            return nums_median(nums2)
        if len_nums2 == 0:
            return nums_median(nums1)

        if len_nums1 <= len_nums2:
            index_nums2 = 0
            for index, num1 in enumerate(nums1):
                new_len_nums2 = len(nums2)
                while nums2[index_nums2] < num1 and index_nums2 - new_len_nums2 + 1:
                    index_nums2 += 1

                if num1 <= nums2[index_nums2]:
                    nums2.insert(index_nums2, num1)
                    index_nums2 += 1

                elif nums2[index_nums2] > num1:
                    nums2.insert(index_nums2, num1)
                    if index_nums2 - len_nums2:
                        index_nums2 += 1

                elif num1 >= nums2[-1]:  # 特殊情况nums2比nums1所有小
                    for num in nums1[index:]:
                        nums2.append(num)
                    return nums_median(nums2)

        return nums_median(nums2)

if __name__ == '__main__':
    s = Solution()
    while 1:
        nums1 = list(map(int, input().split()))
        nums2 = list(map(int, input().split()))
        print(s.findMedianSortedArrays(nums1, nums2))
