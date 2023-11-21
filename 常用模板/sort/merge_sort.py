import random


def merge_sort(nums1, nums2):
    res = []
    while len(nums1) > 0 and len(nums2) > 0:
        if nums1[0] < nums2[0]:
            res.append(nums1.pop(0))
        else:
            res.append(nums2.pop(0))

    res += nums1
    res += nums2
    return res

def merge(nums):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n // 2
    left, right = nums[:mid], nums[mid:]
    return merge_sort(merge(left), merge(right))


if __name__ == '__main__':
    nums = [random.randint(1, 1000) for _ in range(100)]
    print(nums)
    print(100*'-')
    print(merge(nums))

