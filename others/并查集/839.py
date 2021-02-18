from typing import List


class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x1: int, x2: int):
        self.parent[self.find(x2)] = self.find(x1)


class Solution:
    def isSimilar(self, s1: str, s2: str) -> bool:
        len_s = len(s1)
        diffCount = 0

        for i in range(len_s):
            if s1[i] != s2[i]:
                diffCount += 1
            if diffCount > 2:
                return False

        return True

    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = list(set(strs))
        lenS = len(strs)
        strDict = {s: idx for idx, s in enumerate(strs)}

        uf = UF(lenS)
        for i in range(lenS - 1):
            for j in range(i + 1, lenS):
                if self.isSimilar(strs[i], strs[j]):
                    uf.union(strDict[strs[i]], strDict[strs[j]])

        ans = sum(1 for i in range(lenS) if uf.parent[i] == i)
        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        strs = input().split()
        print(s.numSimilarGroups(strs))

'''
tars rats arts star
omv ovm
123
rarct tarcr
blw bwl wlb
koqnn knnqo noqnk nqkon
qihcochwmglyiggvsqqfgjjxu gcgqxiysqfqugmjgwclhjhovi gjhoggxvcqlcsyifmqgqujwhi wqoijxciuqlyghcvjhgsqfmgg qshcoghwmglygqgviiqfjcjxu jgcxqfqhuyimjglgihvcqsgow qshcoghwmggylqgviiqfjcjxu wcoijxqiuqlyghcvjhgsqgmgf qshcoghwmglyiqgvigqfjcjxu qgsjggjuiyihlqcxfovchqmwg wcoijxjiuqlyghcvqhgsqgmgf sijgumvhqwqioclcggxgyhfjq lhogcgfqqihjuqsyicxgwmvgj ijhoggxvcqlcsygfmqgqujwhi qshcojhwmglyiqgvigqfgcjxu wcoijxqiuqlyghcvjhgsqfmgg qshcojhwmglyiggviqqfgcjxu lhogcgqqfihjuqsyicxgwmvgj xscjjyfiuglqigmgqwqghcvho lhggcgfqqihjuqsyicxgwmvoj lhgocgfqqihjuqsyicxgwmvgj qihcojhwmglyiggvsqqfgcjxu ojjycmqshgglwicfqguxvihgq sijvumghqwqioclcggxgyhfjq gglhhifwvqgqcoyumcgjjisqx
rarct tarcr ratcr
abc abc abc dfg

'''
