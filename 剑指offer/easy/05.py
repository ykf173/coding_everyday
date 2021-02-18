class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:
            return ''
        else:
            lenStering = len(s)
            ss = '%20'
            i = 0
            while i < lenStering:
                if s[i] == ' ':
                    s = s[:i] + ss + s[i + 1:]
                    i += 2
                    lenStering += 2
                i += 1
        return s


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        print(s.replaceSpace(string))
