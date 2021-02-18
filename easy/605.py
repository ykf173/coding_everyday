from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_f = len(flowerbed)
        if flowerbed == [0] and n == 1:
            return True
        for i in range(len_f):
            if n > 0:
                if i == 0 and flowerbed[i:i + 2] == [0, 0]:
                    flowerbed[i] = 1
                    n -= 1
                elif 0 < i < len_f - 1 and flowerbed[i - 1:i + 2] == [0, 0, 0]:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len_f - 1 and flowerbed[i - 1:i + 1] == [0, 0]:
                    n -= 1
        if n > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    flowerbed0, n0 = [1, 0, 0, 0, 1], 1
    flowerbed1, n1 = [0, 0, 0, 0, 1], 2
    flowerbed2, n2 = [0, 0, 0, 0, 1, 0, 0], 3
    flowerbed3, n3 = [1, 0, 0, 0, 1], 4
    flowerbed4, n4 = [0], 1

    for i in range(5):
        a = eval('flowerbed%s' % i)
        b = eval('n%s' % i)
        print(s.canPlaceFlowers(a, b))
