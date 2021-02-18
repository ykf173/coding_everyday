from typing import List


class Solution:

    def fairCandySwap2(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        halfSum = (sumA + sumB) // 2
        lenA, lenB = len(A), len(B)

        def findEqualValue(A: list, B: list, sumB, lenB) -> List[int]:
            C = [sumB - B[i] for i in range(lenB)]
            setC = set(C)
            for x in A:
                if halfSum - x in setC:
                    return [x, B[C.index(halfSum - x)]]

        if len(A) <= len(B):
            return findEqualValue(A, B, sumB, lenB)
        else:
            return findEqualValue(B, A, sumA, lenA)[::-1]

    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        v = (sum(A) - sum(B)) // 2
        setB = set(B)
        for x in A:
            if x - v in setB:
                return [x, x - v]


if __name__ == '__main__':
    s = Solution()
    while 1:
        A = list(map(int, input().split(',')))
        B = list(map(int, input().split(',')))
        print(s.fairCandySwap(A, B))

'''
1,1,2,1,4
2,3,3,5
1,1
2,2
1,2
2,3
2
3,1
1,2,5
2,4
'''
