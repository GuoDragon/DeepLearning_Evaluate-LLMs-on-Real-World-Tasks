# HYX 测试样例文档

**选题方向**：代码辅助类 — Python 代码调试  
**样例数量**：15 个（编号 01–15）  
**对应代码文件**：`test_codes/sample_XX_*.py`

---

## 样例总览

| 编号 | 文件名 | 错误类型 | 难度 | 期望能力 |
|------|--------|----------|------|----------|
| 01 | sample_01_syntax_missing_colon.py | 语法错误 | 简单 | 识别 if 缺少冒号 |
| 02 | sample_02_syntax_unmatched_paren.py | 语法错误 | 简单 | 识别括号不匹配 |
| 03 | sample_03_indentation_error.py | 语法错误 | 简单 | 识别缩进不一致 |
| 04 | sample_04_name_error.py | 运行时错误 | 简单 | 识别变量名拼写错误 |
| 05 | sample_05_type_error.py | 运行时错误 | 中等 | 识别类型不匹配 |
| 06 | sample_06_index_error.py | 运行时错误 | 中等 | 识别索引越界 |
| 07 | sample_07_key_error.py | 运行时错误 | 中等 | 识别字典键缺失 |
| 08 | sample_08_logic_off_by_one.py | 逻辑错误 | 中等 | 识别差一错误 |
| 09 | sample_09_logic_wrong_condition.py | 逻辑错误 | 较难 | 识别闰年判断规则 |
| 10 | sample_10_logic_factorial.py | 逻辑错误 | 中等 | 识别初始值错误 |
| 11 | sample_11_runtime_zero_division.py | 运行时错误 | 中等 | 识别除零风险 |
| 12 | sample_12_runtime_recursion.py | 运行时错误 | 中等 | 识别递归终止条件缺失 |
| 13 | sample_13_import_error.py | 运行时错误 | 简单 | 识别模块名拼写错误 |
| 14 | sample_14_performance_nested_loop.py | 性能问题 | 较难 | 识别 O(n²) 可优化为 O(n) |
| 15 | sample_15_performance_string_concat.py | 性能问题 | 较难 | 识别循环字符串拼接低效 |

---

## 各样例详细说明

### 样例 01 — 语法错误：if 缺少冒号

**错误描述**：`if n > 0` 后缺少冒号，Python 解析器报 `SyntaxError`。

**期望修复**：在 `if n > 0:` 后添加冒号。

**测试输入**：`check_positive(5)` 应返回 `True`。

---

### 样例 02 — 语法错误：括号不匹配

**错误描述**：`sum(numbers` 缺少右括号。

**期望修复**：补全 `sum(numbers)`。

---

### 样例 03 — 语法错误：缩进错误

**错误描述**：`print(message)` 缩进与函数体不一致，触发 `IndentationError`。

**期望修复**：统一使用 4 空格缩进。

---

### 样例 04 — NameError：变量拼写错误

**错误描述**：循环中累加至 `total`，返回时误写为 `totl`。

**期望修复**：将 `return totl` 改为 `return total`。

---

### 样例 05 — TypeError：字符串与整数拼接

**错误描述**：`result + item` 中 `item` 可能为 `int`，不能与 `str` 相加。

**期望修复**：使用 `str(item)` 转换，或按类型分别处理。

---

### 样例 06 — IndexError：索引越界

**错误描述**：`items[n]` 和 `items[n+1]` 在 `n=len(items)-1` 时越界。

**期望修复**：取最后三个元素应使用 `items[-3:]` 或正确边界检查。

---

### 样例 07 — KeyError：字典键不存在

**错误描述**：直接访问 `scores[name]`，当 `name` 不存在时抛出 KeyError。

**期望修复**：使用 `scores.get(name)` 或 `try/except`，并给出合理默认/提示。

---

### 样例 08 — 逻辑错误：差一错误

**错误描述**：`range(n)` 求和得到 0..n-1，而非 1..n。

**期望修复**：改为 `range(1, n + 1)` 或 `total += i + 1`（视题意而定，本样例期望 1..n）。

---

### 样例 09 — 逻辑错误：闰年判断不完整

**错误描述**：仅判断 `% 4 == 0`，1900 年会被误判为闰年。

**期望修复**：完整规则：能被 400 整除，或能被 4 整除但不能被 100 整除。

---

### 样例 10 — 逻辑错误：阶乘初始值

**错误描述**：`result = 0` 导致乘积恒为 0。

**期望修复**：`result = 1`。

---

### 样例 11 — 除零错误

**错误描述**：循环中 `numbers[i+1]` 可能为 0，导致 `ZeroDivisionError`。

**期望修复**：除法前检查分母是否为 0。

---

### 样例 12 — 无限递归

**错误描述**：`countdown` 无终止条件，导致 `RecursionError`。

**期望修复**：添加 `if n <= 0: return` 或类似 base case。

---

### 样例 13 — ImportError

**错误描述**：`import numppy` 模块名拼写错误。

**期望修复**：改为 `import numpy as np`（需已安装 numpy）。

---

### 样例 14 — 性能问题：嵌套循环查重

**错误描述**：O(n²) 双重循环判断重复，大数据量极慢。

**期望修复**：使用 `set` 或 `len(nums) != len(set(nums))`，复杂度 O(n)。

---

### 样例 15 — 性能问题：循环字符串拼接

**错误描述**：循环内 `report = report + line` 产生大量临时字符串，O(n²) 内存/时间。

**期望修复**：使用 `"\n".join(lines)` 或 list 收集后 join。

---

## 测试使用说明

1. 将 `test_codes/` 中对应文件内容填入 Prompt 的 `{code}` 占位符；
2. 对 5 种 LLM 分别使用 **基础 Prompt** 和 **改进 Prompt** 各测一遍；
3. 同一编号样例在所有模型间保持输入代码完全一致；
4. 原始输出保存至 `raw_outputs/basic/` 与 `raw_outputs/improved/`；
5. 评分标准见 `evaluation_scores.md`。
