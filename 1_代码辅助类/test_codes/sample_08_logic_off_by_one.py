# 样例08：逻辑错误 - 差一错误（off-by-one）
def sum_first_n(n):
    total = 0
    for i in range(n):  # 应使用 range(1, n + 1) 才能求 1..n 之和
        total += i
    return total

print(sum_first_n(5))  # 期望 15，实际 10
