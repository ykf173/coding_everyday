class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        con_z = [[None] * len_s for _ in range(numRows)]

        if numRows <= 1: #特殊情形，直接返回
            return s

        i = num = j = 0
        for ch in s:
            if not j % (numRows - 1):
                con_z[i][j] = ch

                if i < numRows - 1:
                    i += 1
                else:
                    i -= 1
                    j += 1
            else:
                con_z[i][j] = ch
                num += 1
                j += 1
                i -= 1

        ans = ''
        for i in range(numRows):
            for j in range(len_s):
                if con_z[i][j]:
                    ans += con_z[i][j]

        return ans


if __name__ == '__main__':
    s = Solution()

    s0, numRows0 = "PAYPALISHIRING", 3  # PAHNAPLSIIGYIR
    s1, numRows1 = "PAYPALISHIRING", 4  # PINALSIGYAHRPI
    s2, numRows2 = "PAYPALISHIRING", 1
    s3, numRows3 = "ABCDEFG", 2          # ACEGBDF
    s4, numRows4 = "PAYPALISHIRING", 3
    s5, numRows5 = "PAYPALISHIRING", 3
    for i in range(6):
        ss = eval('s%s' % i)
        numRows = eval('numRows%s' % i)

        print(s.convert(ss, numRows))
