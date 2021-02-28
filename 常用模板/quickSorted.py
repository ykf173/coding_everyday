def quickSorted(nums, left, right):
    if left < right:
        curNum = nums[left]
        while left < right:
            while left < right and curNum < nums[right]:
                right -= 1
            nums[left] = nums[right]
            while left < right and curNum > nums[left]:
                left += 1
            nums[right] = nums[left]
        nums[left] = curNum
        quickSorted(nums, 0, left - 1)
        quickSorted(nums, left + 1, right)


if __name__ == '__main__':
    nums = [29, 1, 2, 4, 6, 7, 50, 3]
    size = len(nums)
    quickSorted(nums, 0, size - 1)
    print(nums)
