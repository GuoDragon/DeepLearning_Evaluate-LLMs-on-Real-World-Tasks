## 一、基础Prompt

### 样例1：基础概念-过拟合与欠拟合（简单）
请用本科生能够理解的方式解释过拟合和欠拟合的区别，并各举一个简单例子。

### 样例2：基础概念-梯度下降与反向传播（简单）
请解释梯度下降和反向传播分别是什么，它们在神经网络训练中有什么关系。

### 样例3：机制理解-Batch Normalization（中等）
请解释为什么 Batch Normalization 可以加速神经网络训练，并说明它对训练稳定性的影响。

### 样例4：对比分析-CNN、RNN 与 Transformer（中等）
请比较 CNN、RNN 和 Transformer 的主要特点、适用场景和局限性。

### 样例5：数学解释-Attention 中的 Query、Key、Value（中等）
请解释 Attention 机制中 Query、Key 和 Value 的含义，并说明它们如何共同计算注意力结果。

### 样例6：数学解释-Softmax 与交叉熵损失（中等）
请解释多分类任务中 Softmax 函数和交叉熵损失的作用，并说明为什么它们经常一起使用。

### 样例7：代码调试-PyTorch 维度不匹配（较难）
请指出下面 PyTorch 代码中的错误原因，并给出修改建议。
```python
import torch
import torch.nn as nn

x = torch.randn(32, 28, 28)
model = nn.Linear(784, 10)
y = model(x)
print(y.shape)
```

### 样例8：代码调试-训练循环问题（较难）
请找出下面训练循环中可能导致训练效果异常的问题，并说明如何修改。
```python
for epoch in range(5):
    for x, y in train_loader:
        pred = model(x)
        loss = criterion(pred, y)
        loss.backward()
        optimizer.step()
```

### 样例9：复习整理-深度学习知识提纲（较难）
请根据以下课堂笔记生成一份适合考前复习的提纲。
课堂笔记：本章讲了神经网络训练中的优化与正则化。优化方法包括 SGD、Momentum、Adam。正则化方法包括 L2 正则化、Dropout、数据增强和 Early Stopping。还提到了学习率对训练收敛速度和最终效果的影响。

### 样例10：论文阅读辅助-英文摘要理解（较难）
请用中文解释下面英文论文摘要片段的核心意思，并说明其中涉及的深度学习概念。
Abstract excerpt: We propose a transformer-based architecture for image classification. By replacing convolutional inductive biases with self-attention mechanisms, the model captures long-range dependencies between image patches. Experiments show improved performance on large-scale datasets, but the approach requires substantial computational resources during training.

---

## 二、改进Prompt

### 样例1：基础概念-过拟合与欠拟合
你是一名深度学习课程助教，请面向刚入门的本科生解释“过拟合”和“欠拟合”。要求：
1. 先分别给出两个概念的核心定义；
2. 用一个直观生活类比帮助理解；
3. 分别说明它们在训练集和测试集上的典型表现；
4. 各给出至少两种常见解决方法；
5. 避免使用过多术语，如使用术语需简短解释。
问题：过拟合和欠拟合有什么区别？

### 样例2：基础概念-梯度下降与反向传播
你是一名深度学习课程助教，请解释“梯度下降”和“反向传播”的区别与联系。请按照以下结构回答：
1. 一句话概括二者各自的作用；
2. 分别解释梯度下降和反向传播的基本流程；
3. 说明二者在一次神经网络训练迭代中的先后关系；
4. 用一个简单比喻说明“计算梯度”和“更新参数”的区别；
5. 列出初学者常见误区。
要求：面向本科生，语言清楚，不要把两者混为一谈。

### 样例3：机制理解-Batch Normalization
你是一名深度学习课程助教，请解释 Batch Normalization 为什么有助于训练。请按以下格式回答：
1. 核心结论；
2. Batch Normalization 在每个 mini-batch 中做了什么；
3. 它如何影响梯度传播、学习率选择和训练稳定性；
4. 训练阶段和推理阶段的差异；
5. 一个常见误区或使用注意事项。
要求：不要只说“减少内部协变量偏移”，需要给出本科生可以理解的直观解释。

### 样例4：对比分析-CNN、RNN 与 Transformer
你是一名深度学习课程助教，请比较 CNN、RNN 和 Transformer。请用 Markdown 表格回答，并包含以下列：
1. 模型类型；
2. 核心思想；
3. 擅长处理的数据；
4. 典型应用场景；
5. 主要优点；
6. 主要局限。
表格后请再用 3-5 句话总结：如果面对图像分类、时间序列预测、机器翻译任务，通常应优先考虑哪类模型以及原因。

### 样例5：数学解释-Attention 中的 Query、Key、Value
你是一名深度学习课程助教，请解释 Attention 机制中的 Query、Key、Value。要求：
1. 先用直观类比解释 Q、K、V 分别代表什么；
2. 给出缩放点积注意力公式：softmax(QK^T / sqrt(d_k))V；
3. 解释公式中每一项的含义，包括 d_k 的作用；
4. 用一个简短例子说明“根据 Query 找相关 Key，再汇总 Value”的过程；
5. 说明初学者容易混淆的地方。
要求：公式解释要准确，但不要过度推导。

### 样例6：数学解释-Softmax 与交叉熵损失
你是一名深度学习课程助教，请解释多分类任务中的 Softmax 和交叉熵损失。请按照以下结构回答：
1. Softmax 的输入和输出分别是什么；
2. 交叉熵损失衡量的是什么；
3. 为什么二者常被组合用于多分类；
4. 用一个三分类的简单数值例子说明预测概率和真实标签如何产生损失；
5. 说明模型“置信度高但预测错误”时损失为什么会很大。
要求：面向本科生，公式可以出现，但必须解释符号含义。

### 样例7：代码调试-PyTorch 维度不匹配
你是一名 PyTorch 助教，请调试下面代码。请按以下格式回答：
1. 报错或潜在问题的位置；
2. 张量 x 当前形状与 nn.Linear 期望输入形状；
3. 最小修改方案；
4. 修改后的完整可运行代码；
5. 为什么这样修改是正确的。
代码：
```python
import torch
import torch.nn as nn

x = torch.randn(32, 28, 28)
model = nn.Linear(784, 10)
y = model(x)
print(y.shape)
```
要求：不要引入不必要的复杂模型，只修复当前维度问题。

### 样例8：代码调试-训练循环问题
你是一名 PyTorch 助教，请检查下面训练循环是否存在问题。请按以下格式回答：
1. 主要错误或遗漏；
2. 为什么该问题会影响训练；
3. 修改后的训练循环代码；
4. 如有必要，补充 model.train()、device 转移等建议，但请区分“必须修改”和“可选改进”。
代码：
```python
for epoch in range(5):
    for x, y in train_loader:
        pred = model(x)
        loss = criterion(pred, y)
        loss.backward()
        optimizer.step()
```
要求：重点检查梯度清零、反向传播和参数更新流程，不要编造 train_loader 或模型细节。

### 样例9：复习整理-深度学习知识提纲
你是一名深度学习课程助教，请根据课堂笔记整理考前复习提纲。要求：
1. 按“优化方法”“正则化方法”“学习率影响”“易混淆概念”四个部分组织；
2. 每个知识点写出一句核心解释；
3. 标出至少 5 个可能的考试提问角度；
4. 不要补充课堂笔记中完全没有出现的章节内容；
5. 最后给出一段 3 句话以内的复习建议。
课堂笔记：本章讲了神经网络训练中的优化与正则化。优化方法包括 SGD、Momentum、Adam。正则化方法包括 L2 正则化、Dropout、数据增强和 Early Stopping。还提到了学习率对训练收敛速度和最终效果的影响。

### 样例10：论文阅读辅助-英文摘要理解
你是一名深度学习课程助教，请帮助本科生理解下面英文论文摘要片段。请按以下结构用中文回答：
1. 摘要核心内容概括，不超过 100 字；
2. 逐句解释原文含义；
3. 解释其中的关键概念：Transformer、self-attention、convolutional inductive bias、long-range dependencies、image patches；
4. 说明该方法的优势和代价；
5. 明确指出哪些信息来自原文，哪些是为了帮助理解而补充的背景解释。
Abstract excerpt: We propose a transformer-based architecture for image classification. By replacing convolutional inductive biases with self-attention mechanisms, the model captures long-range dependencies between image patches. Experiments show improved performance on large-scale datasets, but the approach requires substantial computational resources during training.