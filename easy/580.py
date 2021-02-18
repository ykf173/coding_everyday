from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return list(set(list(range(1, n + 1))) - set(nums))


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.findDisappearedNumbers(nums))

'''
4,3,2,7,8,2,3,1

'''
