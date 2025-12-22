# 找出数组中最长严格递增子序列 nums=[1,8,4,8], return res=3

def get_max_sub(nums):
    n = len(nums)
    if n < 2:
        return n
    
    is_sub = [1] + [0] * (n - 1)
    
    # cur_idx = 0
    for i in range(1, n):
        if nums[i] > nums[cur_idx]:
            for j in range(1, is_sub):
                if is_sub[j] > is_sub[j - 1]:
                    
            is_sub[i] = is_sub[cur_idx] + 1
            cur_idx = i
        # cur_idx = i

    return max(is_sub)


if __name__ == '__main__':
    n_nums = [
        [1,2,4,8],
        [1,8,4,8],
        [8,4,2,1]
    ]
    for nums in n_nums:
        get_max_sub(nums)        



