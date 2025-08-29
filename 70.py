
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [-1] + [1] * (n)
        for i in range(2, n + 1):
            d[i] = d[i - 1] + d[i - 2]
        return d[n]
    
if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(s.climbStairs(i))