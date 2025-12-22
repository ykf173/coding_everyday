'''
Author: yankaifeng ykf_173@163.com
Date: 2023-11-21 19:32:10
LastEditors: yankaifeng ykf_173@163.com
LastEditTime: 2023-11-21 19:58:50
FilePath: \coding_everyday\常用模板\排序\qs.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import random


def qs(nums, left, right):
    if left <= right:
        low, high = left, right
        cur_num = nums[low]
        while low < high:
            while low < high and nums[high] >= cur_num:
                high -= 1
            if low < high:
                nums[low] = nums[high]
            while low < high and nums[low] <= cur_num:
                low += 1
            if low < high:
                nums[high] = nums[low]
        nums[low] = cur_num
        qs(nums, left, low - 1)
        qs(nums, low + 1, right)

if __name__ == "__main__":
    nums = [random.randint(1, 1000) for _ in range(200)]
    nums1 = nums[:]

    qs(nums, 0, len(nums)-1)
    print(nums1)
    print(100*'*')
    print(nums)

    print(set(nums1) == set(nums))
                