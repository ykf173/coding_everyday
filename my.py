def get_target_num(nums, target):
    if not nums or target > nums[-1]:
        return 0

    first_tar = bi_search_left(nums, target)
    if first_tar is None:
        return 0

    last_tar = bi_search_right(nums, target)
    return last_tar - first_tar + 1


def bi_search_left(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    if left < len(nums) and nums[left] == target:
        print('left', left)
        return left
    else:
        return None


def bi_search_right(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    if right >= 0 and nums[right] == target:
        print('right', right)
        return right
    else:
        return None


if __name__ == '__main__':
    numss = [
        [1, 2, 2, 3, 4, 4, 5, 9],
        [4, 4, 4, 4, 4, 4, 4, 4],
        [0, 0, 0, 4, 4, 4, 5, 8, 6, 7, 9],
        [0, 0, 0, 0, 4, 4, 4, 4, 5, 5, 6, 7]
    ]
    for nums in numss:
        print(get_target_num(nums, 4))
