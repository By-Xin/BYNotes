---
title: "N-Gram Language Models"
aliases:
  - "Language Models"
  - "语言模型"
  - "N-gram"
  - "语言建模"
  - "N-Gram Language Model"
  - "NLPAndLLMs/Models.N-Gram-Language-Models"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/language-models
---

> [!quote] References
> - Lecture: CS224N.

## 1. Introduction

直观上的理解, language model 是一个用来预测下一个词的模型. 形式上, 若给定一个句子 $w_1, w_2, ..., w_{i-1}$, 则 language model 的目标是预测下一个词 $w_i$ 应该是 $\mathcal{V} = \{w_1, w_2, ..., w_{|V|}\}$ 中的哪一个. 这种选择可以建模为:

$$
\mathbb{P}(w_i | w_1, w_2, ..., w_{i-1}).
$$

更广义地讲, language model 的目标是从 $0$ 开始预测整个句子的概率分布, 即尝试预测整个序列 $w_1, w_2, ..., w_m$ 的联合概率分布:

$$
\begin{aligned}
\mathbb{P}(w_1, w_2, \cdots, w_m)
&= \mathbb{P}(w_1) \mathbb{P}(w_2 | w_1) \mathbb{P}(w_3 | w_1, w_2) \cdots \mathbb{P}(w_m | w_1, w_2, \cdots, w_{m-1}) \\
&= \prod_{i=1}^{m} \mathbb{P}(w_i | w_1, w_2, \cdots, w_{i-1}).
\end{aligned}
$$

Language model 的研究就在于如何精准地估计这些概率分布.

## 2. N-Gram Language Model

### 2.1 Theory

在深度学习方法流行之前, 一种常见的方法是使用 n-gram 模型来估计这个概率分布:

$$
\begin{aligned}
\mathbb{P}(w_1, w_2, \cdots, w_m)
&= \prod_{i=1}^{m} \mathbb{P}(w_i | w_1, w_2, \cdots, w_{i-1}).
\end{aligned}
$$

对于 n-gram 模型, 一个重要假设是 Markov 假设, 即假设当前词的预测只依赖于前面最接近的 $n$ 个词, 而不是需要依赖整个历史. 这样, 上述概率分布可以近似为:

$$
\begin{aligned}
\mathbb{P}(w_1, w_2, \cdots, w_m)
&\approx \prod_{i=1}^{m} \mathbb{P}(w_i | w_{i-n+1}, w_{i-n+2}, \cdots, w_{i-1}).
\end{aligned}
$$

注意, n-gram 本身指的是长度为 $n$ 个词的语段. 在 Markov 条件下, 我们实际上是用前 $n-1$ 个词来预测第 $n$ 个词:

$$
\begin{aligned}
\mathbb{P}(w_{t+1} | w_{t}, w_{t-1}, \cdots, w_{t-n+2})
= \frac{\mathbb{P}(w_{t+1}, w_{t}, w_{t-1}, \cdots, w_{t-n+2})}{\mathbb{P}(w_{t}, w_{t-1}, \cdots, w_{t-n+2})}.
\end{aligned}
$$

对右侧概率分布的一种常见估计就是用频率代替概率:

$$
\begin{aligned}
\mathbb{P}(w_{t+1} | w_{t}, w_{t-1}, \cdots, w_{t-n+2})
\approx
\frac{\text{count}(w_{t+1}, w_{t}, w_{t-1}, \cdots, w_{t-n+2})}{\text{count}(w_{t}, w_{t-1}, \cdots, w_{t-n+2})}.
\end{aligned}
$$

其本质上就是在统计语料库中某种语段出现的频率, 用最频繁出现的语段来作为预测依据.

当然在求出其概率分布后, 我们既可以固定选择最大概率的词, 也可以以这个概率作为权重来进行随机抽样, 增加模型的多样性.

### 2.2 Practical Tradeoffs

实践中, 我们经常会遇到一个 $n$ 选择的权衡问题. 例如考虑句子: *As the proctor started the clock, the students opened their ( )*. 若 $n$ 长度不足, 则很有可能忽略掉关键信息 *proctor*. 但是另一方面, 若 $n$ 太长, 则很有可能会遇到数据稀疏的问题, 例如很难在语料库中找到连续 $20$ 个词都相同的语段.

因此 n-gram 模型经常会面临两个问题:

- **Sparsity problem**: 数据稀疏问题, 即很多语段在语料库中没有出现过, 从而导致概率分布估计不准确. 通常这种问题是由于 $n$ 过大造成的. 经验而言, 适宜范围为 $n\leq 5$.
  - 若 $w_1, w_2, w_3$ 从未一起在语料库中出现过, 则 $\text{count}(w_{1}, w_{2}, w_{3}) = 0$, 从而导致概率估计为 $0$. 一种直接的解决方法是使用 Laplace smoothing, 即在分子分母上都加上一个小量 $\delta$.
  - 若 $w_1, w_2$ 组合都没有在语料库中出现过, 则 $\text{count}(w_{1}, w_{2}) = 0$, 从而导致概率估计的分母为 $0$. 一种解决方法是使用 back-off, 降低 $n$ 的长度.
- **Storage problem**: n-gram 模型需要存储语料库中的所有 n-gram 语段, 因此当 $n$ 较大或语料库较大时, 会导致存储空间问题.

## Related Notes

- [Word Embeddings](../Embeddings/Word-Embeddings.md)
- [BERT](./BERT.md)
- [Pretraining and Alignment for LLMs](../Training/Pretraining-and-Alignment-for-LLMs.md)
