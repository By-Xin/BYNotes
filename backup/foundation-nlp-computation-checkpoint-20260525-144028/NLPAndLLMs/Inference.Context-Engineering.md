---
title: "Context Engineering"
aliases:
  - "Prompt Engineering"
  - "In-Context Learning"
  - "ICL"
  - "上下文工程"
  - "提示工程"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/llm-inference
  - topic/context-engineering
---

> [!quote] References
> - Lecture: 李宏毅.
> - Video: <https://www.youtube.com/watch?v=lVdajtNpaGI>
> - Reference: Anthropic Claude system prompt.

## 1. Introduction

### 1.1 What Is Context Engineering?

总的而言, 语言模型可以认为是一个 next-token predictor. 给定输入 $x_t$, 语言模型 $f_{\text{LM}}$ 会输出下一个 token 的概率分布:

$$
f_{\text{LM}}(x) = \mathbb{P}(x_{t+1}|x_t).
$$

当我们的输出 $f_{\text{LM}}(x)$ 不是想要的, 有如下几种方式来调整输出:

- 调整模型参数, 即学习 $f_{\text{LM}}$. 在 LM 中通常包括 fine-tuning, LoRA, PEFT 等方法.
- 调整输入上下文 $x_t$ 而不是模型本身. 这就是 context engineering. 其不涉及任何模型训练.

### 1.2 Context Engineering vs Prompt Engineering

二者本质上基本相同, 只不过关注细节可能不太一样.

- **Prompt Engineering**: 更关注 prompt 格式设计、"神奇咒语", 例如 "let's think step by step", 以让模型更好地理解任务. 不过随着技术发展, 这类 prompt 设计带来的提升越来越有限.
- **Context Engineering**: 当单纯 prompt 设计不能满足需求时, 希望通过更自动化的上下文管理来提升模型能力.

## 2. What Should Be in the Context?

Context 一般包括如下几类信息.

### 2.1 User Prompt

User prompt 提供前提、任务范例等:

- 任务说明. 例如: "写一封给老板的请假邮件".
- 详细指引. 例如: "开头先道歉, 然后说明请假原因, 最后表达感谢".
- 额外条件. 例如: "100 字以内".
- 输出风格. 例如: "正式, 幽默".

### 2.2 System Prompt

System prompt 由开发人员提供, 在每次进行对话时提供给语言模型的上下文信息.

Claude Opus 4.1 公开了其 system prompt:

<https://docs.anthropic.com/en/release-notes/system-prompts#august-5-2025>

部分摘录如下:

```text
The assistant is Claude, created by Anthropic.
The current date is {{currentDateTime}}.
Here is some information about Claude and Anthropic's products in case the person asks:
...
```

该版本的 system prompt 一共超过 2000 字, 包含信息众多:

- 基本身份与产品咨询.
- 使用说明与限制.
- 互动态度与使用者回馈.
- 安全与禁止事项.
- 回应风格与格式.
- 知识与事实性.
- 自我定位与哲学原则, e.g. Claude does not claim to be human or conscious.
- 错误处理与互动细节, e.g. if corrected, Claude first thinks carefully before acknowledging.

### 2.3 Dialogue History

Dialogue history 相当于模型的短期记忆.

### 2.4 Long-Term Memory

OpenAI 在 2024 年 9 月的更新支持了 ChatGPT 的长期记忆功能.

通过 prompt 提供任务相关的信息, 让模型更好地理解任务范式, 也称为 in-context learning. 这种方式没有任何模型参数更新.

## Related Notes

- [Deep Reasoning for LLMs](./Inference.Deep-Reasoning-for-LLMs.md)
- [Uncertainty in LLMs](./Inference.Uncertainty-in-LLMs.md)
- [Pretraining and Alignment for LLMs](./Training.Pretraining-and-Alignment-for-LLMs.md)
- [Post-Training and Forgetting](./Training.Post-Training-and-Forgetting.md)
