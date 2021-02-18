from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left, right = 0, k
        lenN = len(nums)
        medians = []
        while right <= lenN:
            window = sorted(nums[left:right])
            median = k // 2
            if (right - left) % 2:
                medians.append(window[median])
            else:
                medians.append((window[median - 1] + window[median]) / 2)
            left, right = left + 1, right + 1
        return medians


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        k = int(input())
        print(s.medianSlidingWindow(nums, k))

''''测试用例
1,3,-1,-3,5,3,6,7
3

1,4,2,3
4

'''
