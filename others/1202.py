from typing import List


class Solution:
    def swap(self, s, pair_index: List):
        s_list = list(s)
        s_list[pair_index[0]], s_list[pair_index[1]] = s_list[pair_index[1]], s_list[pair_index[0]]
        return ''.join(s_list)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        swap_s = ''
        flag = True
        while swap_s < s and flag:
            for pair in pairs:
                swap_s = self.swap(s, pair)
                print(swap_s, pair)
                if swap_s < s:
                    s = swap_s
                if pairs.index(pair) == len(pairs) - 1:
                    flag = False
        return s


if __name__ == '__main__':
    s = Solution()
    ss = "dcab"
    # print(s.swap(ss, [1, 2]))
    pairs = [[0, 3], [1, 2], [0, 2]]
    print(s.smallestStringWithSwaps(ss, pairs))
