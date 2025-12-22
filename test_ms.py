'''
整数数组，找出最大和子数组，返回最大和
input = [-2, 1, -3, 4, -1, 2, 1, -5, 4] output = 6
'''

def get_max_sub_arr(nums):
    n = len(nums)
    if n < 2:
        return nums[0]
    
    for i in range(1, n):
        if nums[i - 1] > 0:
            nums[i] += nums[i-1]
    
    return max(nums)
    

if __name__ == "__main__":
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    output = 6
    print(get_max_sub_arr(input))

        
