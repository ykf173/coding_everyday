import random

def merge_sort(nums):
    '''
    merge_sort 的 Docstring
    归并排序
    :param nums: 说明
    '''
    def merge(a, b):
        i = j = 0
        m, n = len(a), len(b)
        ans = []
        while i < m and j < n:
            if a[i] < b[j]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1

        ans.extend(a[i:])
        ans.extend(b[j:])
        return ans
    
    n = len(nums)
    mid = len(nums) // 2

    if n <= 1:
        return nums
    
    # 分 从上到下合
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    # 治 从底向上合
    return merge(left, right)

def heap_sort(nums):
    '''大根堆，孩子节点小于根节点'''
    def sift_adjust(i, n):
        '''
        sift_adjust 的 Docstring
        
        :param i: 待调整节点
        :param n: 全部节点
        '''
        while True:
            largest = i
            left = 2 * i + 1
            right = left + 1

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest == i:
                break

            nums[largest], nums[i] = nums[i], nums[largest]

            i = largest # 迭代调整

    # 初始化堆
    total = len(nums)
    for i in range(total//2+1, -1, -1): # 最后一层非叶子节点
        sift_adjust(i, total)

    # 根后移，排序
    for i in range(total-1, -1, -1): # 排序
        nums[0], nums[i] = nums[i], nums[0]
        sift_adjust(0, i)
    return nums

def quich_sort(nums):
    def position(left, right):
        if left >= right:
            return
        pos = random.randint(left, right)
        nums[left], nums[pos] = nums[pos], nums[left]
        povit = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= povit:
                j -= 1
            while i < j and nums[i] <= povit:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[i] = nums[i], nums[left]

        position(left, i-1)
        position(i+1, right)
        # return i
        
    position(0, len(nums)-1)
    return nums
        

if __name__ == '__main__':
    nums = [45,2,3,4,5,6,7,7,2,3,4,6,7,2143,3,4,5,6,7,72,2,5]
    # nums = [45,2,3,4,1]

    # print(merge_sort(nums))
    # print(heap_sort(nums))
    print(quich_sort(nums))