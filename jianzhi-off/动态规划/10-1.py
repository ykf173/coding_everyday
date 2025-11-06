MAX = 1000000007

class Solution:
    def fib(self, n: int) -> int:
        pro, post = 0, 1
        for _ in range(n):
            pro, post = post, (pro + post) % MAX
        return pro


if __name__ == '__main__':
    s = Solution()
    while 1:
        n = int(input())
        print(s.fib(n))
