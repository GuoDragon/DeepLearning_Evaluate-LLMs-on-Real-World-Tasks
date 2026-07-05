# 样例11：运行时错误 - 除零错误
def safe_divide(a, b):
    return a / b

numbers = [10, 5, 0, 2]
for i in range(len(numbers) - 1):
    print(safe_divide(numbers[i], numbers[i + 1]))
