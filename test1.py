from typing import List


def maxSumX(nums: List[int]):
    '''
    最大子数组和
    :return:
    '''
    lenN = len(nums)
    maxValue = float('-inf')
    left = right = 0
    sumN = 0
    while right < lenN:
        sumN += nums[right]
        print(nums[left], nums[right])
        if sumN < maxValue:
            sumN -= nums[left]
            left += 1
        else:
            right += 1
        maxValue = max(maxValue, sumN)

    return maxValue


def maxSum(nums: List[int]):
    '''
    最大子数组和
    :return:
    '''
    lenN = len(nums)
    maxValue = float('-inf')
    left = right = 0
    sumN = 0
    for i in range(lenN):
        for j in range(i + 1, lenN):
            maxValue = max(maxValue, sum(nums[i: j]))

    return maxValue


def sortN(nums):
    lenN = len(nums)
    for i in range(lenN):
        for j in range(i + 1, lenN):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


def mediumNum(nums):
    nums = sortN(nums)
    lenN = len(nums)
    medium = lenN // 2
    if not lenN:
        return 'not list'
    if len(nums) % 2:
        return nums[medium]
    else:
        return (nums[medium] + nums[medium + 1]) / 2


if __name__ == '__main__':
    while 1:
        nums = list(map(int, input().split(',')))
        print(maxSumX(nums))
        # print(sortN(nums))
        # print(mediumNum(nums))

'''

1, 3, 2, 4, 7, 6, 5
1, 3, 2, 4, 7, 6, 5,9
'''

''''
-2,1,-3,4,-1,2,1,-5,4
-2,1,-3,4,-1,2,1,-5,4,3 
-2,1,-3,4,-1,2,1,1,1,1,1,-5,4
1,1,1,1
1,0,1,-1,2
1


6
10
4
3
1
'''
