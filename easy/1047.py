'''
给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。


示例：
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

提示：
1 <= S.length <= 20000
S 仅由小写英文字母组成。
'''


class Solution:
    def removeDuplicates(self, S: str) -> str:
        '''
        使用栈，类似括号匹配
        :param S:
        :return:
        '''
        stack = []
        size = len(S)
        for i in range(size):
            if stack and stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        return ''.join(stack)


    def removeDuplicatesX(self, S: str) -> str:
        '''
        暴力
        :param S:
        :return:
        '''
        left, right = 0, 1
        list_S = list(S)
        while left > -1 and right < len(list_S):
            if list_S[left] == list_S[right]:
                list_S.pop(left)
                list_S.pop(left)
                if left > 0:
                    left -= 1
                    right = left + 1
            else:
                left += 1
                right = left + 1
        return ''.join(list_S)


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        print(s.removeDuplicates(string))

'''
caabbdacd
abcde
abbcdde
aaaaa
aaaa
abbaca
abcdeffedcbb
'''
