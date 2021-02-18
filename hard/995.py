import queue
from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        '''
        思想：使用队列统计之前的位置，个数代表之前被翻转过得次数,只统计每个子数组的起始位置
        :param A:
        :param K:
        :return:
        '''
        size = len(A)
        reverseQue = []
        ans = 0
        for i in range(size):
            if reverseQue and reverseQue[0] + K <= i:
                reverseQue.pop(0)

            if len(reverseQue) % 2 == A[i]:
                if i + K > size:
                    return -1
                reverseQue.append(i)
                ans += 1
        return ans

    def minKBitFlipsx(self, A: List[int], K: int) -> int:
        '''
        超时 时间复杂度O(N*K+N)
        :param A:
        :param K:
        :return:
        '''
        i = 0
        size = len(A)
        ans = 0
        flag = True
        while i < size:
            while i < size and A[i]:
                i += 1

            if i < size and not A[i]:
                delta = 0
                while i + delta < size and delta < K:
                    A[i + delta] = 0 if A[i + delta] else 1
                    delta += 1
                if delta != K:
                    flag = False
                ans += 1

        if A == [1] * size and flag:
            return ans
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    while 1:
        A = list(map(int, input().split(',')))
        K = int(input())
        print(s.minKBitFlips(A, K))

'''
1,1,0
2
0,0,0,1,0,1,1,0
3
0,0,0,0
1
1,1,1,1,1,1
5
'''
