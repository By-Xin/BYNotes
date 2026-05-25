---
title: "Post-Training and Forgetting"
aliases:
  - "Post-Training"
  - "Continual Learning"
  - "Catastrophic Forgetting"
  - "后训练"
  - "灾难性遗忘"
  - "持续学习"
  - "NLPAndLLMs/Training.Post-Training-and-Forgetting"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/llm-training
  - topic/post-training
---

> [!quote] References
> - Lecture: 李宏毅.

Post-training, or continual learning, 是指当下许多前沿大模型已经有非常强的基础能力, 我们希望通过微调其参数来在特定领域如医疗、法律或特定语言上进行更好适应.

习惯上, 将 post-training 前的模型称为 foundation model, post-training 之后的模型称为 fine-tuned model. 这里并不局限 pretraining 的模型是基础模型, 也可以是已经经过 alignment 后具备一定能力的模型. 只要是我们想在其上进行微调的模型, 都可以称为 post-training.

## 1. Methods of Post-Training

一般而言, post-training 方法可以分为三种方向.

### 1.1 Pretrain Style

直接通过搜集特定领域的文本数据, 进行预训练式文字接龙.

- 如果模型训练过分依赖这一方式, 可能会缺乏指令跟随能力.
- *Chat Vector: A Simple Approach to Equip LLMs with Instruction Following and Model Alignment in New Languages* 尝试使用 LLaMA-2-Chat 进行中文 post-training, 主要采用 pretrain style. 初步发现, 尽管模型中文生成能力提升, 但原本 alignment 能力明显下降. 这说明 post-training 过程可能导致模型遗忘原本能力, 也就是 forgetting.

### 1.2 SFT

SFT (Supervised Fine-Tuning) 通过搜集特定领域带有人类标注的文本数据, 构建明确的 input-output 组合进行有监督学习, 让模型学习在这种格式下生成目标答案.

- 关键用于提升模型可控性和指令响应性.
- *Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!* 使用 SFT 对模型微调, 实验发现即使对模型进行一些正常的 SFT 微调, 也会导致模型在一些安全性问题上出现问题.
- *Safeguard Fine-Tuned LLMs Through Pre- and Post-Tuning Model Merging* 在 Llama-3-8B-Instruct 上进行 SFT 微调, 发现微调后特定技能能力提升, 但原本能力如 safety alignment 明显下降.
- *Self-Distillation Bridges Distribution Gap in Language Model Fine-Tuning* 发现 post-training 增强了模型在 target task 上的能力, 但削弱了其他任务上的能力, 不只是安全性问题.

### 1.3 RL Style

通过强化学习, 如 PPO, DPO, RLAIF 等, 来优化模型输出偏好和质量, 基于人类反馈或评分. 这时的数据没有固定输出答案, 只有对模型输出内容好坏的评分.

- 存在多个候选输出, 系统根据偏好反馈, 如人类打分或 reward model, 更新策略.

## 2. Catastrophic Forgetting

当我们教模型一个对应任务而导致其他任务能力下降时, 这个现象称为 catastrophic forgetting.

- *An Empirical Study of Catastrophic Forgetting in LLMs During Continual Fine-Tuning* 在最高 8B 的模型上实验发现, 更大的模型并没有更好的抵抗遗忘能力.
- *Scaling Laws for Forgetting When Fine-Tuning LLMs* 提出模型学得越多, 遗忘程度越大.
- *LoRA Learns Less and Forgets Less* 发现如果使用 LoRA, 遗忘程度会更小, 但代价是模型学习能力不足.

为了解决 catastrophic forgetting, 可以尝试一些方法.

### 2.1 Experience Replay

一个经典方法是 **experience replay**, 即在微调新任务的过程中, 将之前任务的数据也加入当前训练数据.

在现代情景下, 一个问题是我们并不总能获取到之前任务的数据. 这时可以使用一些方法进行数据重建. 一个典型方法是让语言模型自己先生成旧有任务的数据, 然后再混合到新数据中进行训练. 这也称为 pseudo experience replay.

### 2.2 Paraphrase

让 foundation model 对人类给定的正确答案进行 **paraphrase** 得到一个新答案, 然后再利用这个答案进行训练. 其背后的思想是, 模型在 paraphrase 过程中可能会保留一些原本知识, 因此在微调过程中可能更好地避免遗忘.

### 2.3 Self-Output

**Self-output** 是让模型自己生成答案, 然后再利用这个答案进行训练. 此时往往训练的都是一些清晰的可分辨任务, 如数学和编程. 只要 foundation model 给出的答案正确, 那么这个答案就可以作为新的训练数据.

- 这个方法和 RL 方法很相像. 进行 RL 时, 我们也会让模型自己生成答案, 然后再利用这个答案进行训练. 这可能也是为什么我们往往会把 RL 放在模型训练最后一步的原因.
- 即使生成答案的 model 与微调的 model 不同, 这种 self-output 方法也可以有效避免遗忘. 而且这样的方法还能避免由于 foundation model 能力太弱而导致生成训练答案不够好的问题.
  - *I Learn Better If You Speak My Language* 对比人类提供答案、Claude 生成答案、GPT-4 生成答案, 发现语言模型生成的答案 post-training 效果要比人类提供答案好. 这里还提出 minimum change 方法, 即让 foundation model 生成答案, 然后让更高级模型如 GPT-4 仅对这个答案进行小修改以确保正确性, 再用这个答案训练.

## 3. Takeaway

在当前大语言模型中, 进行 post-training 以提高模型在某个领域的能力是一个重要方向. 但是除去关注其在特定领域的能力, 我们也要关注其习得这个能力时遗忘了多少原有能力.

一个 general 的思想是, 我们要用模型"自己的话"来进行训练, 这样会更好地避免遗忘.

## Related Notes

- [Pretraining and Alignment for LLMs](./Pretraining-and-Alignment-for-LLMs.md)
- [Deep Reasoning for LLMs](../Inference/Deep-Reasoning-for-LLMs.md)
- [Statistical Learning Algorithms: Transfer Learning planned note](../../StatisticalLearningAlgorithms/)
