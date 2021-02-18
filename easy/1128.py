import time
from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs1(self, dominoes: List[List[int]]) -> int: # 超时
        equal_num = 0
        domino_num = defaultdict(int)
        if len(dominoes) <= 1:
            return 0
        for i in range(len(dominoes)):  # 统一为前小后大
            dominoes[i] = [dominoes[i][1], dominoes[i][0]] if dominoes[i][1] < dominoes[i][0] else dominoes[i]

        for i in range(len(dominoes) - 1):
            key = str(set(dominoes[i]))
            if key not in dominoes:
                domino_num[key] = dominoes.count(dominoes[i])

        for _, num in domino_num.items():
            equal_num += num * (num - 1) / 2

        return int(equal_num)

    def numEquivDominoPairs2(self, dominoes: List[List[int]]) -> int: # 超时
        equal_num = 0
        domino_num = defaultdict(int)
        if len(dominoes) <= 1:
            return 0

        for x, y in dominoes:
            key = tuple([x, y] if x < y else [y, x])
            if key not in dominoes:
                domino_num[key] += 1

        for _, num in domino_num.items():
            equal_num += num * (num - 1) // 2

        return equal_num

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        equal_num = 0
        dominoes_num = [0] * 100

        for x, y in dominoes:
            index = x * 10 + y if x < y else y * 10 + x
            equal_num += dominoes_num[index]  # 模拟了顺序相加的过程 0+1+2
            dominoes_num[index] += 1
        return equal_num


if __name__ == '__main__':
    s = Solution()
    dominoes0 = [[1, 2], [2, 1], [3, 4], [5, 6]]
    dominoes1 = [[1, 2], [2, 1], [1, 2], [5, 6]]
    dominoes2 = [[1, 2], [2, 1], [3, 4], [3, 4]]
    dominoes3 = [[1, 2], [2, 1], [3, 4], [4, 3]]
    dominoes4 = [[1, 2], [2, 1], [3, 4], [4, 3], [0, 0]]
    dominoes5 = [[1, 2], [2, 1], [3, 4], [4, 3], [0, 0], [0, 0]]
    dominoes6 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(7):
        start = time.perf_counter()
        dominoes = eval('dominoes%s' % i)
        print(s.numEquivDominoPairs2(dominoes))
        print(f'总耗时：{time.perf_counter() - start}')


        start = time.perf_counter()
        print(s.numEquivDominoPairs(dominoes))
        print(f'总耗时：{time.perf_counter() - start}')

