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


if __name__ == '__main__':
    nums = [random.randint(1, 10000) for _ in range(1000)]
    numsed = nums[:]
    quick_sorted(nums, 0, len(nums) - 1)
    print(numsed)
    print(150*'-')
    print(nums)
    print(set(nums) == set(numsed))