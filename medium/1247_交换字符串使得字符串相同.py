# 有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。
# 
# 每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
# 
# 交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。
# 
# 最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。
# 
#  
# 
# 示例 1：
# 
# 输入：s1 = "xx", s2 = "yy"
# 输出：1
# 解释：
# 交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。
# 示例 2：
# 
# 输入：s1 = "xy", s2 = "yx"
# 输出：2
# 解释：
# 交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
# 交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
# 注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。
# 示例 3：
# 
# 输入：s1 = "xx", s2 = "xy"
# 输出：-1
# 示例 4：
# 
# 输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
# 输出：4
#  
# 
# 提示：
# 
# 1 <= s1.length, s2.length <= 1000
# s1, s2 只包含 'x' 或 'y'。
from collections import defaultdict


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        s1, s2 = list(s1), list(s2)
        len_s1 = len(s1)
        len_s2 = len(s2)
        res = 0
        if len_s1 != len_s2:
            return res

        not_equ_pos = []
        s1_swap_pos, s2_swap_pos = defaultdict(list), defaultdict(list)
        for i in range(len_s1):
            if s1[i] != s2[i]:
                not_equ_pos.append(i)
                s1_swap_pos[s1[i]].append(i)
                s2_swap_pos[s2[i]].append(i)

        if 'x' in s1_swap_pos and 'x' in s2_swap_pos and len(s1_swap_pos['x']) == len(s2_swap_pos['x']):
            res += len(s1_swap_pos['x'])
        if 'y' in s1_swap_pos and 'y' in s2_swap_pos and len(s1_swap_pos['y']) == len(s2_swap_pos['y']):
            res += len(s1_swap_pos['y'])

        return res


if __name__ == '__main__':
    s11 = ["xxyyxyxyxx", "xx", "yx", 'xx', 'y', 'xxy']
    s22 = ["xyyxyxxxyx", "yy", "xy", "xy", 'x', 'xy']

    s = Solution()
    for s1, s2 in zip(s11, s22):
        print(s.minimumSwap(s1, s2))
