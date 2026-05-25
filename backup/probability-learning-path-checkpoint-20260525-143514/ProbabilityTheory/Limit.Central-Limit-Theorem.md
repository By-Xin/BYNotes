---
title: "Central Limit Theorem"
aliases:
  - "中心极限定理"
  - "CLT"
  - "林德伯格-列维定理"
  - "Lindeberg-Levy CLT"
course: "Probability Theory"
type: "topic-note"
status: "draft"
tags:
  - course/probability-theory
  - topic/limit-theorems
  - topic/asymptotics
---

## 1. Central Limit Theorem

Central Limit Theorem wants to show the limit distribution of

$$
Y_n = X_1 + X_2 + \cdots + X_n.
$$

To constrain the mean and variance as $n$ grows, we need to standardize it as

$$
Y_n^* = \frac{Y_n - \mathbb{E}[Y_n]}{\sqrt{\operatorname{Var}[Y_n]}}.
$$

### 1.1 CLT with i.i.d. Condition

**Theorem (Simplified CLT).** Let $X_1, X_2, \ldots, X_n$ be i.i.d. random variables with $\mathbb{E}[X_i]=0$ and $\operatorname{Var}[X_i]=1$. Then, as $n \to \infty$,

$$
\frac{1}{\sqrt{n}}\sum_{i=1}^n X_i \xrightarrow{d} \mathcal{N}(0,1).
$$

**Theorem (General i.i.d. CLT).** Let $X_1, X_2, \ldots, X_n$ be i.i.d. random variables, and suppose there exists MGF $M_X(t)$ for some neighborhood of $0$, i.e. $\exists \delta > 0$ such that $\forall t \in (-\delta, \delta)$, $M_{X_i}(t)$ exists. Furthermore, $\mathbb{E}[X_i]=\mu$, $\operatorname{Var}[X_i]=\sigma^2 < \infty$, and

$$
\bar{X}_{(n)} = \frac{1}{n} \sum_{i=1}^n X_i.
$$

Define $G_n(x)$ as the CDF of $\sqrt{n}\frac{\bar{X}_{(n)} - \mu}{\sigma}$. Then, $\forall x \in \mathbb{R}$,

$$
\lim_{n \to \infty} G_n(x) = \int_{-\infty}^x \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt.
$$

**Theorem (Lindeberg-Levy CLT).** Let $X_1, X_2, \ldots, X_n$ be i.i.d. random variables with $\mathbb{E}[X_i]=\mu$ and $\operatorname{Var}[X_i]=\sigma^2 < \infty$. Denote

$$
Y_n^* = \frac{\sum_{i=1}^n (X_i - \mu)}{\sigma \sqrt{n}}.
$$

Then, $\forall y \in \mathbb{R}$,

$$
\lim_{n \to \infty} \mathbb{P}(Y_n^* \leq y) = \Phi(y) = \int_{-\infty}^y \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt.
$$

> [!proof]+ Proof
> To prove the last equation, we only need to prove that $Y_n^* \xrightarrow{d} \mathcal{N}(0,1)$, and it is equivalent to show $\varphi_{Y_n^*}(t) \to e^{-t^2/2}$, which is the CF of $\mathcal{N}(0,1)$.
>
> Denote the CF of $X_n-\mu$ as $\varphi(t)$, then the CF of $Y_n^*$ is
>
> $$
> \varphi_{Y_n^*}(t) = \varphi\left(\frac{t}{\sigma \sqrt{n}}\right)^n.
> $$
>
> Given that $\mathbb{E}[X_i]=\mu$ and $\operatorname{Var}[X_i]=\sigma^2$, we can do the Taylor expansion of $\varphi(t)$ as
>
> $$
> \varphi(t) = \varphi(0) + \varphi'(0)t + \frac{\varphi''(0)}{2}t^2 + o(t^2) = 1 - \frac{1}{2}\sigma^2 t^2 + o(t^2).
> $$
>
> Then,
>
> $$
> \varphi_{Y_n^*}(t) = \left(1 - \frac{1}{2}\frac{t^2}{n} + o\left(\frac{t^2}{n}\right)\right)^n \to e^{-t^2/2}
> $$
>
> as $n \to \infty$.
> $\square$

> [!note] Note: Meaning of CLT
> CLT shows that, regardless of the original distribution of $X_i$, as long as $n$ is sufficiently large and the i.i.d. and finite variance assumptions hold, the distribution of $\bar{X}_{(n)}$ or $\sum_{i=1}^n X_i$ will be approximately normal. This also indicates why measurement error is often assumed to be normally distributed, since it is the sum of many small errors.

**Example (Generate $\mathcal{N}(0,1)$ from $\mathcal{U}(0,1)$ by Lindeberg-Levy CLT).**

- Generate 12 i.i.d. $\mathcal{U}(0,1)$ random variables $X_1, X_2, \ldots, X_{12}$. Then, $\mathbb{E}[X_i] = \frac{1}{2}$ and $\operatorname{Var}[X_i] = \frac{1}{12}$.
- Calculate

$$
y = \sum_{i=1}^{12} X_i - 6 \dot\sim \mathcal{N}(0,1).
$$

- Transform $y$ to $z = \sigma y + \mu \dot\sim \mathcal{N}(\mu, \sigma^2)$.
- Repeat the above steps for $n$ times, and we can get $n$ samples from $\mathcal{N}(\mu, \sigma^2)$.

### 1.2 CLT with Independent but Not Identical Condition

In practice, the i.i.d. condition is often too strict. In many cases, the random variables are independent but not identical. Here, we still want to show that, even if the random variables $X_i$ are not identically distributed, given some conditions, the sum $Y_n = \sum_{i=1}^n X_i$ will be approximately normal.

#### 1.2.1 Lindeberg-Feller CLT

In Lindeberg-Feller CLT, the key is to make each term $X_i$ "uniformly small" compared to the sum of all terms.

**Definition (Lindeberg-Feller condition).** Let $X_1, X_2, \ldots, X_n$ be independent random variables with finite mean and variance: $\mathbb{E}[X_i] = \mu_i$ and $\operatorname{Var}[X_i] = \sigma_i^2$. Denote $Y_n = \sum_{i=1}^n X_i$. Then

$$
\mathbb{E}[Y_n] = \sum_{i=1}^n \mu_i,
$$

and

$$
\sigma(Y_n) = \sqrt{\operatorname{Var}[Y_n]} = \sqrt{\sum_{i=1}^n \sigma_i^2}:=B_n.
$$

Then $Y_n$ can be standardized as

$$
Y_n^* = \frac{Y_n - \mathbb{E}[Y_n]}{\sigma(Y_n)} = \frac{Y_n - \sum_{i=1}^n \mu_i}{\sqrt{\sum_{i=1}^n \sigma_i^2}} = \sum_{i=1}^n \frac{X_i - \mu_i}{B_n}.
$$

To make each term of $Y_n^*$ "uniformly small", we can constrain the probability of event $\{\frac{X_i - \mu_i}{B_n} \ge \gamma, \forall \gamma>0\}$ to converge to $0$:

$$
\lim_{n \to \infty} \underbrace{\mathbb{P}\left(\max_{1\le i \le n} |X_i - \mu_i| > \gamma {B_n}\right)}_{(:=\dagger)} = 0, \quad \forall \gamma > 0.
$$

By probability theory, we can further derive:

$$
(\dagger) = \mathbb{P}\left(\bigcup_{i=1}^n \{|X_i - \mu_i| > \gamma B_n\}\right) \le \sum_{i=1}^n \mathbb{P}(|X_i - \mu_i| > \gamma B_n).
$$

And the last term can be further derived as:

$$
\begin{aligned}
RHS
&= \sum_{i=1}^n \int_{|x-\mu_i| > \gamma B_n} f_{X_i}(x) dx\\
&\leq \frac{1}{\gamma^2 B_n^2} \sum_{i=1}^n \int_{|x-\mu_i| > \gamma B_n} (x-\mu_i)^2 f_{X_i}(x) dx.
\end{aligned}
$$

Then, we can derive the Lindeberg-Feller condition as, for any $\gamma > 0$:

$$
\lim_{n \to \infty} \frac{1}{\gamma^2 B_n^2} \sum_{i=1}^n \int_{|x-\mu_i| > \gamma B_n} (x-\mu_i)^2 f_{X_i}(x) dx = 0. \quad (\star)
$$

Here, $(\star)$ is the Lindeberg-Feller condition.

**Theorem (Lindeberg-Feller CLT).** For random variables $X_1, X_2, \ldots, X_n$ satisfying the Lindeberg-Feller condition, for any $x \in \mathbb{R}$,

$$
\lim_{n \to \infty} \mathbb{P}\left(\frac{1}{B_n} \sum_{i=1}^n (X_i - \mu_i) \le x\right) = \Phi(x).
$$

It can be further proved that, if $\{X_i\}$ are i.i.d. with finite variance, then the Lindeberg-Feller condition is satisfied.

#### 1.2.2 Lyapunov CLT

**Theorem (Lyapunov CLT).** Let $\{X_n\}$ be a sequence of independent random variables. If there exists a $\delta > 0$ such that $\forall x$:

$$
\lim_{n \to \infty} \frac{1}{B_n^{2+\delta}} \sum_{i=1}^n \mathbb{E}[|X_i - \mu_i|^{2+\delta}] = 0,
$$

then

$$
\lim_{n \to \infty} \mathbb{P}\left(\frac{1}{B_n} \sum_{i=1}^n (X_i - \mu_i) \le x\right) = \Phi(x).
$$

## 2. Applications Using CLT

### 2.1 Error Analysis

- In numerical analysis, there is a kind of error called **round-off error**, which is caused by the finite precision of computer arithmetic. For example, when we calculate $\pi$, we can only use a finite number of digits to represent it like $\pi'\dot=3.14159$.
- More generally, if we calculate summation of such $n$ numbers $S_n = \sum_{i=1}^n X_i$, approximating it as $S'_n = \sum_{i=1}^n X'_i$, and denote the error as $\varepsilon_n = X_n - X'_n$, then the overall error is $S_n - S'_n = \sum_{i=1}^n \varepsilon_i$.
- By the property of rounding, if the approximated value $X'_i = \overline{x_0.x_1x_2\cdots x_k}$, then the real value should be in the interval $[x_0.x_1x_2\cdots (x_k-1)5, x_0.x_1x_2\cdots x_k4]$. Thus the error of a $k$-digit approximation can be regarded as a uniform distribution in $[-0.5 \times 10^{-k}, 0.5 \times 10^{-k}]$.
- Now use CLT to analyze the error of $S_n - S'_n$. Since the error of each term $\varepsilon_i$ is uniformly distributed in $[-0.5 \times 10^{-k}, 0.5 \times 10^{-k}]$, then $\mathbb{E}[\varepsilon_i] = 0$ and $\operatorname{Var}[\varepsilon_i] = \frac{1}{12} \times 10^{-2k}$. By CLT:

$$
\sum_{i=1}^n \varepsilon_i \xrightarrow{d} \mathcal{N}\left(0, \frac{n}{12} \times 10^{-2k}\right).
$$

### 2.2 Normal Approximation

#### 2.2.1 Normal Approximation with Unknown $\sigma^2$

From CLT above,

$$
\sqrt{n}(\bar{X}_{(n)} - \mu) \xrightarrow{d} \mathcal{N}(0, \sigma^2).
$$

However, in practice, we often do not know the value of $\sigma^2$. In this case, we can use the sample variance

$$
S_n^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X}_{(n)})^2
$$

to estimate $\sigma^2$. Then, Slutsky's theorem can guarantee that:

$$
\frac{\sqrt{n}(\bar{X}_{(n)} - \mu)}{S_n} \xrightarrow{d} \mathcal{N}(0,1).
$$

#### 2.2.2 Normal Approximation of Negative-Binomial Distribution

Assume $X_1, X_2, \ldots, X_n$ are i.i.d. $\operatorname{NegBin}(r,p)$. Then $\mathbb{E}[X_i] = \frac{r(1-p)}{p}$ and $\operatorname{Var}[X_i] = \frac{r(1-p)}{p^2}$. By CLT:

$$
\frac{\sum_{i=1}^n X_i - n\frac{r(1-p)}{p}}{\sqrt{n\frac{r(1-p)}{p^2}}}
= \frac{\sqrt{n}(\bar{X}_{n} - \frac{r(1-p)}{p})}{\sqrt{\frac{r(1-p)}{p}}}
\xrightarrow{d} \mathcal{N}(0,1).
$$

#### 2.2.3 Normal Approximation of Bernoulli Distribution

> [!note] Note: De Moivre-Laplace CLT
> De Moivre-Laplace CLT is a special case of CLT, and actually the first one to be proved. It shows that the binomial distribution can be approximated by normal distribution when $n$ is large.

Assume in $n$ Bernoulli trials $\mathbb{P}(A) = p$, and denote $S_n$ as the number of times $A$ happened. Then $\mathbb{E}[S_n] = np$ and $\operatorname{Var}[S_n] = np(1-p)$. By CLT:

$$
\frac{S_n - np}{\sqrt{np(1-p)}} \xrightarrow{d} \mathcal{N}(0,1).
$$

> [!note] Note: Normal approximation details
> - **Normal approximation vs. Poisson approximation.** Empirically, when $np > 5$ and $n(1-p) > 5$, the normal approximation is better than Poisson approximation. Else if $p$ is small, Poisson approximation is better.
> - **Laplace's correction.** In De Moivre-Laplace CLT, we use a continuous distribution to approximate a discrete distribution. If $S_n \sim \operatorname{Bin}(n,p)$ and $Y \sim \mathcal{N}(np, np(1-p))$, then:
> $$
> \mathbb{P}(S_n\leq x) = \mathbb{P}(Y \leq x + 0.5)
> $$
> $$
> \mathbb{P}(S_n\geq x) = \mathbb{P}(Y \geq x - 0.5)
> $$
> $$
> \mathbb{P}(k_1 \leq S_n \leq k_2) = \mathbb{P}(k_1 - 0.5 \leq Y \leq k_2 + 0.5)
> $$
> especially when $k_1,k_2$ are integers.

Using CLT, we can approximate:

$$
\mathbb{P}\left(Y^*_n = \frac{S_n-np}{\sqrt{npq}} \leq y\right) \approx \mathbb{P}(Z \leq y) = \Phi(y),
$$

where $Z \sim \mathcal{N}(0,1)$, $\Phi(y)$ is the CDF of $\mathcal{N}(0,1)$, and $S_n \sim \operatorname{Bin}(n,p)$.

## Related Notes

- [Convergence of Random Variables](./Limit.Convergence-of-Random-Variables.md)
- [Chebyshev Inequality](./Limit.Chebyshev-Inequality.md)
- [Generating Binomial Random Variables from Uniforms](./Simulation.Generate-Binomial-from-Uniform.md)
