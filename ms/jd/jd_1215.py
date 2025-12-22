# n个数，m个桶，每个桶数值和尽可能相等

def partitial(m, nums):
    nums.sort(reverse=True)
    mean = sum(nums) / m
    min_val = nums[0]

    n = len(nums)
    ans = []
    cur = []
    
    cur_sum = 0
    i = 0
    while i < n and m > 0:
        if nums[i] >= mean:
            ans.append(nums[i])
            m -= 1
        else:
            cur.append(nums[i])
            cur_sum += nums[i]

        if abs(cur_sum - mean) < min_val:
            if cur_sum <= 0:
                ans.append([nums[i]])
            ans.append(cur)
            cur, cur_sum = [], 0
            m -= 1

        if i + 1 < n:
            min_val = nums[i+1]
        else:
            min_val = nums[-1]

        i += 1

    
    return ans




if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    m = 3

    print(partitial(m, nums))

