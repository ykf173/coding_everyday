from typing import List

class Solution:
    def isSimilar(self, s1: str, s2: str) -> bool:
        s1, s2 = list(s1), list(s2)
        len_s = len(s1)
        i = 0
        if s1 == s2:
            return True

        for i in range(len_s):
            if s1[i] != s2[i]:
                break

        posList = []
        for j in range(i + 1, len_s):
            if s2[j] == s1[i]:
                posList.append(j)

        for pos in posList:
            s1[i], s1[pos] = s1[pos], s1[i]
            if s1 == s2:
                return True
        return False

    def numSimilarGroups(self, strs: List[str]) -> int:
        nums = len(strs)
        strsList = []

        for i in range(nums):
            curset = set([strs[i]])
            for j in range(i + 1, nums):
                if self.isSimilar(strs[i], strs[j]):
                    curset.add(strs[j])
            strsList.append(curset)

        len_s = len(strsList)
        for i in range(len_s):
            for j in range(len_s):
                if strsList[i] and strsList[i] != strsList[j] and strsList[i].intersection(strsList[j]):
                    strsList[i] = strsList[i].union(strsList[j])
                    strsList[j] = set()

        ssss = []
        for i in range(len_s):
            if strsList[i]:
                ssss.append(strsList[i])

        null_num = 0
        for i in range(len(ssss)):
            for j in range(i + 1, len(ssss)):
                if ssss[i].intersection(ssss[j]):
                    strsList[i] = strsList[i].union(strsList[j])
                    strsList[j] = set()
                    null_num += 1

        return len(ssss) - null_num


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
'''
