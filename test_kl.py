'''
Author: yankaifeng ykf_173@163.com
Date: 2024-01-03 19:48:16
LastEditors: yankaifeng ykf_173@163.com
LastEditTime: 2024-01-03 20:03:29
FilePath: \coding_everyday\test_kl.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

# [1,2,10,11,6,25,1,-1,-1,-2,3,3,7,12] 返回最大的N个值 ，比如top2=12,25

def quick_sort(nums, left, right):
    while low < high:
        low, high = left, right
        tmp = nums[low]
        while nums[high] >= tmp and low < high:
            high -= 1
        if low < high:
            nums[low] = nums[high]
        
        while nums[low] <= tmp and low < high:
            low += 1
        if low < high:
            nums[high] = nums[low]
        
        nums[low] = tmp
    
    quick_sort(nums, low + 1, high)        

def get_topk(nums, topk):
    quick_sort(nums, 0, len(nums) - 1)
    return nums[-topk:]


if __name__ == '__main__':
    nums = [1,2,10,11,6,25,1,-1,-1,-2,3,3,7,12]

    print(get_topk(nums, 2))