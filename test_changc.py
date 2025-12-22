'''
Author: yankaifeng ykf_173@163.com
Date: 2024-01-02 18:58:23
LastEditors: yankaifeng ykf_173@163.com
LastEditTime: 2024-01-02 20:36:50
FilePath: \coding_everyday\test_changc.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""

def pertem(nums):
    root = [[_] for _ in nums]
    n = len(nums)
    res = root
    while len(res[-1]) != n:
        res = []
        for r in root:
            for j in range(n):
                if nums[j] not in r:
                    res.append(r + [nums[j]])
                    
            root = res
    
    return res
        
    # return pertem(nums)


if __name__ == "__main__":
    n_nums = [
        [1,2,3],
        [0,1],
        [1],
        [1,2,3,4]
    ]

    for nums in n_nums:
        n = len(nums)
        print(pertem(nums))
            