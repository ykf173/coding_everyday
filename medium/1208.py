class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if len(s) != len(t):
            return 0

        size = len(s)
        coList = [0] * size
        for i in range(size):
            coList[i] = abs(ord(s[i]) - ord(t[i]))

        if sum(coList) <= maxCost:
            return size

        cost, maxCount = 0, 0
        left = right = 0
        while right < size:
            cost += coList[right]
            if cost > maxCost:
                cost -= coList[left]
                left += 1
            right += 1
            maxCount = max(maxCount, right - left)
        return maxCount


if __name__ == '__main__':
    s = Solution()
    while 1:
        str1 = input()
        str2 = input()
        cost = int(input())
        print(s.equalSubstring(str1, str2, cost))

'''
baaaacd
caaaadf
1

abcd
bcdf
3
abcd
cdef
3
abcd
acde
0
abcd
aaaa
10
krpgjbjjznpzdfy
nxargkbydxmsgby
14
'''
