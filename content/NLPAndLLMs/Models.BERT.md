---
title: "BERT"
aliases:
  - "Bidirectional Encoder Representations from Transformers"
  - "双向编码器表示"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/pretrained-models
  - topic/embeddings
---

> [!quote] References
> - Lecture: 李宏毅, 机器学习 2021.
> - Code Reference: [NVIDIA DeepLearningExamples BERT](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/LanguageModeling/BERT).

## 1. Intuitive Understanding of BERT from Applications

### 1.1 Core Function: Language Understanding

BERT (Bidirectional Encoder Representations from Transformers) 是 Google 在 2018 年推出的基于 Transformer 架构的自然语言处理模型. BERT 的本质是一个**语言理解模型**, 核心是**学习文本的深层语义信息表示**.

BERT 模型的输入是一个经过基本处理的文本序列, 主要包括分词和位置编码等. 其最基本的输出是对于每个 token 的一个高维向量表示. 简单地说, input 是文本序列, output 是文本序列中每个 token 的数学向量表示.

BERT 能够完成许多下游 NLP 任务, 如文本分类、问答、命名实体识别等. 不过这些任务并不是 BERT 本身直接完成的. BERT 本身只是一个语言理解模型, 核心是学习文本的深度语义表示. 为了完成具体的 NLP 任务, 我们在 BERT 之上加一层额外的任务特定层 (Head), 然后进行 fine-tuning.

### 1.2 BERT vs Word2Vec and GloVe

从表象上看, BERT 和传统词向量模型如 Word2Vec, GloVe 都是将文本转换为向量表示. 不过在原理和表达能力上, BERT 和传统词向量模型有很大区别.

**Word2Vec.**

- Word2Vec 是基于相对简单的神经网络模型, 主要是通过训练一个浅层神经网络来学习词的向量表示.
- 词的向量表示是静态的, 即对于同一个词, 其在不同上下文中的表示是相同的.
- 无法区分同一个词在不同上下文中的含义, 如 "bank" 在 "bank account" 和 "river bank" 中分别表示银行和河岸.
- 其训练基于词的共现信息, 主要适用于词级别任务, 如词相似度和词聚类.
- 优点是计算成本较低, 训练后存储的词向量较小, 计算效率高.

**BERT.**

- BERT 是基于深度 Transformer 模型的, 具有更强的表达能力.
- 词的向量表示是动态的, 即同一个词在不同上下文中的表示是不同的.
- BERT 可以更好地处理语境依赖和歧义词, 适用于文本分类、情感分析、阅读理解等下游任务.
- 缺点是计算成本高, 预训练时需要大规模 Transformer 模型, 参数量巨大, 如 BERT-Base 110M and BERT-Large 340M.

总而言之, 如果任务仅需要静态词向量, 如词相似度和聚类, Word2Vec 是一个更轻量的选择. 如果任务需要理解上下文, 如文本分类、情感分析、阅读理解, BERT 及其变体如 RoBERTa, ALBERT 会有更好的效果.

## 2. Pre-training: How BERT Learns Semantic Understanding

### 2.1 Model Structure

BERT 模型的输入是一串序列, 常为一串 token, 输出也是一串序列, 每个 token 对应一个向量表示, 且二者之间是一一对应的. 输入序列有多长, 输出序列也有多长.

具体而言, BERT 的模型结构是一个基于 Transformer 的深度神经网络. Generally, Transformer 可以分为 Encoder 和 Decoder 两部分, 而 BERT 只使用 Transformer 的 Encoder 部分.

BERT 相当于将多个 Transformer Encoder 串联在一起, 通过多层 Transformer Encoder 来学习文本的深层语义信息.

### 2.2 Self-Supervised Learning in BERT

#### 2.2.1 Self-Supervised Learning

Self-supervised learning 是 BERT 的核心训练方法.

- 传统 supervised learning 在训练时数据包括 feature $X$ 和 label $Y$, 模型通过训练得到 $\hat{Y} = \text{model}(X)$, 使得 $\hat{Y}$ 尽可能接近 $Y$.
- 对于 self-supervised learning, 数据中没有 label $Y$, 我们需要一些方法自己生成 label, 再通过模型训练来预测这个 label.

#### 2.2.2 Random Token Masking

BERT 对一串给定语料学习的核心方法之一是 **Random Token Masking**.

Random token masking 是指面对一串文本序列时, 随机将其中一些 token mask 掉, 然后让模型预测这些被遮盖的 token. 具体的 mask 可能是直接将 token 替换为特殊 token `[MASK]`, 也可能是将选取的 token 替换为另一个随机 token.

对于 BERT 模型, 即使 input 出现 mask token, 其也会输出同样序列长度的 output. 因此我们定位到 mask token 的位置, 通过线性变换和 softmax 等操作, 将模型预测出的数学向量还原为具体 token, 并将预测结果与该位置真实 token 比较, 通过交叉熵损失函数计算预测误差并训练模型.

#### 2.2.3 Next Sentence Prediction

除了 random token masking, BERT 还使用 **Next Sentence Prediction** 来训练模型. 训练时, BERT 会随机从语料库中选取两个句子, 然后让模型判断这两个句子是否连续.

对于两个句子, 我们会用特殊 token `[CLS]` 标记句子的开始, 用 `[SEP]` 标记每个单句的结束. BERT 输出同样长度的序列, 但这里我们只关注最开始的 `[CLS]` token 对应的输出结果. 我们希望模型在这个位置输出 YES/NO 的二分类结果, 判断给定两个句子是否连续.

也有一些质疑认为 Next Sentence Prediction 对模型训练效果不大. 例如:

- Robustly optimized BERT approach (RoBERTa): <https://arxiv.org/abs/1907.11692>
- Sentence Order Prediction (SOP): <https://arxiv.org/abs/1902.00751>

SOP 会将两个相邻句子随机打乱顺序, 让模型判断两个句子的顺序.

## 3. Fine-tuning BERT for Downstream Tasks

通过 random token masking 和 next sentence prediction pre-train BERT 后, BERT 具有了基本的语义理解能力.

为了完成具体的 NLP downstream tasks, 我们需要在 BERT 之上加一层额外的 task-specific head, 然后进行 fine-tuning. Fine-tuning 时不再使用 random token masking 和 next sentence prediction, 而是直接使用下游任务的数据集进行有监督训练.

### 3.1 Sequence to Classification

Sequence to classification 的输入是一个文本序列, 输出是一个分类结果. 常见任务包括文本分类、情感分析等. 实现方式是在 BERT 之上加一个 fully connected layer 进行分类. 我们主要关注第一个 token `[CLS]` 的输出结果, 然后通过全连接层分类, 并与真实 label 比较, 通过交叉熵损失函数训练.

### 3.2 Sequence to Sequence with Same Length

Seq2Seq 任务的输入是一个文本序列, 输出也是一个文本序列, 且特别要求输入和输出序列长度相同. 常见任务有 POS tagging. 这里可以直接使用 BERT 将每个 token 对应到一个向量表示, 然后将该向量输入全连接层, 预测每个 token 的标签.

### 3.3 Two Sequences to Classification

Two-sequences to classification 的输入是两个文本序列, 输出是一个分类结果. 常见任务有 NLI (Natural Language Inference). 在 NLI 中, 我们需要判断两个句子之间的逻辑关系, 通常有 entailment, neutral, contradiction 三种关系.

对于 BERT, 我们可以将两个句子的 token 序列拼接在一起, 然后通过一个全连接层, 根据 `[CLS]` token 的输出来分类.

### 3.4 Extractive Question Answering

Extractive question answering 的输入是一个文本序列 $D$ 和一个基于该文本的问题 $Q$. 模型输出两个 token 索引 $(s,e)$, 表示针对问题 $Q$ 在文本 $D$ 中答案的起始和结束位置.

例如文本 "The capital of France is Paris." 和问题 "What is the capital of France?" 的答案是 $(4,5)$, 即 "Paris".

## 4. Initial Use of BERT in Hugging Face

Hugging Face 的 `transformers` library 提供了简单易用的 API, 可以快速加载 BERT 并应用到各种 NLP 任务. 一个简单流程如下.

### 4.1 Install `transformers`

```bash
pip install transformers torch
```

### 4.2 Load a Pretrained BERT Model

```python
from transformers import BertTokenizer, BertModel

# Load BERT tokenizer and model.
# bert-base-uncased is case-insensitive and suitable for English.
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Test text
text = "BERT is a powerful model for NLP tasks."

# Tokenize and convert to tensors
inputs = tokenizer(text, return_tensors="pt")

# Get BERT outputs
outputs = model(**inputs)

# Get the last hidden states.
# Shape: (batch_size, sequence_length, hidden_size)
last_hidden_states = outputs.last_hidden_state
print(last_hidden_states.shape)  # torch.Size([1, token_length, 768])
```

### 4.3 Get Token Embeddings

```python
# Get the vector representation of token i
token_i = 2
word_embedding = last_hidden_states[:, token_i, :]
print(word_embedding.shape)
print(word_embedding)
```

Further, we can use classes such as `BertForSequenceClassification` to call BERT models that are already pretrained and fine-tuned for specific NLP tasks. We can also add task-specific layers on top of a pretrained BERT model.

## Related Notes

- [Word Embeddings](./Embeddings.Word-Embeddings.md)
- [Word2Vec](./Embeddings.Word2Vec.md)
- [GloVe](./Embeddings.GloVe.md)
- [Pretraining and Alignment for LLMs](./Training.Pretraining-and-Alignment-for-LLMs.md)
