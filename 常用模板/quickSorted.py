def quickSorted(nums, left, right):
    if left < right:
        low, high = left, right
        curNum = nums[low]
        while low < high:
            while low < high and curNum <= nums[high]:
                high -= 1
            if low < high:
                nums[low] = nums[high]
            while low < high and curNum >= nums[low]:
                low += 1
            if low < high:
                nums[high] = nums[low]
        nums[low] = curNum
        quickSorted(nums, left, low - 1)
        quickSorted(nums, low + 1, right)


if __name__ == '__main__':
    nums = [29, 1, 2, 4, 6, 7, 50, 3, 1000, 0, 0]
    size = len(nums)
    quickSorted(nums, 0, size - 1)
    print(nums)
