'''
如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。
'''
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        '''
        设计标志位，不能同时出现单调递增递减
        :param A:
        :return:
        '''
        size = len(A)
        increaseFlag, decreaseFlag = True, True
        for i in range(1, size):
            if A[i] > A[i - 1]:
                decreaseFlag = False
            elif A[i] < A[i - 1]:
                increaseFlag = False
        return increaseFlag or decreaseFlag

    def isMonotonicS(self, A: List[int]) -> bool:
        '''
        三轮遍历，第一轮确定趋势，递增，递减
        第二轮，递增出现递减为false
        第三轮，递减出现递增为flase
        :param A:
        :return:
        '''
        size = len(A)
        increaseFlag = True
        i = 0
        if size == 1:
            return True

        for i in range(1, size):  # 确定单调递增，递减
            if A[0] > A[i]:
                increaseFlag = False
                break
            elif A[0] < A[i]:
                break

        if i == size - 1:
            return True

        for i in range(1, size):
            if increaseFlag and A[i] < A[i - 1]:
                return False

        if i == size - 1 and increaseFlag:
            return True

        for i in range(1, size):
            if not increaseFlag and A[i] > A[i - 1]:
                return False

        if i == size - 1 and not increaseFlag:
            return True


if __name__ == '__main__':
    s = Solution()
    while 1:
        A = list(map(int, input().split(',')))
        print(s.isMonotonic(A))

'''
1,2,2,3
6,5,4,4
1,2,4,5
111,22,14,5
1,1,1
22222
1,3,2
111,12,24,5
'''
