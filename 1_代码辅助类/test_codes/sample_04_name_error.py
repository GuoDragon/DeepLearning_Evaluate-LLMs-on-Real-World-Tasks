# 样例04：运行时错误 - NameError 未定义变量
def compute_total(prices):
    total = 0
    for price in prices:
        total += price
    return totl  # 拼写错误，应为 total

print(compute_total([10, 20, 30]))
