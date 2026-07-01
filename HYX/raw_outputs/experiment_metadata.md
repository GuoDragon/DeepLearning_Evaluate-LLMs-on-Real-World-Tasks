# HYX 实验原始记录 — 元数据

## 实验信息

| 项目 | 内容 |
|------|------|
| 选题 | Python 代码调试 |
| 测试样例数 | 15 |
| Prompt 类型 | 基础 Prompt / 改进 Prompt |
| 实验日期 | 2026-06-28 ~ 2026-06-30 |

## 使用的 LLM 及平台

| 序号 | 模型名称 | 版本/标识 | 平台 | 使用日期 |
|------|----------|-----------|------|----------|
| 1 | GPT-4o | gpt-4o-2024-08-06 | OpenAI ChatGPT (chat.openai.com) | 2026-06-28 |
| 2 | Claude 3.5 Sonnet | claude-3-5-sonnet-20241022 | Anthropic Claude (claude.ai) | 2026-06-28 |
| 3 | Gemini 2.0 Flash | gemini-2.0-flash | Google AI Studio (aistudio.google.com) | 2026-06-29 |
| 4 | Qwen2.5-72B-Instruct | qwen2.5-72b-instruct | 阿里云 DashScope / 通义千问 | 2026-06-29 |
| 5 | DeepSeek-V3 | deepseek-chat | DeepSeek 官网 (chat.deepseek.com) | 2026-06-30 |

## 文件目录说明

```
raw_outputs/
├── experiment_metadata.md    # 本文件
├── basic/                    # 使用基础 Prompt 的原始输出
│   ├── GPT-4o_outputs.md
│   ├── Claude-3.5-Sonnet_outputs.md
│   ├── Gemini-2.0-Flash_outputs.md
│   ├── Qwen2.5-72B_outputs.md
│   └── DeepSeek-V3_outputs.md
└── improved/                 # 使用改进 Prompt 的原始输出
    ├── GPT-4o_outputs.md
    ├── Claude-3.5-Sonnet_outputs.md
    ├── Gemini-2.0-Flash_outputs.md
    ├── Qwen2.5-72B_outputs.md
    └── DeepSeek-V3_outputs.md
```

## 实验流程

1. 从 `test_codes/` 读取 15 段错误代码；
2. 将代码嵌入 `basic_prompt.txt` 或 `improved_prompt.txt` 的 `{code}` 占位符；
3. 在同一平台、相同温度设置（默认）下依次向各模型提问；
4. 完整复制模型回复，不做人工修改；
5. 对修复后代码进行人工验证（语法检查 + 关键样例运行）。

## 备注

- 样例 13 修复后依赖 `numpy`，验证环境：Python 3.11，numpy 1.26.x
- 样例 14、15 为性能类问题，修复方案以算法/数据结构优化为主，功能输出应与原版一致
