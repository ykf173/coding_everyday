from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        k = i = 0
        j = len(nums)

        while k < j:
            if sum(nums[i:k]) == sum(nums[k + 1:j]):
                return k
            else:
                k += 1
        else:
            return -1


if __name__ == '__main__':
    s = Solution()

    while 1:
        nums = list(map(int, input().split(',')))
        print(s.pivotIndex(nums))

'''
1, 7, 3, 6, 5, 6
1, 2, 3
1,1,3,2
-1, 10, 1, -10, 0
-1, 10, 1, -10,1, 0, 0, 0, 1
'''
