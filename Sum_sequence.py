def cul_a1(N, n):
    first_value = (2 * N - n * (n - 1)) // (2 * n)
    flag = (2 * N - n * (n - 1)) / (2 * n) == first_value
    return flag, first_value


def print_sequence(a1, n):
    for a in range(a1, a1 + n-1):
        print(a, end=" ")
    print(a1 + n-1, end="")


class Sum:
    def sum_sequence(self, N, L):
        flag = True
        for i in range(L, N//2):
            if i <= 100:
                t = cul_a1(N, i)
                if t[0]:
                    flag = False
                    print_sequence(t[1], i)
                    break
            else:
                flag = False
                print("No")
                break
        if flag:
            print("No")


N, L = map(int, input().split())
s = Sum()
s.sum_sequence(N, L)
