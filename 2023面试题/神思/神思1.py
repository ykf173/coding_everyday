import math

def calculate_remaining_stock(v0, a, t):
    return v0 * math.exp(-a * t)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_arrival_time(x1, y1, x2, y2, vs):
    return calculate_distance(x1, y1, x2, y2) / vs

def plan_truck_route(warehouses, v0, a, vs):
    # remaining_stock = {warehouse: calculate_remaining_stock(v0, a, 0) for warehouse in warehouses}
    truck_route = []

    current_location = (0, 0)
    while warehouses:
        next_warehouse = None
        max_stock = -1

        for warehouse in warehouses:
            arrival_time = calculate_arrival_time(current_location[0], current_location[1], warehouse[0], warehouse[1], vs)
            stock = calculate_remaining_stock(v0, a, arrival_time)

            if stock > max_stock:
                max_stock = stock
                next_warehouse = warehouse

        if next_warehouse:
            truck_route.append(next_warehouse)
            warehouses.remove(next_warehouse)
            current_location = next_warehouse

    return truck_route

# 仓库坐标
warehouses = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]

# 初始库存
v0 = 100

# 衰减常数
a = 0.1

# 卡车速度
vs = 10

truck_route = plan_truck_route(warehouses, v0, a, vs)
print(truck_route)

# 动态规划

import math

def calculate_remaining_stock(v0, a, t):
    return v0 * math.exp(-a * t)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_arrival_time(x, y, vs):
    return calculate_distance(0, 0, x, y) / vs

def plan_truck_route(warehouses, v0, a, vs):
    N = len(warehouses)  # 仓库总数
    dp = [[0] * (1 << N) for _ in range(N + 1)]  # 动态规划数组，dp[i][S]表示卡车在前往第i个仓库时，已经经过的仓库集合为S时，卡车能够获得的最大库存量

    for S in range(1, 1 << N):  # 遍历所有仓库集合S
        for i in range(N):  # 遍历所有仓库
            if S & (1 << i):  # 仓库i在集合S中
                S_without_i = S ^ (1 << i)  # S_without_i为去掉仓库i后的集合
                max_stock = 0

                for j in range(N):
                    if S_without_i & (1 << j):  # 仓库j在集合S_without_i中
                        arrival_time = calculate_arrival_time(warehouses[i][0], warehouses[i][1], vs)
                        stock = calculate_remaining_stock(v0, a, arrival_time)

                        max_stock = max(max_stock, dp[j][S_without_i] + stock)

                dp[i][S] = max_stock

    max_total_stock = 0

    for i in range(N):
        arrival_time = calculate_arrival_time(warehouses[i][0], warehouses[i][1], vs)
        stock = calculate_remaining_stock(v0, a, arrival_time)
        max_total_stock = max(max_total_stock, dp[i][(1 << N) - 1] + stock)

    return max_total_stock

# 仓库坐标
warehouses = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]

# 初始库存
v0 = 100

# 衰减常数
a = 0.1

# 卡车速度
vs = 10

max_total_stock = plan_truck_route(warehouses, v0, a, vs)
print(max_total_stock)
