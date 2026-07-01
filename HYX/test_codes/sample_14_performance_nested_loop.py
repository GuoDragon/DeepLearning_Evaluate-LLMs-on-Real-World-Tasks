# 样例14：性能问题 - 不必要的嵌套循环查找重复
def has_duplicate(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                return True
    return False

print(has_duplicate(list(range(10000)) + [9999]))
