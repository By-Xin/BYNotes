---
title: "Exponential Family"
aliases:
  - "指数族"
  - "指数族分布"
  - "指数分布族"
  - "ProbabilityTheory/Distribution.Exponential-Family"
course: "Probability Theory"
type: "topic-note"
status: "draft"
tags:
  - course/probability-theory
  - topic/distribution-theory
  - topic/exponential-family
---

## 1. Definition

**Definition (Exponential family).** Exponential family distributions can be written as:

$$
p(y;\eta) = b(y) \exp(\eta^T T(y) - a(\eta)).
$$

其中:

- $\eta$ 是 natural parameter 或者 canonical parameter, 是决定分布的一个参数.
- $T(y)$ 是标签 $y$ 的[[Sufficiency|充分统计量 (sufficient statistic)]], 有时会取 $T(y) = y$.
- $a(\eta)$ 是 log partition function, 是一个归一化因子, 使得指数分布族中的分布 pdf 积分为 $1$.

当固定 $T$ 的选择后, 不同的 $a,b$ 就会确定不同的分布族, 这些分布族都是指数分布族, 其分布的参数由 $\eta$ 决定.

事实上, 诸如 *Gaussian, Bernoulli, Binomial, Poisson, Exponential, Gamma, Beta, Dirichlet* 等分布都是指数分布族的一种.

## 2. Bernoulli Distribution as an Exponential Family

已知 Bernoulli distribution:

$$
\begin{aligned}
p(y;\phi)
&= \phi^y(1-\phi)^{1-y} \\
&= \exp(y\log\phi + (1-y)\log(1-\phi)) \\
&= \exp\left[\left(\log\frac{\phi}{1-\phi}\right)y + \log(1-\phi)\right].
\end{aligned}
$$

[[Generalized-Linear-Models|参照 GLM 的定义]], 可以发现 Bernoulli 的分布是令 GLM 中:

- $T(y) = y$
- $\eta = \log(\frac{\phi}{1-\phi})$; 其等价于 $\phi = \frac{1}{1+e^{-\eta}}$, 即 logistic function.
- $a(\eta) = -\log (1-\phi) = \log(1 + e^{\eta})$
- $b(y) = 1$

## 3. Normal Distribution as an Exponential Family

不失一般性, 令正态分布的 $\sigma^2=1$, 则有:

$$
\begin{aligned}
p(y;\mu)
&= \frac{1}{\sqrt{2\pi}}\exp\left(-\frac{1}{2}(y-\mu)^2\right) \\
&= \frac{1}{\sqrt{2\pi}}\exp\left(-\frac{1}{2}y^2\right)\exp\left(\mu y-\frac{1}{2}\mu^2\right).
\end{aligned}
$$

对比 GLM 的定义, 可以发现:

- $\eta = \mu$
- $T(y) = y$
- $a(\eta) = \mu^2/2 = \eta^2/2$
- $b(y) = (1/\sqrt{2\pi}\exp(-y^2/2))$

## Related Notes

- [Central Limit Theorem](../Limit/Central-Limit-Theorem.md)
- [Statistical Learning Algorithms: Generalized Linear Models](../../StatisticalLearningAlgorithms/Linear/Generalized-Linear-Models.md)
