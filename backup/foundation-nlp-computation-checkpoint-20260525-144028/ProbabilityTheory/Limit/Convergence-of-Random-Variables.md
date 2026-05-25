---
title: "Convergence of Random Variables"
aliases:
  - "Convergence in Statistics"
  - "收敛性"
  - "随机变量的收敛"
  - "Convergence"
  - "依概率收敛"
  - "依分布收敛"
  - "ProbabilityTheory/Limit.Convergence-of-Random-Variables"
course: "Probability Theory"
type: "topic-note"
status: "draft"
tags:
  - course/probability-theory
  - topic/convergence
  - topic/limit-theorems
---

## 1. Introduction

### 1.1 Convergence of Sequences

Convergence is not a new concept in mathematics. In calculus, we define convergence of a sequence $X_n \to X$ as:

$$
\forall \epsilon > 0, \exists N \in \mathbb{N}, \text{ s.t. } \forall n \geq N, |X_n - X| < \epsilon.
$$

Or in vector form, a sequence of vectors $X_n \to X$ if:

$$
\forall \epsilon > 0, \exists N \in \mathbb{N}, \text{ s.t. } \forall n \geq N, \|X_n - X\| < \epsilon.
$$

Here, when we talk about *convergence*, we are talking about limits, and when we talk about limits, we are talking about approximations. Thus we need a distance metric to measure the closeness of two points, such as $|X_n - X|$ or $\|X_n - X\|$.

### 1.2 Convergence of Functions

Recall that, in stochastic calculus, $X_n$ is a random variable, and random variables are functions from $\Omega$ to $\mathbb{R}$. Thus, convergence of random variables is essentially the limit of a sequence of functions.

Assume that $\{f_n(x)\}$ is a sequence of functions and $f(x)$ is a function, where all functions map from $A\subseteq \mathbb{R}$ to $B\subseteq \mathbb{R}$.

**Definition (Pointwise convergence).**

$$
\forall x \in A, \forall \epsilon > 0, \exists N \in \mathbb{N}, \text{ s.t. } \forall n \geq N, |f_n(x) - f(x)| < \epsilon.
$$

**Example (Pointwise convergence).** $f_n(x) = x^n$ converges pointwise to $f(x) = 0$ on $[0,1)$.

**Definition (Uniform convergence).**

$$
\forall \epsilon > 0, \exists N \in \mathbb{N}, \text{ s.t. } \forall x \in A, \forall n>N, |f_n(x) - f(x)| < \epsilon.
$$

Notice the difference between pointwise and uniform convergence is the position of the quantifiers, i.e. $\forall x$ and $\forall n$. In pointwise convergence, $\exists N_{x,\epsilon}$ is dependent on $x$ and $\epsilon$, while in uniform convergence, $\exists N_{\epsilon}$ is independent of $x$.

**Definition (Integral convergence).**

$$
\|f_n - f\|=\int_A |f_n(x) - f(x)|dx \to 0, \quad \text{as } n \to \infty.
$$

In this note, we introduce four types of convergence in probability theory:

- Mean square convergence
- Almost sure convergence
- Convergence in probability
- Convergence in distribution

The essential difference between them is how we measure distance between random variables.

## 2. Convergence of Random Variables

### 2.1 Mean Square Convergence

In mean square convergence, we measure the distance between two random variables by the mean square error:

$$
d(X,Y) = \sqrt{\mathbb{E}|X-Y|^2}.
$$

**Definition (Mean square convergence).** $X_n$ converges to $X$ in mean square, written $X_n \xrightarrow{ms} X$, if:

$$
\lim_{n \to \infty} \mathbb{E}|X_n - X|^2 = 0.
$$

Equivalently,

$$
\forall \epsilon > 0, \exists N \in \mathbb{N}, \text{ s.t. } \forall n \geq N, \mathbb{E}|X_n - X|^2 < \epsilon.
$$

**Proposition (Mean square algebra).** Given $X_n \xrightarrow{ms} X$ and $Y_n \xrightarrow{ms} Y$:

- $X_n+Y_n \xrightarrow{ms} X+Y$ as $n \to \infty$.

  > [!proof]+ Proof of additivity
  > $$
  > d(X_n+Y_n, X+Y) \leq d(X_n, X) + d(Y_n, Y) \to 0.
  > $$
  > $\square$

- $X_nY_n \xrightarrow{ms} XY$ as $n \to \infty$.

  > [!proof]+ Proof of multiplicativity
  > $$
  > \|X_nY_n - XY\|
  > = \|X_nY_n - X_nY + X_nY - XY\|
  > $$
  >
  > $$
  > \leq \|X_n\|\cdot\|Y_n - Y\| + \|Y\|\cdot\|X_n - X\| \to 0.
  > $$
  > $\square$

- Cauchy Criterion: $\|X_n - X_m\| \xrightarrow{ms} 0$ as $n,m \to \infty$ implies there exists $X$ such that $X_n \xrightarrow{ms} X$.

Note that, in statistics, consistency is a concept similar to mean square convergence. If a sequence of estimators $\hat{\theta}_n$ converges to $\theta$ in mean square, then $\hat{\theta}_n$ is a consistent estimator of $\theta$.

> [!note] Note: $L_p$ convergence
> Convergence in mean square is a special case of convergence in $L_p$ with $p=2$:
> $$
> \lim_{n \to \infty} \mathbb{E}|X_n - X|^p = 0.
> $$
> Thus we sometimes write it as $X_n \xrightarrow{L_2} X$.

### 2.2 Almost Sure Convergence

**Definition (Almost sure convergence).** A sequence of random variables $X_1, X_2, \cdots$ converges almost surely to a random variable $X$, written $X_n \xrightarrow{a.s.} X$, if, for every $\epsilon > 0$:

$$
\mathbb{P}\left(\lim_{n \to \infty} |X_n - X| < \epsilon\right) = 1.
$$

Equivalently,

$$
\mathbb{P}\{\omega \in \Omega: X_n(\omega) \to X(\omega)\}= 1.
$$

Here, *almost surely* means $X_n$ converges to $X$ for almost all $\omega \in \Omega$, except perhaps for some set $N \subseteq \Omega$ with $\mathbb{P}(N) = 0$. Thus, $\text{a.s.} \approx \text{pointwise} - \text{zero-probability set}$.

**Example (Almost sure convergence).** Let sample space $\Omega = [0,1]$ with uniform distribution. Define $X_n(\omega) = \omega + \omega^n$ and $X(\omega) = \omega$. Then for any $\omega \in [0,1)$, $\omega^n \to 0$ as $n \to \infty$. Thus $X_n \to X$ for almost all $\omega \in \Omega$. The only exception is $\omega=1$, but $\mathbb{P}(\{1\}) = 0$.

**Proposition (No direct relation to mean square convergence).** Almost sure convergence and mean square convergence have no direct implication either way:

$$
X_n \xrightarrow{a.s.} X \nLeftrightarrow X_n \xrightarrow{ms} X.
$$

**Theorem (Strong law of large numbers).** Let $X_1, X_2, \ldots, X_n$ be i.i.d. random variables with $\mathbb{E}[X_i]=\mu$ and $\operatorname{Var}[X_i]=\sigma^2 < \infty$. Denote $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$. Then, for any $\epsilon > 0$,

$$
\mathbb{P}\left(\lim_{n \to \infty} |\bar{X}_n - \mu| < \epsilon\right) = 1.
$$

### 2.3 Convergence in Probability

**Definition (Convergence in probability).** A sequence of random variables $X_1, X_2, \cdots$ converges in probability to a random variable $X$, written $X_n \xrightarrow{p} X$, if, for every $\epsilon > 0$:

$$
\lim_{n \to \infty} \mathbb{P}(|X_n - X| < \epsilon) = 1.
$$

Equivalently,

$$
\lim_{n \to \infty} \mathbb{P}(|X_n - X| \geq \epsilon) = 0.
$$

It means that the outliers $\omega$ that make $X_n(\omega)$ far away from $X(\omega)$ become less and less likely as $n \to \infty$.

**Theorem (Almost sure convergence implies convergence in probability).** If $X_n \xrightarrow{a.s.} X$, then $X_n \xrightarrow{p} X$.

**Theorem (Continuous mapping for convergence in probability).** Suppose $X_1, X_2, \cdots$ converges to $X$ in probability, and $h(\cdot)$ is continuous. Then $h(X_1), h(X_2), \cdots$ converges to $h(X)$ in probability.

**Theorem (Weak law of large numbers).** Let $X_1, X_2, \ldots, X_n$ be i.i.d. random variables with $\mathbb{E}[X_i]=\mu$ and $\operatorname{Var}[X_i]=\sigma^2 < \infty$. Denote $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$. Then, for any $\epsilon > 0$,

$$
\lim_{n \to \infty} \mathbb{P}(|\bar{X}_n - \mu| < \epsilon) = 1.
$$

### 2.4 Convergence in Distribution / Weak Convergence

**Definition (Convergence in distribution).** A sequence of random variables $X_1, X_2, \cdots$ converges in distribution to a random variable $X$, written $X_n \xrightarrow{d} X$, $X_n \xrightarrow{L} X$, or $F_n(x) \xrightarrow{w} F_X(x)$, if for every $x \in \mathbb{R}$ where $F_X(x)$ is continuous:

$$
\lim_{n \to \infty} F_{X_n}(x) = F_X(x).
$$

Equivalently, if $X_n \sim F_{X_n}$ and $X \sim F_X$, then $X_n \xrightarrow{d} X$ iff $F_{X_n}(x) \to F_X(x)$ for all continuity points of $F_X$.

**Theorem (Slutsky's theorem).** Let $X_n \xrightarrow{d} X$ and $Y_n \xrightarrow{p} c$, where $c$ is a constant. Then:

- $X_n + Y_n \xrightarrow{d} X + c$.
- $X_nY_n \xrightarrow{d} cX$.

**Theorem (Convergence in probability implies convergence in distribution).** If $X_n \xrightarrow{p} X$, then $X_n \xrightarrow{d} X$.

**Corollary (Almost sure convergence implies convergence in distribution).** If $X_n \xrightarrow{a.s.} X$, then $X_n \xrightarrow{d} X$.

> [!note] Note: CDF-level convergence
> Convergence in distribution is essentially the convergence of the CDFs, rather than the random variables themselves. It is different from the other types of convergence, yet those types can imply convergence in distribution.

**Theorem (Constant limit equivalence).** Random variables $X_n$ converge in probability to some constant $\mu$ if and only if $X_n$ converges in distribution to $\mu$:

$$
X_n \xrightarrow{p} \mu \Leftrightarrow X_n \xrightarrow{d} \mu.
$$

## 3. Relationship Summary

$$
\begin{aligned}
&\text{Almost Sure Convergence} \Rightarrow \text{Convergence in Probability} \Rightarrow \text{Convergence in Distribution},\\
&\text{Mean Square Convergence} \Rightarrow \text{Convergence in Probability}.
\end{aligned}
$$

However, there is no direct relationship between almost sure convergence and mean square convergence.

## Related Notes

- [Chebyshev Inequality](./Chebyshev-Inequality.md)
- [Central Limit Theorem](./Central-Limit-Theorem.md)
