'''
Author: yankaifeng ykf_173@163.com
Date: 2023-11-20 22:32:51
LastEditors: yankaifeng ykf_173@163.com
LastEditTime: 2023-11-20 23:03:55
FilePath: \coding_everyday\常用模板\排序\merge_sort.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def merge(nums):
    length = len(nums)
    if length <= 1:
        return nums
    mid = length // 2
    left, right = nums[:mid], nums[mid:]
    return merge_sort(merge(left), merge(right))


def merge_sort(nums1, nums2):
    res = []
    while nums1 and nums2:
        if nums1[0] < nums2[0]:
            res.append(nums1.pop(0))
        else:
            res.append(nums2.pop(0))
    
    res.extend(nums1)
    res.extend(nums2)

    return res


if __name__ == '__main__':
    numss = [
        [1,2,5,43,455,6,9,7,10, 0, 19, 0],
        [1,2,3,4,5,6,7,8, 10, 19],
        [1,1,1,1,1,1,1,1],
        [19,12,9,7,6,5,4,3, 1, 0],
    ]

    for nums in numss:
        print(nums)
        print(merge(nums))
        print(50*'-')
