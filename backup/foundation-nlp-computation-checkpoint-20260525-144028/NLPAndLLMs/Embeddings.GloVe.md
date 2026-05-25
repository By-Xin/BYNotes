---
title: "GloVe"
aliases:
  - "GloVe: Global Vectors for Word Representation"
  - "Global Vectors"
  - "共现矩阵"
  - "Co-occurrence Matrix"
  - "PMI"
  - "PPMI"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/embeddings
---

> [!quote] References
> - Paper: [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf), Pennington, Socher, Manning, 2014.
> - Lecture: CS224N Lecture 2.

## 1. Method Comparison

传统词向量方法有两类:

| 方法类型 | 代表 | 优点 | 缺点 |
|----------|------|------|------|
| **Count-based** | LSA, PPMI | 利用全局统计信息 | 难以捕捉语义关系 |
| **Prediction-based** | [Word2Vec](./Embeddings.Word2Vec.md) | 捕捉语义关系 | 无法利用全局信息 |

**GloVe** means **Glo**bal **Ve**ctors. It combines global information from the co-occurrence matrix with a prediction-style optimization objective.

## 2. Co-occurrence Matrix

### 2.1 Definition

- $X$: 共现矩阵, $X_{ij}$ 表示词 $j$ 在词 $i$ 的上下文窗口中出现的次数.
- $X_i = \sum_k X_{ik}$: 词 $i$ 的上下文中所有词的总次数.
- $P_{ij} = \mathbb{P}(j|i) = \frac{X_{ij}}{X_i}$: 词 $j$ 在词 $i$ 上下文中出现的概率.

### 2.2 Features

- **Symmetry**: 由于不区分词序, $X$ 是对称矩阵.
- **Sparsity**: 大型语料库中, $X$ 非常稀疏.
- **One-pass construction**: 只需扫描语料库一次.

### 2.3 Dimensionality Reduction: SVD

**Theorem (SVD).** Any matrix $X \in \mathbb{R}^{m \times n}$ can be decomposed as:

$$
X = U \Sigma V^\top.
$$

取前 $k$ 个奇异值得到低秩近似:

$$
\hat{X} \approx U_k \Sigma_k V_k^\top.
$$

**Problem.** 高频词, 如 "the" and "a", 影响过大.

**Solutions.**

- 对数变换: $\log(X_{ij})$.
- 阈值截断: $\min(X_{ij}, t)$, $t \approx 100$.
- 直接忽略.

## 3. PMI: Pointwise Mutual Information

### 3.1 PMI Definition

$$
\text{PMI}(\mathrm{w}, \mathrm{c}) =
\log \frac{P(\mathrm{w}, \mathrm{c})}{P(\mathrm{w})P(\mathrm{c})}
= \log \frac{\#(\mathrm{w}, \mathrm{c}) \cdot |\mathcal{D}|}{\#(\mathrm{w}) \cdot \#(\mathrm{c})}.
$$

- $\text{PMI} > 0$: $\mathrm{w}$ 和 $\mathrm{c}$ 正相关, 共现频率高于独立假设.
- $\text{PMI} = 0$: 独立.
- $\text{PMI} < 0$: 负相关, 倾向于不共现.

### 3.2 PPMI: Positive PMI

$$
\text{PPMI}(\mathrm{w}, \mathrm{c}) = \max(\text{PMI}(\mathrm{w}, \mathrm{c}), 0).
$$

只保留正相关, 更稳定.

### 3.3 SPPMI: Shifted PPMI

$$
\text{SPPMI}(\mathrm{w}, \mathrm{c}) = \max(\text{PMI}(\mathrm{w}, \mathrm{c}) - \log k, 0).
$$

其中 $k$ 是平滑参数.

> [!note] Note: SGNS as matrix factorization
> Skip-gram with negative sampling implicitly factorizes a shifted PMI matrix.
> Reference: [Neural Word Embedding as Implicit Matrix Factorization](https://papers.nips.cc/paper/5477).

## 4. GloVe Model

### 4.1 Core Intuition: Odds Ratio

考虑词 *ice* 和 *steam* 的共现概率比:

| $k$ | $P(k \mid \text{ice})$ | $P(k \mid \text{steam})$ | Ratio |
|-----|------------------------|--------------------------|-------|
| *solid* | $1.9 \times 10^{-4}$ | $2.2 \times 10^{-5}$ | **8.9** > 1 |
| *gas* | $6.6 \times 10^{-5}$ | $7.8 \times 10^{-4}$ | **0.085** < 1 |
| *water* | $3.0 \times 10^{-3}$ | $2.2 \times 10^{-3}$ | **1.36** approx. 1 |
| *fashion* | $1.7 \times 10^{-5}$ | $1.8 \times 10^{-5}$ | **0.96** approx. 1 |

Interpretation:

- Ratio > 1: $k$ 与 *ice* 更相关.
- Ratio < 1: $k$ 与 *steam* 更相关.
- Ratio approx. 1: $k$ 与两者关系相似.

### 4.2 Model Derivation

**Goal.** Find function $\hat{F}$ such that:

$$
\hat{F}(\mathbf{w}_i, \mathbf{w}_j, \tilde{\mathbf{w}}_k) = \frac{P(k|i)}{P(k|j)}.
$$

Derivation:

1. **Difference vector representation.**

$$
\hat{F}((\mathbf{w}_i - \mathbf{w}_j)^\top \tilde{\mathbf{w}}_k).
$$

2. **Homomorphic property.**

$$
\hat{F}(a - b) = \frac{\hat{F}(a)}{\hat{F}(b)}.
$$

3. **Exponential function.**

$$
\hat{F}(\mathbf{w}_i^\top \tilde{\mathbf{w}}_k) = \exp(\mathbf{w}_i^\top \tilde{\mathbf{w}}_k).
$$

4. **Taking log.**

$$
\mathbf{w}_i^\top \tilde{\mathbf{w}}_k = \log P(k|i) + \text{const} = \log X_{ik} - \log X_i + \text{const}.
$$

5. **Merge bias terms.**

$$
\boxed{\mathbf{w}_i^\top \tilde{\mathbf{w}}_k + b_i + \tilde{b}_k = \log X_{ik}}.
$$

### 4.3 Loss Function

$$
\mathcal{J} = \sum_{i,k=1}^{|V|} f(X_{ik}) \left( \mathbf{w}_i^\top \tilde{\mathbf{w}}_k + b_i + \tilde{b}_k - \log X_{ik} \right)^2.
$$

其中:

- $f(X_{ik})$: 权重函数, 抑制高频词影响.
- $\mathbf{w}_i, \tilde{\mathbf{w}}_k$: 词向量.
- $b_i, \tilde{b}_k$: bias 项.
- 本质是**加权最小二乘法**.

### 4.4 Weight Function $f(x)$

$$
f(x) =
\begin{cases}
(x/x_{\max})^{0.75} & \text{if } x < x_{\max}, \\
1 & \text{otherwise}.
\end{cases}
$$

通常 $x_{\max} = 100$.

## 5. GloVe vs Word2Vec

| 特性 | Word2Vec | GloVe |
|------|----------|-------|
| **方法类型** | Prediction-based | Count-based + Prediction |
| **训练方式** | 滑动窗口, 逐样本 | 全局共现矩阵 |
| **目标函数** | 交叉熵 / 负采样 | 加权最小二乘 |
| **训练效率** | 较慢, 多次扫描 | 较快, 一次构建矩阵 |
| **语义关系** | Yes | Yes |
| **全局信息** | No | Yes |

## Related Notes

- [Word Embeddings](./Embeddings.Word-Embeddings.md)
- [Word2Vec](./Embeddings.Word2Vec.md)
- [Negative Sampling](./Embeddings.Negative-Sampling.md)
- [BERT](./Models.BERT.md)
