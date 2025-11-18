"""
题目描述
给出一个nxm的点阵,第i行第j列的点为(i,j)。
初始时,马被放置在(1,1)位置上。众所周知马走日,形式化来说,若马位于(2,y),其可以跳到(x+1,y+2),(a-1y+2),(a+1,y-2),(2-1,y-2),(2),(a+2,y+1),(ж-2,y+1), (σ+2,y-1),(۰-2,y -
1)其中之一。
注意,马的位置(æ,y)必须时刻保持1<x<n,1<y<m。
询问在nxm的点阵上,马能跳到多少个位置。
输入描述:
第一行一个整数T,表示询问组数。
接下来T行,每行两个数n,m,表示一组询问。
输出描述:
输出为T行,即每组数据的答案。

示例1
输入
3
3 3
2 3
100 100

输出：
8
2
10000
"""
def bfs(m, n):
    x, y = {-2, -1, 1, 2}, {-1, -2, 1, 2}
    m, n = m + 1, n + 1
    visited = [[0] * n for _ in range(m)]
    i, j = 1, 1
    visited[i][j] = 1
    stack = [(i, j)]
    while stack and 1 <= i < n and 1 <= j < m:
        for i_x in x:
            for j_y in y:
                if abs(i_x) != abs(j_y):
                    i_tmp, j_tmp = i + i_x, j + j_y
                    if stack and 1 <= i_tmp < m and 1 <= j_tmp < n and not visited[i_tmp][j_tmp]:
                        visited[i_tmp][j_tmp] = 1
                        stack.append((i_tmp, j_tmp))

        i, j = stack.pop()

    return sum([sum(vis) for vis in visited])


def statistic(m, n):
    if m == 2:
        return (n + 1) // 2
    elif n == 2:
        return (m + 1) // 2
    
    elif m == 1 or n == 1:
        return 1
    
    elif m == 3 and n ==3:
        return 8
    
    else:
        return m * n

    return sum([sum(vis) for vis in visited])

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m, n = map(int, input().split())
        # res = bfs(m, n)
        res = statistic(m, n)
        print(res, end='')
        if i != t-1:
            print()


            



