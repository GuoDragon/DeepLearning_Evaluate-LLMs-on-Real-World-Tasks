# 样例06：运行时错误 - IndexError 索引越界
def get_last_three(items):
    n = len(items)
    return [items[n - 1], items[n], items[n + 1]]

print(get_last_three([1, 2, 3]))
