---
title: "Word Embeddings"
aliases:
  - "Word Embeddings 词向量"
  - "词向量"
  - "词嵌入"
  - "Word_Embeddings"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/embeddings
---

词嵌入: 将词映射到连续向量空间的表示学习方法.

## 1. Core Problem

NLP 的首要问题是**如何表示词**.

### 1.1 Traditional Method: One-Hot Encoding

- 每个词是一个维度为 $V$ 的向量, 其中 $V$ 为词汇表大小.
- 表示是**离散的、稀疏的**.
- 缺点: 词与词之间都是正交的, 无法表示相似性.

### 1.2 Modern Method: Word Embeddings

- 将每个词映射到一个**连续的低维向量空间**.
- 语义相近的词在空间中距离也相近.
- 将**高维稀疏**表示转化为**低维稠密**表示.

## 2. Mathematical Representation

给定词嵌入矩阵 $U \in \mathbb{R}^{V \times d}$:

- $V$ = 词汇表大小.
- $d$ = 词向量维度, 是超参数, 常取 $100$ 到 $300$.
- 第 $i$ 行 $u_i$ 表示第 $i$ 个词的向量.

对于 one-hot 表示的句子 $X \in \mathbb{R}^{V \times T}$, 其中 $T$ 是句子长度, 词向量表示为:

$$
X^\top U \in \mathbb{R}^{T \times d}.
$$

## 3. Method Categories

| 方法类型 | 代表模型 | 核心思想 | 优缺点 |
|----------|----------|----------|--------|
| **Prediction-based** | [Word2Vec](./Embeddings.Word2Vec.md) | 通过预测上下文学习词向量 | 捕捉语义关系, 但无全局信息 |
| **Count-based** | LSA, [GloVe](./Embeddings.GloVe.md) | 基于共现矩阵学习词向量 | 利用全局信息, 但计算复杂 |
| **Contextual** | [BERT](./Models.BERT.md), ELMo | 动态词向量, 依赖上下文 | 消歧能力强, 但计算成本高 |

## 4. Notes Index

| Note | Key Concepts |
|------|--------------|
| [Word2Vec](./Embeddings.Word2Vec.md) | Skip-gram, CBOW, neural network perspective, PyTorch implementation |
| [Negative Sampling](./Embeddings.Negative-Sampling.md) | Sampling distribution, binary approximation |
| [GloVe](./Embeddings.GloVe.md) | Co-occurrence matrix, PMI, global vectors |

## 5. Concept Map

```text
Word Embeddings
  |
  |-- Word2Vec (Prediction-based)
  |     |-- Negative Sampling (optimization)
  |
  |-- GloVe (Count-based)
  |
  |-- BERT (Contextual embeddings)
```

## Related Notes

- [BERT](./Models.BERT.md)
- [Word2Vec](./Embeddings.Word2Vec.md)
- [GloVe](./Embeddings.GloVe.md)
- [Negative Sampling](./Embeddings.Negative-Sampling.md)
