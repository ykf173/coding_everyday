from typing import List
import time

class Solution:
    def twoSum(self, num: List[int], tar: int) -> List[int]:
        lens = len(num)
        for i in range(lens-1):
            another = tar - num[i]
            if another in num[i+1:]:
                return [i, num.index(another, i+1, lens)]

    def dictory(self, num: List[int], tar: int) -> List[int]:
        dict = {}
        for i, n in enumerate(num):
            key = tar - n
            if  key in dict:
                return [dict.get(key), i]

            dict[n] = i

start = time.perf_counter()
s = Solution()
print(s.dictory([3,3], 6))
end = time.perf_counter()
print('programing running time is ', end-start)
a = [1, 2, 4]
if 2 in a[1:]:
    print(2)