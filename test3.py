# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = set()
        sums = []
        for i in range(n):
            for j in range(i + 1, n):
                sums.append([nums[i], nums[j], i, j])

        for i in range(len(sums)):
            num = -1 * sum(sums[:-2])
            for j in range(n):
                if num in nums and i not in sums[2:]:
                    tmp = sums[i].append(num)
                    # tmp
                    res.add(str(tmp))

        res = list(res)
        for i in range(len(res)):
            res[i] = eval(res[i])

        return res

