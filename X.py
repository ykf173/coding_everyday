'''
1. 旋转；有序
2. 查找索引
'''


def find_ele(left, right, target, nums):
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return None


if __name__ == '__main__':
    # nums = [4, 5, 6, 7, 0, 1, 2, 3]
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    # nums = [1, 2, 3, 4, 6]
    # nums = [1, 2, 3, 4, 6, 8]
    target = 3

    print(find_ele(0, len(nums), target, nums))
