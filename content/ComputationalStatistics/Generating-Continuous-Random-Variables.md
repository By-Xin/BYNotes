---
title: "Generating Continuous Random Variables"
aliases:
  - "连续随机变量的生成"
  - "连续随机变量生成"
  - "Inverse Transform"
  - "Rejection Method"
  - "接受拒绝法"
  - "ProbabilityTheory/Simulation.Generating-Continuous-Random-Variables"
  - "ProbabilityTheory/Simulation/Generating-Continuous-Random-Variables"
course: "Computational Statistics"
type: "method-note"
status: "draft"
tags:
  - course/computational-statistics
  - topic/random-variable-generation
  - topic/continuous-simulation
---

## 1. Inverse Transform Algorithm

### 1.1 Principle

若 $U$ 为 $(0,1)$ 区间随机数, 则任意连续型随机变量可以通过下式确定:

$$
X=F^{-1}(U).
$$

### 1.2 Example: Exponential Random Variable

See [Generating Exponential Random Variables from Uniforms](./Generate-Exponential-from-Uniform.md).

Generate a random variable $X\sim\mathrm{exp}(\lambda)$:

$$
F(x)=1-e^{-\lambda x}.
$$

Let

$$
u=F(x)=1-e^{-\lambda x}.
$$

Solving for $x$:

$$
x=-\frac1\lambda \log (1-u).
$$

Equivalently:

$$
\boxed {X=-\frac1\lambda \log (u)}.
$$

Code:

```matlab
lam = 2;
uni = rand(1, n);
X = -log(uni) / lam;
```

## 2. Rejection Method

### 2.1 Simulation Goal

通过辅助分布 $g(x)$ 生成服从较复杂的密度函数 $f(x)$ 的随机变量.

### 2.2 Simulation Method

- 首先确定一个辅助的建议分布 $Y$, 已知其概率密度函数为 $g_Y(y)$, 用来产生候选样本. 理论上 $Y$ 可服从任意分布, 而在实际计算中通常采取与目标分布 $f(x)$ 形状较为接近的分布.
- 另生成一个 $U(0,1)$ 用于后续比较.
- 计算一个常数 $c$, 使得对于 $\forall x$, 都有 $f(x)/g(x)\leq c$. 为了计算方便, 常常选择满足条件的 $c$ 中的最小值.
- 若不等式 $U \leq \frac {f(Y)}{cg(Y)}$ 成立, 则接受 $Y$, 令 $X=Y$; 否则重新生成进行比较.

Algorithm:

1. Generate $Y$ having density $g$.
2. Generate a random number $U$.
3. If $U \leqslant \frac{f(Y)}{c g(Y)}$, set $X=Y$. Otherwise, return to Step 1.

### 2.3 Principle

Let $X$ be the target random variable and $N$ be the necessary iteration count:

$$
\begin{aligned}
P\{X \leq x\}
&=P\left\{Y_N \leq x\right\} \\
&=P\{Y \leq x \mid U \leq f(Y) / \operatorname{cg}(Y)\} \\
&=\frac{P\{Y \leq x, U \leq f(Y) / \operatorname{cg}(Y)\}}{K} \\
&=\frac{\int P\{Y \leq x, U \leq f(Y) / \operatorname{cg}(Y) \mid Y=y\} g(y) d y}{K} \\
&=\frac{\int_{-\infty}^x(f(y) / \operatorname{cg}(y)) g(y) d y}{K} \\
&=\frac{\int_{-\infty}^x f(y) d y}{K c}.
\end{aligned}
$$

其中 $K=P(U \leq f(Y) / \operatorname{cg}(Y))$. 令 $x \rightarrow \infty$ 可知 $K=1/c$, 证毕.

> [!note] Note: Rejection sampling details
> - 该方法由 Von Neumann 创造, 其中的 $Y$ 为 $(a,b)$ 区间的均匀分布.
> - 由于每次接受的概率为 $P(U\leq f(Y)/cg(Y))=1/c$, 故平均循环次数的几何平均为 $c$.
> - 在循环中若拒绝, 即 $U>f(Y)/cg(Y)$, 此时并不需要重新生成随机数, 而是可以通过下面的公式直接利用先前拒绝的 $U$ 计算出新的随机数以减少运算量:
> $$
> \frac{U-f(Y)/cg(Y)}{1-f(Y)/cg(Y)}=\frac{cUg(Y)-f(Y)}{cg(Y)-f(Y)}.
> $$

### 2.4 Example: Density $f(x)=20x(1-x)^3$

要求生成随机变量 $X$ 服从:

$$
f(x)=20x(1-x)^3.
$$

Let

$$
g(x)=1, \quad 0<x<1.
$$

下求解最优 $c$:

$$
\frac{f(x)}{g(x)}=20x(1-x)^3.
$$

通过求导可知上式的极大值点为 $x=1/4$, 极大值为 $135/64$, 故 $c=135/64$.

Therefore:

$$
\frac{f(x)}{cg(x)}=\frac{256}{27}x(1-x)^3.
$$

Simulation:

1. Generate random numbers $U_1,U_2$.
2. If

$$
U_2 \leqslant \frac{256}{27} U_1\left(1-U_1\right)^3,
$$

accept and set $X=U_1$; otherwise repeat.

### 2.5 Example: Generate Standard Normal Random Variables

要求生成标准正态随机数 $Z\sim N(0,1)$.

先考虑 $X=|Z|$ 的分布:

$$
f(x)=\frac{2}{\sqrt{2 \pi}} e^{-x^2 / 2}, \quad 0<x<\infty.
$$

Let $g(x)$ be the density of $\mathrm{exp}(1)$:

$$
\frac{f(x)}{g(x)}=\sqrt{2 / \pi} e^{x-x^2 / 2}.
$$

The optimal $c$ is:

$$
c=\mathrm{max}\frac{f(x)}{g(x)}=\sqrt{\frac{2e}{\pi}}.
$$

Thus:

$$
\begin{aligned}
\frac{f(x)}{c g(x)}
&=\exp \left\{x-\frac{x^2}{2}-\frac{1}{2}\right\} \\
&=\exp \left\{-\frac{(x-1)^2}{2}\right\}.
\end{aligned}
$$

Algorithm:

1. Generate $Y$, an exponential random variable with rate $1$.
2. Generate a random number $U$.
3. If $U \leqslant \exp \left\{-(Y-1)^2 / 2\right\}$, set $X=Y$. Otherwise, return to Step 1.

在生成了绝对值正态分布后, 我们可以令 $Z$ 以相等的概率等于 $X$ 或 $-X$, 即有标准正态函数的分布.

Improvement: 对上述不等式左右取对数, 有:

$$
-\log U \geqslant(Y-1)^2 / 2.
$$

根据计算又知 $-\log U$ 服从 $\mathrm{exp}(1)$ 分布, 故算法可改进为:

1. Generate $Y_1$, an exponential random variable with rate $1$.
2. Generate $Y_2$, an exponential random variable with rate $1$.
3. If $Y_2-\left(Y_1-1\right)^2 / 2>0$, set $Y=Y_2-\left(Y_1-1\right)^2 / 2$ and go to Step 4. Otherwise, go to Step 1.
4. Generate a random number $U$ and set:

$$
Z=
\begin{cases}
Y_1 & \text{if } U \leqslant \frac{1}{2}, \\
-Y_1 & \text{if } U>\frac{1}{2}.
\end{cases}
$$

通过生成标准正态 $Z$, 其余正态函数可以通过 $\mu+\sigma Z$ 生成.

## Related Notes

- [Generating Discrete Random Variables](./Generating-Discrete-Random-Variables.md)
- [Generating Exponential Random Variables from Uniforms](./Generate-Exponential-from-Uniform.md)
- [Box-Muller Transformation](./Box-Muller-Transformation.md)
- [Change of Variables for Probability Distributions](../ProbabilityTheory/Distribution/Change-of-Variables.md)
