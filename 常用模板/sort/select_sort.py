import random


def select_sort(nums):
    i, length  = 0, len(nums)
    while i < length:
        min_id, j = i, i + 1
        while j < length:
            if nums[j] < nums[min_id]:
                min_id = j
            j += 1
        nums[i], nums[min_id] = nums[min_id], nums[i]
        i += 1
    return nums


if __name__ == '__main__':
    nums = [random.randint(1, 1000) for _ in range(100)]
    print(nums)
    print(100*'-')
    print(select_sort(nums))