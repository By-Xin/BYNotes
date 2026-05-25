---
title: "Sufficiency"
aliases:
  - "Sufficiency"
  - "Sufficiency.md"
  - "Sufficient Statistic"
  - "充分性"
  - "充分统计量"
course: "Statistical Inference"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-inference
  - topic/sufficiency
  - topic/estimation
---

## 1. Definition

R. A. Fisher proposed the concept of sufficiency in 1922. Given a random sample $\mathbf{X} = (X_1, \cdots, X_n)^T$ from a distribution with pdf $f(\mathbf{x},\theta)$, a statistic $S(\mathbf{X})$ is called a sufficient statistic for $\theta$ if $f(\mathbf{x},\theta| S(\mathbf{X}))$ is independent of $\theta$.

**Example (Sufficient statistic for Bernoulli distribution).** Consider $X_1, \cdots, X_n \sim_{i.i.d.} \text{Bernoulli}(p)$. The likelihood function is

$$
L(p) = \prod_{i=1}^n p^{x_i}(1-p)^{1-x_i} = p^{\sum_{i=1}^n x_i}(1-p)^{n-\sum_{i=1}^n x_i}.
$$

The conditional distribution of $\mathbf{X}$ given $S(\mathbf{X}) = \sum_{i=1}^n X_i$ is

$$
f(\mathbf{x}| S(\mathbf{X})) = \frac{\mathbb{P}(X_1 = x_1, \cdots, X_n = x_n)}{\mathbb{P}(S(\mathbf{X}) = \sum_{i=1}^n x_i = t)} = \frac{p^t(1-p)^{n-t}}{\binom{n}{t} p^t (1-p)^{n-t}} = \binom{n}{t}^{-1}.
$$

This is a function of $S(\mathbf{X})$ only without $p$. Therefore, $S(\mathbf{X})$ is a sufficient statistic for $p$.

> [!note] Note: Conditional randomness
> This is natural regarding the distribution. As long as $\sum_{i=1}^n X_i$ is given, the total number of $X_i = 1$ and $X_i = 0$ are determined. The randomness about $\{\sum X_k = t\}$ is the permutation, or the order of those $0$s and $1$s, whose probability is $\binom{n}{t}^{-1}$, a uniform distribution independent of $p$.

## 2. Neyman Factorization Theorem

**Theorem (Neyman Factorization Theorem).** A statistic $S(\mathbf{X})$ is a sufficient statistic for $\theta$ if and only if the probability density function can be written as

$$
f(\mathbf{x}, \theta) = h(\mathbf{x}) g(S(\mathbf{x}), \theta)
$$

for some functions $h(\mathbf{x})$ and $g(S(\mathbf{x}), \theta)$.

## Related Notes

- [Neyman Factorization Theorem](./Sufficiency.Neyman-Factorization-Theorem.md)
- [Fisher Information](./Information.Fisher-Information.md)
- [UMVUE](./UMVU.UMVUE.md)
