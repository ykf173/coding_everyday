#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        num = 0
        i, n = 0, len(s)
        while i < n:
            if roman_dict.get(s[i:i+2], ''):
                num += roman_dict[s[i:i+2]]
                i += 2
            else:
                num += roman_dict[s[i]]
                i += 1
        return num
        
# @lc code=end
if __name__ == '__main__':
    s = Solution()

    ss = [
        "III", 
        "IV",
        "IX",
        "LVIII",
        "MCMXCIV",
        "XLIX",
        "CMXCIX"
    ]

    for x in ss:
        print(s.romanToInt(x))
