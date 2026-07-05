# 样例10：逻辑错误 - 阶乘计算错误
def factorial(n):
    result = 0  # 初始值应为 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 期望 120
