---
title: "Chebyshev Inequality"
aliases:
  - "切比雪夫不等式"
  - "Concentration Inequality"
course: "Probability Theory"
type: "topic-note"
status: "draft"
tags:
  - course/probability-theory
  - topic/limit-theorems
  - topic/concentration
---

## 1. Statement

**Theorem (Chebyshev inequality).** For every $\epsilon > 0$,

$$
\mathbb{P}(|X| \geq \epsilon) \leq \frac{\mathbb{E}[X^2]}{\epsilon^2}.
$$

## 2. Proof

> [!proof]+ Proof
> $$
> \mathbb{E}|X|^2
> = \int_{\{|X| \geq \epsilon\} \cup \{|X| < \epsilon\}} |x|^2 f_X(x) dx
> \geq \int_{|X| \geq \epsilon} x^2 f_X(x) dx
> \geq \int_{|X| \geq \epsilon} \epsilon^2 f_X(x) dx
> = \epsilon^2 \mathbb{P}(|X| \geq \epsilon).
> $$
> Dividing by $\epsilon^2$ gives the result.
> $\square$

## 3. Corollary

**Corollary (Centered Chebyshev inequality).**

$$
\mathbb{P}(|X-\mathbb{E}[X]| \geq \epsilon) \leq \frac{\operatorname{Var}[X]}{\epsilon^2}.
$$

## Related Notes

- [Convergence of Random Variables](./Limit.Convergence-of-Random-Variables.md)
- [Central Limit Theorem](./Limit.Central-Limit-Theorem.md)
