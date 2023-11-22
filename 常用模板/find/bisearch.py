import random

def quick_sorted(nums, left, right):
    if left <= right:
        low, high = left, right
        cur_num = nums[left]
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

        quick_sorted(nums, left, low - 1)
        quick_sorted(nums, low + 1, right)


def bisearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    return f'not found {target}'

if __name__ == '__main__':
    nums = [random.randint(1, 10000) for _ in range(1000)]
    numsed = nums[:]
    target = random.choice(nums)
    quick_sorted(numsed, 0, len(numsed) - 1)
    print(nums)
    print(150*'-')
    print(numsed)

    print(set(nums) == set(numsed))
    print(f'我要找{target}')
    print(numsed.index(target))
    print(bisearch(numsed, target))
