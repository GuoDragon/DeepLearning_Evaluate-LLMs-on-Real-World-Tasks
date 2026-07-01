# 样例03：语法错误 - 缩进错误
def greet(name):
    message = "Hello, " + name
  print(message)  # 缩进与函数体不一致
    return message

greet("Alice")
