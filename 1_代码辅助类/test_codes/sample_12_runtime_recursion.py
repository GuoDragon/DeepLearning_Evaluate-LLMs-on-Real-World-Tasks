# 样例12：运行时错误 - 递归缺少/base case
def countdown(n):
    print(n)
    return countdown(n - 1)  # 缺少终止条件

countdown(5)
