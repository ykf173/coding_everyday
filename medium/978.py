from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        size = len(arr)
        if size == 1 or len(set(arr)) == 1:
            return 1
        left, right = 0, 2
        maxCount = 1
        dis = arr[1] - arr[0]

        while right < size:
            if ((arr[right] - arr[right - 1]) * dis) >= 0:
                maxCount = max(maxCount, right - left)
                left = right - 1

            dis = arr[right] - arr[right - 1]
            right += 1
        return max(maxCount, right - left)


if __name__ == '__main__':
    s = Solution()
    while 1:
        arr = list(map(int, input().split(',')))
        print(s.maxTurbulenceSize(arr))

'''
9,4,2,10,7,8,8,1,9
4,8,12,16
100
9,9
10,10,10
10,10,11
9,4,5,2,1,6,4,7,5,8,10,11
0,8,45,88,48,68,28,55,17,24

答案：[5,2,1,1,1,2,7,8]
'''
