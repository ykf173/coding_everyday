import math

def calculate_remaining_stock(v0, a, t):
    return v0 * math.exp(-a * t)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_arrival_time(x1, y1, x2, y2, vs):
    return calculate_distance(x1, y1, x2, y2) / vs

def plan_truck_route(warehouses, v0, a, vs, w):
    remaining_stock = {warehouse: calculate_remaining_stock(v0, a, 0) for warehouse in warehouses}
    truck_route = []

    current_location = (0, 0)
    total_distance = 0

    while warehouses and total_distance + calculate_distance(current_location[0], current_location[1], 0, 0) <= w:
        next_warehouse = None
        max_stock = -1

        for warehouse in warehouses:
            arrival_time = calculate_arrival_time(warehouse[0], warehouse[1], vs)
            stock = calculate_remaining_stock(v0, a, arrival_time)

            if stock > max_stock:
                max_stock = stock
                next_warehouse = warehouse

        if next_warehouse:
            truck_route.append(next_warehouse)
            warehouses.remove(next_warehouse)
            current_location = next_warehouse
            total_distance += calculate_distance(current_location[0], current_location[1], 0, 0)

    return truck_route

# 仓库坐标
warehouses = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]

# 初始库存
v0 = 100

# 衰减常数
a = 0.1

# 卡车速度
vs = 10

# 最大里程
w = 100

truck_route = plan_truck_route(warehouses, v0, a, vs, w)
print(truck_route)
