# 样例15：性能问题 - 循环中字符串拼接效率低
def build_report(lines):
    report = ""
    for line in lines:
        report = report + line + "\n"  # 应使用 list + join
    return report

lines = [f"Line {i}: data" for i in range(50000)]
print(len(build_report(lines)))
