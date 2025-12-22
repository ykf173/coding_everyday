# 输入数组，输出数组中第三大数的下标，不存在返回-1。
def get_top3(nums, left, right):
    tmp = nums[left]
    low, high = left, right
    while low < high:
        while low < high and nums[high] >= tmp:
            high -= 1
        if low < high:
            nums[low] = nums[high]
        while low < high and nums[low] <= tmp:
            low += 1
        if low < high:
            nums[high] = tmp

    return

def get_topn(nums, left, right, n):
    if n > left:
        return None
    if left < right:
        low, high = left, right
        tmp = nums[low]
        while low < high:
            while low < high and nums[high] >= tmp:
                high -= 1
            if low < high:
                nums[low] = nums[high]
            while low < high and nums[low] <= tmp:
                low += 1
            if low < high:
                nums[high] = nums[low]
        nums[low] = tmp
        if low == n:
            return n
        quicksort(nums, left, low - 1)
        quicksort(nums, low + 1, right)


def quicksort(nums, left, right):
    # pos = get_top3(nums, left, right)
    if left < right:
        low, high = left, right
        tmp = nums[low]
        while low < high:
            while low < high and nums[high] >= tmp:
                high -= 1
            if low < high:
                nums[low] = nums[high]
            while low < high and nums[low] <= tmp:
                low += 1
            if low < high:
                nums[high] = nums[low]
        nums[low] = tmp
        quicksort(nums, left, low - 1)
        quicksort(nums, low + 1, right)

def bi_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


if __name__ == '__main__':
    numss = [
        [6, 5, 4, 9, 2],
        [6, 5, 4, 9, 7, 8]
    ]
    # for nums in numss:
        # quicksort(nums, 0, len(nums) - 1)
        # n = int(input('top-'))
        # if n > len(nums):
        #     continue
        # get_topn(nums, 0, len(nums) - 1, n)
        # print(nums[:n])

    for nums in numss:
        quicksort(nums, 0, len(nums) - 1)
        print(nums)
        print(bi_search(nums, 5))