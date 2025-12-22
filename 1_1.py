# 写一个函数f（N），返回1到N之间出现“1”的个数，例如f（11）=4

def count_1(n):
    count = 0
    for i in range(1, n + 1):
        while i:
            if i % 10 == 1:
                count += 1
                # print(i)
            i //= 10

    return count


if __name__ == '__main__':
    n = [0, 1, 2, 10, 11, 100, 12, 13, 14, 21, 31]
    for x in n:
        print(x, count_1(x))
