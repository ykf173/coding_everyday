# 蚂蚁一面
# 给定一个有序数组，arr = [1, 2, 2, 3, 4, 4, 5, 9]，查找target=4，返回出现次数，要求时间复杂度logn。
# [4, 4, 4, 4, 4, 4, 4]

def get_taget_num(nums, target):
    if not nums or target > nums[-1]:
        return None
    first_tar = bi_search_left(nums, target)
    last_tar = bi_search_right(nums, target)
    return last_tar - first_tar + 1


def bi_search_left(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            if mid == 0 or (mid > 0 and nums[mid - 1] != target):
                print('left:', mid)
                return mid
            else:
                right = mid - 1



def bi_search_right(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            if mid == right - 1 or (mid < right and nums[mid + 1] != target):
                print('right', mid)
                return mid
            else:
                left = mid + 1



if __name__ == '__main__':
    numss = [
        [1, 2, 2, 3, 4, 4, 5, 9],
        [4, 4, 4, 4, 4, 4, 4, 4],
        [0, 0, 0, 4, 4, 4, 5, 8, 6, 7, 9],
        [0, 0, 0, 0, 4, 4, 4, 4, 5, 5, 6, 7]
    ]
    for nums in numss:
        print(get_taget_num(nums, 4))
