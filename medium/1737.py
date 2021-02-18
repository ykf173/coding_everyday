class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        ta = [0 for _ in range(26)]
        tb = [0 for _ in range(26)]
        aASCII = ord('a')  # 97
        for char in a:
            ta[ord(char) - aASCII] += 1

        for char in b:
            tb[ord(char) - aASCII] += 1

        sa, sb = 0, 0
        ans = len_a + len_b

        # a > b
        for i in range(25):  # 不考虑z
            sa += ta[i]
            sb += tb[i]
            ans = min(ans, len_a - sa + sb)  # a > b
            ans = min(ans, len_b - sb + sa)  # b > a
            ans = min(ans, len_b + len_a - ta[i] - tb[i])  # a == b

        ans = min(ans, len_a + len_b - ta[-1] - tb[-1])  # 考虑z

        return ans


if __name__ == '__main__':
    s = Solution()

    a0, b0 = "dabadd", "cda"
    a1, b1 = "aaa", "cda"
    a2, b2 = "vvv", "cda"
    a3, b3 = "acv", "cda"

    for i in range(4):
        a = eval('a%s' % i)
        b = eval('b%s' % i)

        print(s.minCharacters(a, b))
