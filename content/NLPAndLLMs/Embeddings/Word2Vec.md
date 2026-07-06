---
title: "Word2Vec"
aliases:
  - "Skip-gram"
  - "CBOW"
  - "词向量模型"
  - "NLPAndLLMs/Embeddings.Word2Vec"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/embeddings
---

> [!quote] References
> - Paper: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), Mikolov et al., 2013.
> - Lecture: CS224N Lecture 1.

## 1. Basic Idea

**Word2Vec** 是一种通过预测上下文来学习词向量的模型.

Core idea:

1. 拥有一个大型文本 **corpus**.
2. 模型扫描文本, 每次选取一个**中心词** $\mathrm{c}$ 和其**上下文词** $\mathrm{o}$.
3. 通过最大化 "在 $\mathrm{c}$ 的上下文中 $\mathrm{o}$ 出现的概率" 来优化词向量.

![Word2Vec sliding-window illustration](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/20250116130511.png)

Word2Vec 有两种实现方式:

- **Skip-gram**: given the center word, predict context words. This is more commonly used.
- **CBOW** (Continuous Bag of Words): given context words, predict the center word.

## 2. Skip-gram Model

### 2.1 Intuition

Given sentence *"the quick brown **fox** jumps over the lazy dog"*:

- Center word: *fox*.
- Context words with window size 2: *quick*, *brown*, *jumps*, *over*.

**Goal.** Maximize the probability of context words and minimize the probability of non-context words.

![Skip-gram prediction illustration](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/20250116170501.png)

### 2.2 Model Definition

Notation:

- Text position $t = 1, 2, \ldots, T$.
- Word (token) $w_t$ at position $t$, where the word vector is introduced separately below as $v_w$ (center) / $u_w$ (context), each in $\mathbb{R}^d$ with $d$ often $100$ to $300$.
- Context window size $m$, usually $2$ to $4$.

Likelihood:

$$
\mathcal{L}(\theta) = \prod_{t=1}^T \prod_{-m \leq j \leq m, j \neq 0} \mathbb{P}(w_{t+j}|w_t ; \theta).
$$

Negative log-likelihood:

$$
\mathcal{J}(\theta) = - \frac{1}{T} \sum_{t=1}^T \sum_{-m \leq j \leq m, j \neq 0} \log \mathbb{P}(w_{t+j}|w_t ; \theta).
$$

### 2.3 Probability Calculation

**Dual vector representation.** 为计算方便, 对同一词汇使用两种向量:

- $v_\mathrm{w}$: vector when $\mathrm{w}$ is the center word.
- $u_\mathrm{w}$: vector when $\mathrm{w}$ is the context word.

Conditional probability with softmax:

$$
\mathbb{P}(\mathrm{o}|\mathrm{c}) =
\frac{\exp(u_\mathrm{o}^\top v_\mathrm{c})}{\sum_{\mathrm{w} \in \mathcal{V}} \exp(u_\mathrm{w}^\top v_\mathrm{c})}.
$$

其中 $\mathcal{V}$ 为词汇表. 内积 $u_\mathrm{o}^\top v_\mathrm{c}$ 衡量两个词向量的相似性.

Cross-entropy-style loss:

$$
\mathcal{J}(\theta) =
\sum_{d \in \mathcal{D}} \sum_{t=1}^{|T_d|} \sum_{-m \leq j \leq m, j \neq 0}
- \log \mathbb{P}(w^{(d)}_{t+j}|w^{(d)}_t ; \theta).
$$

Equivalently:

$$
\min_{U,V} \mathbb{E}_{\mathrm{c},\mathrm{o}}[-\log \mathbb{P}_{U,V}(\mathrm{o}|\mathrm{c})].
$$

## 3. Gradient Derivation

### 3.1 Gradient Descent

Initialization:

$$
U, V \sim \mathcal{N}(0, 0.001)^{|\mathcal{V}| \times d}.
$$

Update rule:

$$
U^{(i+1)} := U^{(i)} - \alpha \nabla_U \mathcal{J}(U^{(i)}, V^{(i)}).
$$

### 3.2 Gradient Calculation

For center word $\mathrm{c}$ and context word $\mathrm{o}$, calculate $\nabla_{v_\mathrm{c}} \log \mathbb{P}(\mathrm{o}|\mathrm{c})$:

$$
\nabla_{v_\mathrm{c}} \log \mathbb{P}(\mathrm{o}|\mathrm{c})
= \nabla_{v_\mathrm{c}} \log \exp(u_\mathrm{o}^\top v_\mathrm{c})
- \nabla_{v_\mathrm{c}} \log \sum_{\mathrm{w} \in \mathcal{V}} \exp(u_\mathrm{w}^\top v_\mathrm{c}).
$$

First term:

$$
\nabla_{v_\mathrm{c}} \log \exp(u_\mathrm{o}^\top v_\mathrm{c}) = u_\mathrm{o}.
$$

Second term:

$$
\nabla_{v_\mathrm{c}} \log \sum_{\mathrm{w}} \exp(u_\mathrm{w}^\top v_\mathrm{c})
= \frac{\sum_{\mathrm{x}} \exp(u_\mathrm{x}^\top v_\mathrm{c}) \cdot u_\mathrm{x}}{\sum_{\mathrm{w}} \exp(u_\mathrm{w}^\top v_\mathrm{c})}
= \sum_{\mathrm{x}} \mathbb{P}(\mathrm{x}|\mathrm{c}) u_\mathrm{x}.
$$

### 3.3 Final Result

$$
\boxed{\nabla_{v_\mathrm{c}} \log \mathbb{P}(\mathrm{o}|\mathrm{c}) = u_\mathrm{o} - \mathbb{E}_{\mathrm{w} \sim \mathbb{P}(\mathrm{w}|\mathrm{c})}[u_\mathrm{w}]}.
$$

Intuition:

- $u_\mathrm{o}$: observed context word vector.
- $\mathbb{E}[u_\mathrm{w}]$: expected context word vector under the current model.
- Gradient = observed - expected.
- 通过梯度下降, 使词向量接近观测到的上下文, 远离预期的上下文.

## 4. Problem with Softmax

The computational bottleneck is the denominator:

$$
\sum_{\mathrm{w} \in \mathcal{V}} \exp(u_\mathrm{w}^\top v_\mathrm{c}).
$$

- 词汇表 $|\mathcal{V}|$ 通常很大, often more than 100k.
- 每次更新都需要 $\mathcal{O}(|\mathcal{V}|)$ complexity.
- Solution: [Negative Sampling](./Negative-Sampling.md), which approximates the full vocabulary with a small number of negative samples.

## 5. Neural Network Perspective

Skip-gram 模型本质上是一个**浅层神经网络**.

![Skip-gram network structure](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/20250116200255.png)

### 5.1 Network Structure

| Layer | Shape | Description |
|----|------|------|
| **Input layer** | $\mathbf{x} \in \mathbb{R}^V$ | One-hot vector of the center word |
| **Hidden layer** | $\mathbf{h} \in \mathbb{R}^d$ | Word embedding vector |
| **Output layer** | $\mathbf{z} \in \mathbb{R}^V$ | Prediction scores or logits |

### 5.2 Forward Propagation

1. **Input to hidden layer**, i.e. embedding lookup:

$$
\mathbf{h} = \mathbf{x}^\top W_{\text{in}} = W_{\text{in}}[c, :].
$$

- $W_{\text{in}} \in \mathbb{R}^{V \times d}$: center-word embedding matrix.
- One-hot multiplication is equivalent to taking row $c$.

2. **Hidden layer to output layer**, i.e. linear transformation:

$$
\mathbf{z} = W_{\text{out}} \mathbf{h}.
$$

- $W_{\text{out}} \in \mathbb{R}^{V \times d}$: context-word embedding matrix.
- $z_j = \mathbf{u}_j^\top \mathbf{h}$: score of word $j$.

3. **Softmax / Sigmoid**:

- Full softmax: $\hat{y}_j = \frac{\exp(z_j)}{\sum_w \exp(z_w)}$.
- Negative sampling: $\sigma(z_j)$ or $\sigma(-z_j)$.

### 5.3 Training Process

```text
1. Forward:  one-hot -> embedding -> logits -> softmax/sigmoid
2. Loss:     cross-entropy / negative sampling loss
3. Backward: calculate gradients and update W_in, W_out
4. Repeat:   sample (center, context) pairs and iterate
```

Key insights:

- 无隐藏层激活函数, 即恒等映射.
- 本质是两层线性变换 + softmax/sigmoid.
- 模型参数就是两个嵌入矩阵.

## 6. Matrix Factorization Perspective

### 6.1 Full Softmax Matrix Form

1. Take the center-word vector:

$$
\mathbf{v}_c = W_{\text{in}}[c, :] \in \mathbb{R}^{1 \times d}.
$$

2. Calculate scores for all words:

$$
\mathbf{z} = \mathbf{v}_c \times W_{\text{out}}^\top \in \mathbb{R}^{1 \times V}.
$$

3. Apply softmax:

$$
\hat{\mathbf{y}} = \text{softmax}(\mathbf{z}) \in \mathbb{R}^{1 \times V}.
$$

4. Cross-entropy loss:

$$
\mathcal{L} = -\log \hat{y}_o.
$$

### 6.2 Negative Sampling Matrix Form

1. Positive sample score:

$$
z_{\text{pos}} = \mathbf{v}_c \cdot \mathbf{u}_o.
$$

2. Negative sample scores:

$$
\mathbf{z}_{\text{neg}} = \mathbf{v}_c \times \mathbf{U}_{\text{neg}}^\top \in \mathbb{R}^{1 \times K}.
$$

Here $\mathbf{U}_{\text{neg}} \in \mathbb{R}^{K \times d}$ is the embedding matrix for $K$ negative samples.

3. Loss:

$$
\mathcal{L} = -\log \sigma(z_{\text{pos}}) - \sum_{k=1}^K \log \sigma(-z_{\text{neg},k}).
$$

## 7. PyTorch Implementation

### 7.1 Data Preparation

```python
import torch
import random
import numpy as np
from collections import Counter

torch.manual_seed(42)
random.seed(42)
np.random.seed(42)

# Example corpus
corpus = [
    "i like to eat apples and bananas",
    "i like to watch movies and cartoons",
    "the cat likes to eat fish",
    "john loves to read books about python",
]

# Tokenization
tokenized_sentences = [sent.lower().split() for sent in corpus]

# Build vocabulary
all_tokens = [t for sent in tokenized_sentences for t in sent]
word_counter = Counter(all_tokens)
vocab = sorted(word_counter.keys())
word2idx = {w: i for i, w in enumerate(vocab)}
idx2word = {i: w for w, i in word2idx.items()}
vocab_size = len(vocab)

print(f"Vocabulary size = {vocab_size}")
```

### 7.2 Generate Skip-gram Training Samples

```python
def make_skipgram_data(tokenized_sentences, word2idx, window_size=2):
    """Generate (center_idx, outside_idx) pairs."""
    pairs = []
    for tokens in tokenized_sentences:
        token_ids = [word2idx[w] for w in tokens]
        length = len(token_ids)
        for i, center_id in enumerate(token_ids):
            start = max(i - window_size, 0)
            end = min(i + window_size + 1, length)
            for j in range(start, end):
                if j != i:
                    pairs.append((center_id, token_ids[j]))
    return pairs

skipgram_pairs = make_skipgram_data(tokenized_sentences, word2idx, window_size=2)
print(f"Total skip-gram pairs: {len(skipgram_pairs)}")
```

### 7.3 Model Definition with Negative Sampling

```python
import torch.nn as nn

class SkipGramNegSample(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_negatives=5):
        super().__init__()
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim
        self.num_negatives = num_negatives

        # Two embedding matrices
        self.in_embed = nn.Embedding(vocab_size, embed_dim)   # center word
        self.out_embed = nn.Embedding(vocab_size, embed_dim)  # context word

        # Negative sampling distribution: word frequency^0.75
        word_freq = np.array([word_counter[idx2word[i]] for i in range(vocab_size)], dtype=np.float32)
        word_freq = word_freq ** 0.75
        self.neg_sampling_dist = word_freq / word_freq.sum()

        # Initialization
        nn.init.uniform_(self.in_embed.weight, -0.5, 0.5)
        nn.init.uniform_(self.out_embed.weight, -0.5, 0.5)

    def forward(self, center_ids, outside_ids):
        batch_size = center_ids.size(0)

        # 1. Lookup embeddings
        center_embed = self.in_embed(center_ids)      # (batch, embed_dim)
        outside_embed = self.out_embed(outside_ids)   # (batch, embed_dim)

        # 2. Positive sample score and loss
        pos_scores = torch.sum(center_embed * outside_embed, dim=1)
        pos_loss = -torch.log(torch.sigmoid(pos_scores) + 1e-8)

        # 3. Sample negative examples
        neg_samples = np.random.choice(
            range(self.vocab_size),
            size=(batch_size, self.num_negatives),
            p=self.neg_sampling_dist,
        )
        neg_samples = torch.LongTensor(neg_samples)

        # 4. Negative sample scores and loss
        neg_embed = self.out_embed(neg_samples)        # (batch, num_neg, embed_dim)
        center_expand = center_embed.unsqueeze(1)      # (batch, 1, embed_dim)
        neg_scores = torch.bmm(neg_embed, center_expand.transpose(1, 2)).squeeze()
        neg_loss = -torch.log(torch.sigmoid(-neg_scores) + 1e-8)

        # 5. Total loss
        total_loss = (pos_loss + neg_loss.sum(1)).mean()
        return total_loss
```

### 7.4 Training Loop

```python
embed_dim = 8
num_negatives = 4
model = SkipGramNegSample(vocab_size, embed_dim, num_negatives)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

num_epochs = 3
pairs_list = skipgram_pairs[:]

for epoch in range(num_epochs):
    random.shuffle(pairs_list)
    total_loss = 0.0

    for (center_id, outside_id) in pairs_list:
        center_tensor = torch.LongTensor([center_id])
        outside_tensor = torch.LongTensor([outside_id])

        loss = model(center_tensor, outside_tensor)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(pairs_list)
    print(f"Epoch {epoch+1}/{num_epochs}, Avg Loss={avg_loss:.4f}")
```

### 7.5 Validate Results

```python
def get_embedding(model, word):
    idx = word2idx[word]
    return model.in_embed.weight[idx].detach().numpy()

def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9)

def most_similar_words(model, query_word, top_k=3):
    query_emb = get_embedding(model, query_word)
    sims = []
    for w in vocab:
        if w == query_word:
            continue
        sim_score = cosine_sim(query_emb, get_embedding(model, w))
        sims.append((w, sim_score))
    sims.sort(key=lambda x: x[1], reverse=True)
    return sims[:top_k]

# Test
for w in ["eat", "movies", "python"]:
    if w in word2idx:
        print(f"\n[Most similar to '{w}']")
        for candidate, score in most_similar_words(model, w):
            print(f"   {candidate:<10} cos_sim = {score:.4f}")
```

## 8. Summary

| Perspective | Core Idea |
|------|----------|
| **Neural network** | Two linear transformations: one-hot to embedding to logits |
| **Matrix factorization** | Implicitly factorizes a PMI matrix |
| **Probabilistic model** | Maximizes the conditional probability of context words |

Key points:

1. 以可微方式从输入映射到输出.
2. 通过反向传播更新参数.
3. 本质是学习两个嵌入矩阵 $W_{\text{in}}, W_{\text{out}}$.

## Related Notes

- [Negative Sampling](./Negative-Sampling.md)
- [GloVe](./GloVe.md)
- [Word Embeddings](./Word-Embeddings.md)
- [BERT](../Models/BERT.md)
