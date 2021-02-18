import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sizeS1, sizeS2 = len(s1), len(s2)
        if sizeS1 > sizeS2:
            return False
        front, back = 0, sizeS1
        alphS1 = [0] * 26
        alphS2 = [0] * 26
        for ch1, ch2 in zip(s1, s2[:back]):
            alphS1[ord(ch1) - ord('a')] += 1
            alphS2[ord(ch2) - ord('a')] += 1

        while back < sizeS2:
            if alphS2 == alphS1:
                return True
            else:
                alphS2[ord(s2[back]) - ord('a')] += 1
                alphS2[ord(s2[front]) - ord('a')] -= 1
                front, back = front + 1, back + 1
        return alphS2 == alphS1

    def checkInclusionX(self, s1: str, s2: str) -> bool:
        sizeS2 = len(s2)
        left = right = 0

        while right < sizeS2:
            continueFlag = True
            list_s1 = list(s1)
            while left < sizeS2 and s2[left] in list_s1:
                continueFlag = False
                list_s1.remove(s2[left])
                left += 1
            if not list_s1:
                return True
            if continueFlag:
                right += 1
                left = right
        return False


if __name__ == '__main__':
    s = Solution()
    while 1:
        s1 = input()
        s2 = input()
        print(s.checkInclusion(s1, s2))

'''
ab
eidbaooo
ab
eidboaoo
abc
efiobcwabxcba
abc
efiobcwabxcbd
adc
dcda
'''
