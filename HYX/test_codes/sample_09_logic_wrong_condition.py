# 样例09：逻辑错误 - 条件判断错误
def is_leap_year(year):
    if year % 4 == 0:  # 未考虑 century 规则
        return True
    return False

print(is_leap_year(1900))  # 期望 False，实际 True
