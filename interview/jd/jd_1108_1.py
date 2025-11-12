# 给你两个字符串，比如s1=acdk, s2=ckad，每次可以把s1的任意一个字母移动到末尾，
# 问最少移动次数使s1==s2。如果不存在，则返回-1；


def min_move(s1, s2):
    if set(s1) != set(s2):
        return -1
    
    m, n = len(s1), len(s2)

    i = j = 0
    p = 0

    s1, s2 = list(s1), list(s2)
    while i < m:
        if s1[i] == s2[j]:
            j += 1
            p += 1
        else:
            i += 1
        
    return m - p



if __name__ == '__main__':
    s1='acdk'
    s2='ckad'

    print(min_move(s1, s2))
