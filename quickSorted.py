def quickSoted(left, right, nums):
    if left < right:
        low, high = left, right
        cur = nums[low]
        while low < high:
            while low < high and nums[high] >= cur:
                high -= 1
            if low < high:
                nums[low] = nums[high]
            while low < high and nums[low] <= cur:
                low += 1
            if low < high:
                nums[high] = nums[low]
        nums[low] = cur
        quickSoted(left, low - 1, nums)
        quickSoted(low + 1, right, nums)


if __name__ == '__main__':
    nums = [4, 56, 6, 30, 7, 8, 5, 9, 20]
    print(nums)
    quickSoted(0, len(nums) - 1, nums)
    print(nums)
