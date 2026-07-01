# 样例07：运行时错误 - KeyError 字典键不存在
def get_student_grade(scores, name):
    return scores[name]

student_scores = {"Alice": 90, "Bob": 85}
print(get_student_grade(student_scores, "Charlie"))
