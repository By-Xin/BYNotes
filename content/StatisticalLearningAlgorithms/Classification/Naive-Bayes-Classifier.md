---
title: "Naive Bayes Classifier"
aliases:
  - "Naive_Bayes_Classifier"
  - "Naive Bayes"
  - "Naive Bayes Classifier"
  - "StatisticalLearningAlgorithms/Classification.Naive-Bayes-Classifier"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/classification
  - topic/generative-models
---

在 GDA 的假设中, 我们所处理的数据 $y$ 是离散的 0-1 形式, 而 $x$ 是连续的特征指标. 在 Naive Bayes 中, 我们将处理 $x$ 同样为离散的情景.

本节以 spam mail filter 为例. 其中 $y\in\{0,1\}$ 表示否/是 spam mail; $x$ 为一个 0-1 向量, 每一个元素 $x_i\in\{0,1\}$ 表示是否包含某个单词.

## 1. Multivariate Bernoulli Event Model

### 1.1 Naive Bayes Assumption

作为 generative model, 我们要通过 Bayes 公式计算 $P(y|x)$, 而为了计算它就需要得到 $P(x|y)$ 和 $P(y)$.

其中 $P(x|y)$ 由于是离散的, 假设 $x\in R^k$, 会有 $2^{k}-1$ 种可能的结果, 这会造成维度爆炸.

为简化模型, Naive Bayes 做了一个强假设, 称为 Naive Bayes Assumption, 而由此得到的模型就称为 Naive Bayes Classifier.

**Assumption (Naive Bayes).** 在给定 $y$ 的条件下, 各 $x_i$ 彼此独立, 即

$$
p(x_1, \dots, x_k | y) = \prod_{i=1}^k p(x_i | y).
$$

### 1.2 Derivation

记号:

- $\phi_{i|y=1} = p(x_i =1 | y=1 )$, $\phi_{i|y=0} = p(x_i =1 | y=0 )$.
- $\phi_{y=1} = p(y=1)$.
- Training set: $\{(x^{(i)}, y^{(i)})\}_{i=1}^m$.

得到联合似然函数:

$$
\mathcal{L(\phi_y, \phi_{j|y=0},\phi_{j|y=1})} = \prod_{i=1}^m p(x^{(i)}, y^{(i)};\phi_y, \phi_{j|y=0},\phi_{j|y=1}).
$$

得到 MLE 的参数估计:

$$
\begin{aligned}
\phi_{j|y=1} &= \frac{\sum_{i=1}^m 1\{x_j^{(i)} = 1 \wedge y^{(i)} = 1\}}{\sum_{i=1}^m 1\{y^{(i)} = 1\}}, \\
\phi_{j|y=0} &= \frac{\sum_{i=1}^m 1\{x_j^{(i)} = 1 \wedge y^{(i)} = 0\}}{\sum_{i=1}^m 1\{y^{(i)} = 0\}}, \\
\phi_y &= \frac{\sum_{i=1}^m 1\{y^{(i)} = 1\}}{m}.
\end{aligned}
$$

> [!note] Note: Parameter interpretation
> $\phi_{j|y=1}$ 就是在所有 $y=1$ 的样本中, 例如是 spam 的样本中, 第 $j$ 个特征取值为 $1$ 的样本占比. $\phi_{j|y=0}$ 同理. $\phi_y$ 就是 $y=1$ 的样本占总样本的比例.

做出判断, 即判断是否是 spam, 也就是判断概率 $p(y=1|x)$ 的大小. 具体地, 将得到的 MLE 参数带入判别式:

$$
\begin{aligned}
p(y=1|x)
&= \frac{p(x|y=1)p(y=1)}{p(x|y=1)p(y=1)+p(x|y=0)p(y=0)} \\
&= \frac{\prod_{i=1}^n p(x_i|y=1)p(y=1)}{\prod_{i=1}^n p(x_i|y=1)p(y=1)+\prod_{i=1}^n p(x_i|y=0)p(y=0)}.
\end{aligned}
$$

> [!note] Note: New dictionary entries
> 如果在 test set 中出现了一个 dictionary 不存在的新单词, 会出现问题. 因为在这种情况下, $p(x|y=1) = p(x|y=0) = 0$, 所以分子分母都是 $0$. 下文的 Laplace smoothing 可以解决这一问题.

简而言之, 得到的新的 Naive Bayes Classifier 参数估计为:

$$
\begin{aligned}
\phi_{i|y=1}
&= \frac{\sum_{j=1}^{m} 1\{x_i^{(j)} = 1 \wedge y^{(j)} = 1\} + 1}{\sum_{j=1}^{m} 1\{y^{(j)} = 1\} + 2}, \\
\phi_{i|y=0}
&= \frac{\sum_{j=1}^{m} 1\{x_i^{(j)} = 1 \wedge y^{(j)} = 0\} + 1}{\sum_{j=1}^{m} 1\{y^{(j)} = 0\} + 2}.
\end{aligned}
$$

## 2. Laplace Smoothing

原始问题: 上文提到的 $\frac00$ 问题可以概括为, 在统计学意义上, 我们直接将数据集中没有出现过的结果都认为其出现概率为 $0$.

具体而言, 假设我们有一个有限样本容量 $m$ 的数据集 $\{z^{(1)},...,z^{(m)}\}$, 每个样本 $z^{(i)}$ 以概率 $\phi_i = p(z=i)$ 取值为 $\{1,\ldots,k\}$ 的一个. Initially, 对于参数 $\phi_j$, 即 $z$ 取第 $j$ 种取值, 其估计为:

$$
\phi_j = \sum_{i=1}^m \mathit{1}_{\{z^{(i)}=j\}}/m.
$$

**Definition (Laplace smoothing formula).**

$$
\phi_j = \frac{1+\sum_{i=1}^m \mathit{1}_{\{z^{(i)}=j\}}}{m+k}.
$$

这里的 $k$ 是 $z^{(i)}$ 有可能取到的取值个数.

通过 Laplace smoothing 变换的数据依然符合归一化, 即 $\sum_{j=1}^k \phi_j = 1$, 且解决了 $0/0$ 的问题.

## 3. Multinomial Event Model

对于同样的 spam detection 问题, 我们采用另一种表示方法:

- 记 $|V|$ 为词典规模, 即含有的单词数量; $n$ 为识别的 email 中的 token 总数.
- 向量 $x \in \mathbb{R}^{n}$ 表示一整个 email, 每个分量 $x_{i}\in \{1,2,\ldots,|V|\}$ 中下标 $i$ 表示 email 按照行文顺序的第 $i$ 个字符, 其取值表示该位置的这个词在词典中的编号.

同样施加 Naive Bayes Assumption:

$$
p(x,y) = p(x|y)p(y) = \prod_{i=1}^{n}p(x_i|y)p(y).
$$

### 3.1 Spam Detection Example

- $\phi_y = p(y=1)$.
- $\phi_{k|y=0} = p(x_j=k|y=0)$: 在类别为 $0$ 的情况下, email 中第 $j$ 个单词取到字典中第 $k$ 个单词的概率. 注意这里的 $\phi$ 并不依赖于 $j$, 这是在假设单词的出现内容与其所在的位置无关.

得到似然函数:

$$
\begin{aligned}
\mathcal{L}\left(\phi, \phi_{k \mid y=0}, \phi_{k \mid y=1}\right)
&=\prod_{i=1}^m p\left(x^{(i)}, y^{(i)}\right) \\
&=\prod_{i=1}^m\left(\prod_{j=1}^{n_i} p\left(x_j^{(i)} \mid y ; \phi_{k \mid y=0}, \phi_{k \mid y=1}\right)\right) p\left(y^{(i)} ; \phi_y\right).
\end{aligned}
$$

其中 $m$ 为 email 数, 即 training set 样本数, $n_i$ 为第 $i$ 个 email 中的 token 数.

得到 MLE:

$$
\begin{aligned}
\phi_{k \mid y=1} & =\frac{\sum_{i=1}^m \sum_{j=1}^{n_i} 1\left\{x_j^{(i)}=k \wedge y^{(i)}=1\right\}}{\sum_{i=1}^m 1\left\{y^{(i)}=1\right\} n_i}, \\
\phi_{k \mid y=0} & =\frac{\sum_{i=1}^m \sum_{j=1}^{n_i} 1\left\{x_j^{(i)}=k \wedge y^{(i)}=0\right\}}{\sum_{i=1}^m 1\left\{y^{(i)}=0\right\} n_i}, \\
\phi_y & =\frac{\sum_{i=1}^m 1\left\{y^{(i)}=1\right\}}{m}.
\end{aligned}
$$

该理解也是自然的:

- $\phi_{k|y=0}$ 表示遍历每一个 email 样本 $i=1 \text{ to } m$, 再遍历每个 email 样本中的全部 token, 得到标记为 spam 的 email 且出现单词 $k$ 的次数, 再除以全部 email 中标记为 spam 的总词汇数目.
- 其余参数也以此类推.

## Related Notes

- [Gaussian Discriminant Analysis](./Gaussian-Discriminant-Analysis.md)
- [Regularization](../Linear/Regularization.md)
