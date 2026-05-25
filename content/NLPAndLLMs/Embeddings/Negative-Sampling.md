---
title: "Negative Sampling"
aliases:
  - "Negative Sampling 负采样"
  - "负采样"
  - "NEG"
  - "Skip-gram with Negative Sampling"
  - "NLPAndLLMs/Embeddings.Negative-Sampling"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/embeddings
  - topic/optimization
---

> [!quote] References
> - Paper: [Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546), Mikolov et al., 2013.
> - Lecture: CS224N Lecture 1.

## 1. Motivation

### 1.1 Problem with Softmax

In standard [Word2Vec](./Word2Vec.md), the conditional probability uses softmax:

$$
\mathbb{P}(\mathrm{o}|\mathrm{c}) =
\frac{\exp(u_\mathrm{o}^\top v_\mathrm{c})}{\sum_{\mathrm{w} \in \mathcal{V}} \exp(u_\mathrm{w}^\top v_\mathrm{c})}.
$$

The denominator, or partition function, has several problems:

1. **Computational complexity**: It requires summing over the whole vocabulary $\mathcal{V}$, so the complexity is $\mathcal{O}(|\mathcal{V}|)$.
2. **Large vocabulary**: Usually $|\mathcal{V}| > 100,000$.
3. **Low optimization efficiency**: Every update needs scores for all words.

### 1.2 Role of the Partition Function

从两个角度理解分母:

- **Probability perspective**: 归一化项, 保证概率和为 $1$.
- **Optimization perspective**:
  - 提高分子 $\exp(u_\mathrm{o}^\top v_\mathrm{c})$, 即正样本相似度.
  - 降低分母 $\sum_{\mathrm{w}} \exp(u_\mathrm{w}^\top v_\mathrm{c})$, 即负样本相似度.

## 2. Negative Sampling Method

### 2.1 Core Idea

> [!note] Note: Core idea
> 我们没必要遍历整个词汇表, 只需要对少量有代表性的词汇进行采样即可.

将多分类问题转化为**多个二分类问题**:

- 正样本: 真实的 `(center, context)` pair, label = $1$.
- 负样本: 随机采样的 `(center, random)` pair, label = $0$.

### 2.2 New Loss Function

For center word $\mathrm{c}$ and context word $\mathrm{o}$:

$$
\boxed{\mathcal{J} = -\log \sigma(u_\mathrm{o}^\top v_\mathrm{c}) - \sum_{\mathrm{k} \in \mathcal{K}} \log \sigma(-u_\mathrm{k}^\top v_\mathrm{c})}.
$$

其中:

- $\sigma(x) = \frac{1}{1+\exp(-x)}$ is the sigmoid function.
- $\mathcal{K}$ is the set of $K$ negative samples, usually $K = 5 \sim 20$.

### 2.3 Loss Interpretation

| Term | Formula | Goal |
|-----|------|------|
| **Positive sample** | $-\log \sigma(u_\mathrm{o}^\top v_\mathrm{c})$ | Make $\sigma(\cdot) \to 1$, so positive sample score is high |
| **Negative sample** | $-\log \sigma(-u_\mathrm{k}^\top v_\mathrm{c})$ | Make $\sigma(-\cdot) \to 1$, so negative sample score is low |

Equivalently, the negative sample term can be written as:

$$
-\log(1 - \sigma(u_\mathrm{k}^\top v_\mathrm{c})).
$$

## 3. Negative Sampling Distribution

### 3.1 Sampling Strategy

Negative sample $\mathrm{k}$ is sampled from distribution $p_{\text{neg}}$:

$$
p_{\text{neg}}(\mathrm{w}) =
\frac{\text{freq}(\mathrm{w})^{\alpha}}{\sum_{\mathrm{w'} \in \mathcal{V}} \text{freq}(\mathrm{w'})^{\alpha}}.
$$

其中:

- $\text{freq}(\mathrm{w})$ is the frequency of word $\mathrm{w}$ in the corpus.
- $\alpha \in (0, 1)$, with empirical recommendation $\alpha = 0.75$.

### 3.2 Why Use $\alpha = 0.75$?

- $\alpha = 1$: 按原始词频采样, 高频词如 "the" and "a" 被过度采样.
- $\alpha = 0$: 均匀采样, 忽略词频信息.
- $\alpha = 0.75$: 平滑词频分布, 既考虑词频又避免过度集中.

Example: suppose "the" appears 100 times and "cat" appears 1 time.

- Original ratio: $100:1$.
- Smoothed ratio: $100^{0.75} : 1^{0.75} = 31.6 : 1$.

## 4. Softmax vs Negative Sampling

|  | **Full Softmax** | **Negative Sampling** |
|--|------------------|----------------------|
| **Computed logits** | All $V$ words | 1 positive sample + $K$ negative samples |
| **Complexity** | $\mathcal{O}(V)$ | $\mathcal{O}(K)$, $K \ll V$ |
| **Loss** | $-\log \frac{\exp(u_\mathrm{o}^\top v_\mathrm{c})}{\sum_{\mathrm{w}} \exp(u_\mathrm{w}^\top v_\mathrm{c})}$ | $-\log \sigma(u_\mathrm{o}^\top v_\mathrm{c}) - \sum_{\mathrm{k}} \log \sigma(-u_\mathrm{k}^\top v_\mathrm{c})$ |
| **Normalization** | Global normalization | No global normalization |
| **Classification type** | Multi-class classification | Multiple binary classifications |

### 4.1 Matrix Form

**Full Softmax.**

$$
\mathbf{z} = \mathbf{v}_c \times W_{\text{out}}^\top \in \mathbb{R}^{1 \times V}.
$$

$$
\hat{\mathbf{y}} = \text{softmax}(\mathbf{z}).
$$

$$
\mathcal{L} = -\log \hat{y}_o.
$$

**Negative Sampling.**

$$
\mathcal{L} = -\log \sigma(\mathbf{v}_c \cdot \mathbf{u}_o) - \sum_{k=1}^{K} \log(1 - \sigma(\mathbf{v}_c \cdot \mathbf{u}_k)).
$$

## 5. Practical Suggestions

### 5.1 Hyperparameters

| Parameter | Suggested Value | Description |
|------|--------|------|
| $K$ | 5-20 | Use larger $K$ for small datasets and smaller $K$ for large datasets |
| $\alpha$ | 0.75 | Empirically strong smoothing exponent |

### 5.2 Preprocessing

```python
# Count word frequency
word_freq = Counter(all_tokens)

# Compute negative sampling probabilities
alpha = 0.75
freq_array = np.array([word_freq[w] for w in vocab])
neg_sampling_dist = (freq_array ** alpha) / (freq_array ** alpha).sum()
```

## Related Notes

- [Word2Vec](./Word2Vec.md)
- [GloVe](./GloVe.md)
- [Word Embeddings](./Word-Embeddings.md)
