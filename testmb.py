'''
Author: yankaifeng ykf_173@163.com
Date: 2023-11-28 18:57:41
LastEditors: yankaifeng ykf_173@163.com
LastEditTime: 2023-11-28 19:59:51
FilePath: \coding_everyday\testmb.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
有一个有序数组，需要删除重复出现的元素，定义出现次数超过两次的元素为重复出现的元素，要求返回删除之后的数组的新长度。
不要使用额外的数组空间，在 原地 修改输入数组，并在使用 O(1) 额外空间的条件下完成。
1. 输入：nums = [1,1,1,2,2,3]
   输出：5, nums = [1,1,2,2,3]
   解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

2. 输入：nums = [0,0,1,1,1,1,2,3,3]
   输出：7, nums = [0,0,1,1,2,3,3]
   解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。
"""

def del_rep(nums):
    length = len(nums)
    cur_len = 1
    if length < 3:
        return length, nums
    # if nums[0] == nums[1] :
    #     cur_len = 2
    for i in range(1, length):
        if nums[i - 1] == nums[i]:
            cur_len += 1
        if cur_len > 2:
            num = nums[i-1]
            for j in range(i, length):
                nums[j - 1] = nums[j]
            nums[-1] = num
            cur_len -= 1
            
        if nums[i - 1] != nums[i]:
            cur_len = 1
            
    cur_len = 0
    for i in range(1, length):
        if nums[i - 1] > nums[i]:
            break
        else:
            cur_len+=1
    return cur_len, nums[:cur_len + 1]


if __name__ == "__main__":
    # nums1 = [1,1,1,2,2,3]
    nums2 = [0,0,1,1,1,1,2,3,3]
    # for i in [1,2]:
    #     nums = eval(f"nums{i}")
    #     print('原始:', nums)
    #     print('当前：', del_rep(nums))
    print('原始:', nums2)
    print('当前：', del_rep(nums2))
    # print(del_rep(nums2))

