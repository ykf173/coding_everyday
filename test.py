def is_all_zero(s):
    m = ''
    for n in s:
        m = m + n
    if m == 0:
        return True
    else:
        return False

def reverse_str(s):
    new_str1 = list(s)
    new_str2 = new_str1[:]
    for i in range(len(s)):
        count = 0
        if new_str1[i] == '1':
            new_str2[i] = '0'
            if 0 <= i-1 <= len(s) - 1 and new_str1[i-1] == '1':
                new_str2[i-1] = '0'
            if 0 <= i+1 <= len(s) - 1 and new_str2[i + 1] == '1':
                new_str2[i+1] = '0'
            if is_all_zero(new_str2):
                count += 1


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        reverse_str(s)
    # print(is_all_zero(['1','2','3']))