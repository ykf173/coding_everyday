# 2023328   20230318
# 合理，计算时间差
# 前>后
# 好未来

month_dict = {
    1: 31,
    3: 31,
    5: 31,
    7: 31,
    8: 31,
    10: 31,
    12: 31,
    4: 30,
    6: 30,
    9: 30,
    11: 30,
    2: 28,
}

def coun_time(year1, year2, month1, month2, day1, day2):
    year_time = month_time = day_time = 0
    if month1 >= month2:
        year_time = (year1 - year2) * 365
        month_time = sum([month_dict[mon] for mon in range(month2, month1)])
        if day1 >= day2:
            day_time = day1 - day2
        else:
            day_time = day1 - day2


    else:
        for mon in range(1, month2):
            month_time += month_dict[mon]
        for mon in range(12, month1, -1):
            month_time += month_dict[mon]






    return year_time + month_time + day_time
