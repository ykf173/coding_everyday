# 我们从一块字母板上的位置(0, 0)出发，该坐标对应的字符为board[0][0]。
# 
# 在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。
#
# 我们可以按下面的指令规则行动：
# 
# 如果方格存在，'U'意味着将我们的位置上移一行；
# 如果方格存在，'D'意味着将我们的位置下移一行；
# 如果方格存在，'L'意味着将我们的位置左移一列；
# 如果方格存在，'R'意味着将我们的位置右移一列；
# '!'会把在我们当前位置 (r, c) 的字符board[r][c]添加到答案中。
# （注意，字母板上只存在有字母的位置。）
# 
# 返回指令序列，用最小的行动次数让答案和目标target相同。你可以返回任何达成目标的路径。
#
# 
# 示例 1：
# 
# 输入：target = "leet"
# 输出："DDR!UURRR!!DDD!"
# 示例 2：
# 
# 输入：target = "code"
# 输出："RR!DDRR!UUL!R!"
# 
# 
# 提示：
# 
# 1 <= target.length <= 100
# target仅含有小写英文字母。


class Solution:
    def __init__(self):
        k = 0
        self.positions = {}
        for i in range(6):
            for j in range(5):
                self.positions[chr(k + 97)] = (i, j)
                k += 1

    def alphabetBoardPath(self, target: str) -> str:
        res = ''
        target = 'a' + target
        len_t = len(target)

        for i in range(len_t - 1):
            h = self.positions[target[i]][0] - self.positions[target[i + 1]][0]
            w = self.positions[target[i]][1] - self.positions[target[i + 1]][1]
            if h > 0:
                res += 'U' * h
            if w > 0:
                res += 'L' * w
            if w < 0:
                res += -1 * w * 'R'

            if h < 0:
                res += -1 * h * 'D'
            res += '!'

        return res


if __name__ == '__main__':
    s = Solution()

    targets = [
        # 'leet',
        # 'code',
        # 'xxxxx',
        # 'z',
        'zdz' #"DDDDD!UUUUURRR!DDDDLLLD!"
    ]

    for target in targets:
        print(s.alphabetBoardPath(target))
