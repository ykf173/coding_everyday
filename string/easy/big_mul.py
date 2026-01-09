def big_mul(a, b):
    cur_add = 0
    ans = []
    sign = 1
    if a < 0 and b > 0 or a > 0 and b < 0:
        sign = -1

    a = abs(a)
    b = abs(b)
    str_a = str(a)
    n = len(str_a)
    for i in range(n-1, -1, -1):
        tmp = b * int(str_a[i]) + cur_add
        ans.append(str(tmp % 10))
        cur_add = tmp // 10
    
    while cur_add % 10:
        ans.append(str(cur_add % 10))
        cur_add //= 10

    res = ''.join(ans[::-1])

    if sign == -1:
        res = '-' + res
    return res

print(big_mul(123456789, -987654321))   # 121932631112635269
# print(big_mul(-012, 003))             # -36
