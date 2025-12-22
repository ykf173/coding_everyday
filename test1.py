'''
Author: yankaifeng ykf_173@163.com
Date: 2022-02-17 00:07:55
LastEditors: yankaifeng ykf_173@163.com
LastEditTime: 2023-11-23 19:40:25
FilePath: \coding_everyday\test1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
提示：
0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成
'''

def get_num(s):
    i, j, length = 0, 0, len(s)
    pos = [0]
    ex = set()
    for i in range(1, length):
        if s[i] in ex:
            pos.append(i)
        ex.add(s[i])

    while i< length and j < length:
        if s[j] in set(s[i:j]):
            i += pos[j]
        

    
    return j - i + 1




