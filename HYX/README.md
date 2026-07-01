# Final Project — HYX 部分（Python 代码调试）

本目录为 **HYX** 负责的「代码辅助类：Python 代码调试」实验交付物，供 LCL 汇总至最终报告。

## 目录结构

```
topics/HYX/
├── test_samples.md          # 15 个测试样例说明
├── basic_prompt.txt         # 基础 Prompt 模板
├── improved_prompt.txt      # 改进 Prompt 模板
├── evaluation_scores.md     # 评分结果与分析
├── test_codes/              # 15 个含错误的 Python 样例
│   ├── sample_01_syntax_missing_colon.py
│   ├── ...
│   └── sample_15_performance_string_concat.py
└── raw_outputs/             # 实验原始记录
    ├── experiment_metadata.md
    ├── basic/               # 5 模型 × 基础 Prompt
    └── improved/            # 5 模型 × 改进 Prompt
```

## 测试 LLM

| 模型 | 平台 | 日期 |
|------|------|------|
| GPT-4o | OpenAI ChatGPT | 2026-06-28 |
| Claude 3.5 Sonnet | Anthropic Claude | 2026-06-28 |
| Gemini 2.0 Flash | Google AI Studio | 2026-06-29 |
| Qwen2.5-72B-Instruct | 阿里云 DashScope | 2026-06-29 |
| DeepSeek-V3 | DeepSeek Chat | 2026-06-30 |

## 评价指标

正确性、可运行性、鲁棒性、注释质量、简洁性（1–5 分），详见 `evaluation_scores.md`。

## 复现实验

1. 打开 `test_codes/` 中任一样例；
2. 将代码粘贴进 `basic_prompt.txt` 或 `improved_prompt.txt` 的 `{code}` 位置；
3. 在对应 LLM 平台发送完整 Prompt；
4. 将输出保存至 `raw_outputs/` 对应目录。

## 提交给 LCL 的文件清单

- [x] `test_samples.md`
- [x] `basic_prompt.txt` / `improved_prompt.txt`
- [x] `raw_outputs/`（含 10 个模型输出文件 + 元数据）
- [x] `evaluation_scores.md`
- [x] `test_codes/`（15 个 `.py` 文件）
