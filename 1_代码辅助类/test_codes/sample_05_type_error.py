# 样例05：运行时错误 - TypeError 类型不匹配
def concatenate_items(items):
    result = ""
    for item in items:
        result = result + item  # item 可能是 int，不能与 str 拼接
    return result

data = ["a", "b", 3, "d"]
print(concatenate_items(data))
