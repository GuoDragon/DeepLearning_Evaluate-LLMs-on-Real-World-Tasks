# Final Project 任务分工

## （一）HYX

### 1. 选题方向

**代码辅助类**

### 2. 步骤与注意事项

**步骤：**
1. 设计 10–20 个测试样例，包含不同类型的 Python 代码错误（语法错误、逻辑错误、运行时错误、性能问题等）；
2. 选择至少 5 种 LLM（如 GPT-4、Claude、Gemini、Qwen、DeepSeek）进行测试；
3. 设计基础 Prompt 和改进 Prompt；
4. 使用两类 Prompt 分别对所有模型执行测试；
5. 记录每个模型的输出结果；
6. 按评价指标（正确性、可运行性、鲁棒性、注释质量、是否引入不必要复杂度）进行评分；
7. 整理测试样例、Prompt、原始输出、评分结果，提交给 LCL 汇总。

**注意事项：**
- 记录每个模型的具体名称、版本、平台和使用日期；
- 同一选题下所有模型使用相同测试样例；
- 评分标准要客观一致；
- 保留完整原始记录。

### 3. 交付文件

- 测试样例文档：`topics/HYX/test_samples.md`
- Prompt 文件：`topics/HYX/basic_prompt.txt`、`topics/HYX/improved_prompt.txt`
- 实验原始记录：`topics/HYX/raw_outputs/`
- 评分结果：`topics/HYX/evaluation_scores.md`
- 代码文件：`topics/HYX/test_codes/`（测试用的错误代码示例）

---

## （二）PX

### 1. 选题方向

**学习辅助类**

### 2. 步骤与注意事项

**步骤：**
1. 设计 10–20 个测试样例，覆盖不同难度（简单/中等/较难）和类型（概念解释、机制理解、对比分析、数学解释、代码调试）；
2. 选择至少 5 种 LLM（如 GPT-4、Claude、Gemini、Qwen、DeepSeek）进行测试；
3. 设计基础 Prompt 和改进 Prompt；
4. 使用两类 Prompt 分别对所有模型执行测试；
5. 记录每个模型的输出结果；
6. 按评价指标（正确性、完整性、清晰度、可靠性、知识覆盖度）进行评分；
7. 整理测试样例、Prompt、原始输出、评分结果，提交给 LCL 汇总。

**注意事项：**
- 记录每个模型的具体名称、版本、平台和使用日期；
- 同一选题下所有模型使用相同测试样例；
- 评分标准要客观一致；
- 保留完整原始记录。

### 3. 交付文件

- 测试样例文档：`topics/PX/test_samples.md`
- Prompt 文件：`topics/PX/basic_prompt.txt`、`topics/PX/improved_prompt.txt`
- 实验原始记录：`topics/PX/raw_outputs/`
- 评分结果：`topics/PX/evaluation_scores.md`

---

## （三）LCL

### 1. 选题方向

**写作表达类**

### 2. 步骤与注意事项

**步骤：**
1. 设计 10–20 个测试样例，涵盖不同场景（求职邮件、商务沟通、学术咨询、日常交流等）和不同质量的原始邮件；
2. 选择至少 5 种 LLM（如 GPT-4、Claude、Gemini、Qwen、DeepSeek）进行测试；
3. 设计基础 Prompt 和改进 Prompt；
4. 使用两类 Prompt 分别对所有模型执行测试；
5. 记录每个模型的输出结果；
6. 按评价指标（语言流畅性、逻辑结构、表达准确性、是否符合目标场景、是否过度夸张）进行评分；
7. 整理测试样例、Prompt、原始输出、评分结果。

**注意事项：**
- 记录每个模型的具体名称、版本、平台和使用日期；
- 同一选题下所有模型使用相同测试样例；
- 评分标准要客观一致；
- 保留完整原始记录。

### 3. 交付文件

- 测试样例文档：`topics/LCL/test_samples.md`
- Prompt 文件：`topics/LCL/basic_prompt.txt`、`topics/LCL/improved_prompt.txt`
- 实验原始记录：`topics/LCL/raw_outputs/`
- 评分结果：`topics/LCL/evaluation_scores.md`

---

## （四）汇总与提交（LCL）

### 1. 汇总职责

整合三人的实验结果，撰写最终项目报告，规整仓库并提交。

### 2. 步骤与注意事项

**步骤：**
1. 收集 HYX、PX、LCL 三人的测试样例、Prompt、原始输出和评分结果；
2. 对比分析不同选题下各模型的表现差异；
3. 选取典型案例（最优、最差、差异明显、幻觉/错误、Prompt 改进前后对比）进行深度分析；
4. 编写最终项目报告 PDF，包含背景、分工、各选题 LLM 信息、测试样例、Prompt、评价指标、结果、案例分析、结论；
5. 规整 GitHub 仓库，编写 `.gitignore`，检查合规性；
6. 在小雅平台提交所有材料。

**注意事项：**
- 分析要深入，不流于表面；
- 报告需标注所有引用来源，若使用 LLM 辅助写作需说明；
- 仓库无无关文件，目录层级清晰；
- 提交前确认所有材料齐全，留存提交记录。

### 3. 交付文件

- 最终报告：`report/project_report.pdf`
- 案例分析：`analysis/case_analysis.md`
- 结果汇总表格：`results/summary_scores.md`（Markdown 表格）
- 仓库文件：`.gitignore`、规整后的完整 GitHub 仓库
- 交付成果：小雅平台提交记录（含 GitHub 仓库链接）

---

## 截止时间

**2026年7月5日**

---

**具体内容以小雅 PDF 为准**