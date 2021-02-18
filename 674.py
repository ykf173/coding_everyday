from typing import List


class Solution:
    def findlongest(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        start = 0
        for i in range(n):
            if i > 0 and nums[i - 1] >= nums[i]:
                start = i
            ans = max(ans, i - start + 1)
        return ans

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = j = 0
        longest_nums = []
        while j < len(nums):
            if j + 1 < len(nums):
                if nums[j] < nums[j + 1]:
                    j += 1
                    if len(longest_nums) < j - i + 1:
                        longest_nums = nums[i:j + 1]
                else:
                    if len(longest_nums) < j - i + 1:
                        longest_nums = nums[i:j + 1]
                    i = j + 1
                    j = j + 1

            else:
                if len(longest_nums) < j - i + 1:
                    longest_nums = nums[i:j + 1]
                return len(longest_nums)
        return len(longest_nums)


if __name__ == '__main__':
    s = Solution()
    nums0 = [1]
    nums1 = [2, 2, 2, 2]
    nums2 = [1, 3, 5, 4, 7, 9, 10]
    nums3 = [1, 3, 2]
    for i in range(4):
        num = 'nums%s' % i
        num = eval(num)
        print(s.findLengthOfLCIS(num))
        print(s.findlongest(num))
