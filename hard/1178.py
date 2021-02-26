'''
外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
单词 word 中包含谜面 puzzle 的第一个字母。
单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）都不能作为谜底。
返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。
'''
import collections
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        frequency = collections.Counter()

        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord("a")))
            if str(bin(mask)).count("1") <= 7:
                frequency[mask] += 1

        ans = list()
        for puzzle in puzzles:
            total = 0

            # 枚举子集方法一
            # for choose in range(1 << 6):
            #     mask = 0
            #     for i in range(6):
            #         if choose & (1 << i):
            #             mask |= (1 << (ord(puzzle[i + 1]) - ord("a")))
            #     mask |= (1 << (ord(puzzle[0]) - ord("a")))
            #     if mask in frequency:
            #         total += frequency[mask]

            # 枚举子集方法二
            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(puzzle[i]) - ord("a")))

            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0]) - ord("a")))
                if s in frequency:
                    total += frequency[s]
                subset = (subset - 1) & mask

            # 在枚举子集的过程中，要么会漏掉全集 mask，要么会漏掉空集
            # 这里会漏掉空集，因此需要额外判断空集
            if (1 << (ord(puzzle[0]) - ord("a"))) in frequency:
                total += frequency[1 << (ord(puzzle[0]) - ord("a"))]

            ans.append(total)

        return ans


    def findNumOfValidWordsx(self, words: List[str], puzzles: List[str]) -> List[int]:
        '''
        超时
        :param words:
        :param puzzles:
        :return:
        '''
        sizeWords, sizePuzzles = len(words), len(puzzles)
        ans = []
        for i in range(sizePuzzles):
            count = 0
            for j in range(sizeWords):
                if puzzles[i][0] in words[j] and not set(words[j]) - set(puzzles[i]):
                    count += 1
            ans.append(count)

        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        words = list(eval(input()))
        puzzles = list(eval(input()))
        print(s.findNumOfValidWords(words, puzzles))

'''
["aaaa","asas","able","ability","actt","actor","access"]
["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
'''
