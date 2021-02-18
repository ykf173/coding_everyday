import collections
from typing import List


class Solution:
    def maxCounterK(self, A: List[int], K: int) -> int:
        size = len(A)
        left = right = 0
        ans = 0

        while right < size:
            sizeSet = len(set(A[left:right + 1]))
            while sizeSet > K:
                left += 1
                sizeSet = len(set(A[left:right + 1]))
            right += 1
            ans += right - left + 1
        return ans

    def atMostK(self, A, K):
        N = len(A)
        left, right = 0, 0
        counter = collections.Counter()
        distinct = 0
        res = 0
        while right < N:
            if counter[A[right]] == 0:
                distinct += 1
            counter[A[right]] += 1
            while distinct > K:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    distinct -= 1
                left += 1
            res += right - left + 1
            # print(left, right, res)
            right += 1
        return res


    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K - 1)


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        k = int(input())
        print(s.subarraysWithKDistinct(nums, k))

'''
1,2,1,2,3
2
1,2,1,3,4
3
1,1,1,1,1
1
1,1,1,1,1
2
1,1,1,1,1
3
2,1,2,1,2
2

答案：[7,3,15,0,0,10]
'''
