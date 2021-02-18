from typing import List


class UnionFindSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1, x2):
        self.parent[self.find(x1)] = self.find(x2)


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        '''
        方法2：并查集
        :param row:
        :return:
        '''
        size = len(row)
        N = size // 2
        uf = UnionFindSet(N)
        for i in range(0, size, 2):
            uf.union(row[i] // 2, row[i + 1] // 2)

        count = 0
        for i in range(N):
            if uf.find(i) == i:
                count += 1

        return N - count

    def minSwapsCouples1(self, row: List[int]) -> int:
        '''
        方法1：插入排序，贪心算法
        :param row:
        :return:
        '''
        count = 0
        size = len(row)
        for i in range(0, size, 2):
            firstCouple = row[i] // 2
            proPos = i // 2
            for j in range(i + 1, size):
                secondCouple = row[j] // 2
                postPos = j // 2

                if proPos == postPos and firstCouple == secondCouple:
                    break

                if proPos != postPos and firstCouple == secondCouple:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    count += 1
                    # print(row)
                    break
        return count



if __name__ == '__main__':
    s = Solution()
    while 1:
        row = list(map(int, input().split(',')))
        print(s.minSwapsCouples(row))

'''
0, 2, 1, 3
3,2,0,1
0,1,7,4,3,6,5,2
5,3,4,2,1,0
10,7,4,2,3,0,9,11,1,5,6,8

answer: [1,0,2,1,4]
'''
