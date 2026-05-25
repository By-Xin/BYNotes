---
title: "Support Vector Machine"
aliases:
  - "Support_Vector_Machine"
  - "Support Vector Machine"
  - "SVM"
  - "支持向量机"
  - "StatisticalLearningAlgorithms/Classification.Support-Vector-Machine"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/classification
  - topic/svm
  - topic/convex-optimization
---

## 1. Problem Setup

SVM 主要用于处理分类任务.

具体地, 我们有如下训练集 $(x_1,y_1),\ldots, (x_n,y_n)$, 希望能够构造一个函数 $f(\cdot)$, such that

$$
f(x_i)=y_i, \qquad i=1,2,\ldots,n, \quad x_i\in \mathbb{R}^n, \quad y_i\in \{-1,1\}.
$$

进一步, 为了模型的简便性, 我们希望构造的函数是线性的, 或至少是仿射的 (affine):

$$
f(x) = w^Tx + b.
$$

可以认为上述 $f(x)$ 构造了一个超平面 (hyperplane). 由解析几何知识可知, $w$ 是超平面的法向量, $b$ 是超平面的截距.

## 2. Naive Optimization Objective

首先定义点 $x$ 到平面的距离 $d(x,f)$:

$$
d(x,f) = \frac{1}{\|w\|} |w^Tx + b|.
$$

> [!proof]+ Proof of point-to-hyperplane distance
> 已知 $w$ 是平面上的法向量, $x$ 是平面上的一点, $x_0$ 是 $x$ 向平面做垂线的垂足, 则有
>
> $$
> x-x_0 \perp f \Rightarrow x-x_0 \mathop{//} w.
> $$
>
> 故
>
> $$
> |w^T(x-x_0)| =|w^Tx-w^Tx_0| = |w^Tx + b| = \|w\|\cdot \underbrace{\|x-x_0\|}_{d(x,f)}.
> $$
>
> 命题由上式最后一个等号变形即证.
>
> $\square$

再定义点集 $A$ 到超平面的距离 $d(A,f)$:

$$
d(A,f) = \min_{x\in A} d(x,f).
$$

将这个距离称为 **margin**.

在给出上述定义后, 给出理想超平面的分类准则, 即希望得到的超平面对任意类别的集合的距离最大:

$$
\begin{aligned}
\max_{w,b}\left ( \frac{w^Tx^{(A)}+b}{\|w\|} + \frac{w^Tx^{(B)}+b}{\|w\|} \right ). \quad\quad(1)
\end{aligned}
$$

由对称性, 有 $|w^Tx^{(A)}+b| = |w^Tx^{(B)}+b| := a$, 故上式可化为:

$$
\begin{aligned}
\max_{w,b}\left( \frac{2a}{\|w\|} \right). \quad\quad(2)
\end{aligned}
$$

观察上式, 会发现 $a$ 对于超平面的优化没有影响. 换言之, 我们可以通过坐标变换, 在不改变超平面的法向量 $w$ 和截距 $b$ 的情况下, 改变 $a$ 的值.

因此, 可以不妨令 $a$ 归一化为 $1$. 此时上式变为:

$$
\begin{aligned}
\max_{w,b}\left( \frac{2}{\|w\|} \right) \Leftrightarrow \min_{w,b}{\|w\|}. \quad\quad(3)
\end{aligned}
$$

但是我们还需要在优化问题中指示分类的正误与否. 具体而言, 对于 margin 上的两个点 $x^{(1)}$ 和 $x^{(-1)}$, 希望它们被正确分类:

$$
\begin{aligned}
\begin{cases}
w^Tx^{(1)}+b = 1, \\
w^Tx^{(-1)}+b = -1.
\end{cases}
\end{aligned}
$$

考虑到 margin 上的点已经是该类别点中的最小值, 则其余点的距离都将大于 $1$. 由此整合, 得到正确分类时的条件:

$$
\begin{aligned}
(w^Tx_i+b)y_i \ge 1. \quad\quad (4)
\end{aligned}
$$

结合 (3)(4) 两式, 最终得到正式的朴素分类优化目标:

$$
\begin{aligned}
\min_{w,b} \quad & \|w\| \\
\text{s.t.} \quad & y^{(i)}(w^Tx^{(i)} + b) \geq 1, \quad i = 1, \ldots, n.
\end{aligned}
$$

## 3. Mathematical Derivation

为了方便, 继续对上述优化目标进行变形. 首先该优化目标等价于:

$$
\begin{aligned}
\min_{w,b} \quad & \frac12 \|w\|^2 \\
\text{s.t.} \quad & y^{(i)}(w^Tx^{(i)} + b) \geq 1, \quad i = 1, \ldots, n.
\end{aligned}
$$

为解决这一优化问题, 引入 Lagrange multiplier, 希望优化目标 Lagrange 函数为:

$$
\begin{aligned}
L^*(w,b,\boldsymbol{\lambda}) = \frac{1}{2}\|w\|^2 + \sum_{i=1}^m {\lambda}_i \underbrace{\left [- y^{(i)}(w^Tx^{(i)}+b)+ 1\right ]}_{\text{Penalty}}. \quad \ast
\end{aligned}
$$

其中, 记 $\boldsymbol{\lambda} = [\lambda_1, \lambda_2, \cdots, \lambda_m]^T$. 此外, 注意式中 penalty 项中的符号方向.

但是 $\ast$ 中的优化函数存在问题:

- 考虑数据集中远离超平面的数据点, 会发现这些点会使得 penalty 项很负, 从而极大地影响优化结果.
- 然而, 事实上超平面的位置并不应该被这些远离 margin 的点影响.
- Ideally, 我们只需要优化函数指示分类是否大于 $1$. 对于大于 $1$ 的 case, 即不在 margin 上的点, 我们并不关心它们的具体位置.

因此得到修改后的最终 Lagrange 优化函数:

$$
\begin{aligned}
L(w,b,\boldsymbol{\lambda}) &= \frac{1}{2}\|w\|^2 + \sum_{i=1}^n \lambda_i \cdot \underbrace{\mathcal{Hinge}\left [ 1 - y^{(i)}(w^Tx^{(i)} + b)\right]  }_{\text{Nonlinear}}.
\end{aligned}
$$

其中引入截断函数:

$$
\mathcal{Hinge}(z) = \max(0, z).
$$

```python
# Hinge Function Plot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.maximum(0, x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Hinge Function")
plt.show()
```

## 4. Convex Optimization Transformations

### 4.1 Squeezing / Relaxing

继续整理上述优化内容, 得到:

$$
\begin{aligned}
\dagger^1:\quad
\min_{w,b,z} \quad & \frac{1}{2} \|w\|^2 + \sum_{i=1}^n z_i \\
\text{s.t.} \quad &  z_i \geq 1 - y^{(i)} (w^T x^{(i)} + b), \quad i = 1, \ldots, n, \\
& z_i \geq 0, \quad i = 1, \ldots, n.
\end{aligned}
$$

**Intuition (Squeezing).**

- 上述优化内容中, $\frac12\|w\|^2$ 表示需要优化的 margin, 后面 $\sum z_i$ 是 penalty.
- 由于 $\sum z_i$ 的加入, 优化中希望这一项尽可能小, 但至少要大于等于 $0$.
- 可以近似将 $z_i$ 看作是 $1-y_i(w^Tx_i+b)$ 的 inf.
- 因此在不断缩小 $z_i$ 的同时, 就在不断缩小 $1-y_iw^Tx_i$, 也就是在不断增大 margin.

**Intuition (Relaxing).**

首先有下列事实:

$$
\begin{aligned}
& z_i \ge 1-y_i\cdot (w^Tx_i+b) \ge 0 \\
\Leftrightarrow ~& \quad y_i\cdot(w^Tx_i+b) \ge 1-z_i.
\end{aligned}
$$

这一事实可以理解为:

- 可以放宽原先的 $y_i(w^Tx_i+b) \ge 1$ 约束, 允许一些误分类的点存在; 即将原约束放宽为 $y_i(w^Tx_i+b) \ge 1-z_i$, 其中 $z_i \ge 0$.
- 接着希望误分类的情况尽可能少出现, 即最小化 $\sum_{i=1}^m z_i$.

> [!note] Note: Squeezing and relaxing
> Squeezing 和 relaxing 都是在优化中常见的处理非线性等复杂情况的手段.

### 4.2 Lagrange Duality

一般地, 有下列约束问题:

$$
\begin{aligned}
\min_{x} \quad & f_0(x) \\
\text{s.t.} \quad & g_i(x) \leq 0, \quad i = 1, \ldots, n, \\
& h_i(x) = 0, \quad i = 1, \ldots, m.
\end{aligned}
$$

得到对应的 Lagrange 函数:

$$
\begin{aligned}
L(x, \lambda, \mu) &= f_0(x) + \sum_{i=1}^n \lambda_i g_i(x) + \sum_{i=1}^m \mu_i h_i(x).
\end{aligned}
$$

为了解决上述优化问题, 可以将 Lagrange 函数处理成 inner 和 outer 两个优化问题.

**Inner Optimization Problem.**

$$
x^*_{\lambda,\mu} = \arg\min_{x\in D} L(x,\lambda,\mu).
$$

**Outer Optimization Problem.**

代入上面已经得到的最优化 $x^*$, 进行优化有:

$$
\lambda^*,\mu^* = \arg\max_{\lambda,\mu} L(x^*_{\lambda,\mu},\lambda,\mu).
$$

这是一个 minimax 的策略.

> [!proof]+ Explanation of the minimax strategy
> 首先当 $x\in D$ 即处于可行域中时, 一定恒有
>
> $$
> f_0(x)\ge f_0(x) +\underbrace{  \sum \lambda_i g_i}_{g_i\le 0} + \underbrace{ \sum \mu_i h_i}_{h_i=0}. \quad\quad \text{(1)}
> $$
>
> 而 RHS 就是 Lagrange Function, 即 $f_0(x)\ge L$, 由此得到了 $L$ 的一个 sup.
>
> 由此推出, 定有:
>
> $$
> f_0(x) \ge \min_{x\in D} L(x, \lambda, \mu) ,\quad \forall x\in D. \quad\quad \text{(2)}
> $$
>
> 进一步, 亦有:
>
> $$
> \min_{x\in D} f_0(x) \ge \min_{x\in D} L(x, \lambda, \mu). \quad\quad \text{(3)}
> $$
>
> 当控制住 $x$ 的取值时, 再改变 $\lambda,\mu$ 将不会再改变 (3) 中的符号方向, 故有
>
> $$
> \min_{x\in D} f_0(x) \ge \max_{\lambda,\mu}\min_{x\in D} L(x, \lambda, \mu). \quad\quad \text{(4)}
> $$
>
> 上式中对 $\lambda,\mu$ 取 $\max$ 的原因是, $f_0(x)$ 是我们的优化目标, 在满足约束条件的前提下, 希望最终优化的结果可以尽可能接近 $f_0(x)$.

说明:

- 在满足一定条件下, (4) 中的不等号将严格取等, 即对于 Lagrange Function 的 minimax 策略最终完全逼近其 sup.
- 我们称该条件为 Slater's Condition.
- 对于能够严格取等的情况, 称为 strong duality; 反之则为 weak duality.

进一步处理, 首先恒有如下不等式:

$$
f_0(x) \ge \min_{x\in D}L(x,\lambda,\mu) \ge \min_{x}L(x,\lambda,\mu).
$$

代入到上述 (3)(4) 中, 就可以将约束优化转化为无约束优化:

$$
\min_{x\in D} f_0(x) \ge \min_{x} L(x, \lambda, \mu). \quad\quad \text{(3*)}
$$

$$
\min_{x\in D} f_0(x) \ge \max_{\lambda,\mu}\min_{x} L(x, \lambda, \mu). \quad\quad \text{(4*)}
$$

可以证明, 对于满足 Slater's Condition 的情况, 等号依然可以严格取到.

### 4.3 Example of Lagrange Duality

**Example (Minimum distance hyperplane).** 考虑如下优化问题: 寻找一个经过 $x$ 的平面使得经过原点的距离最小, 即

$$
\begin{aligned}
\min_{w,b} \quad & \frac12\|w\|^2 \\
\text{s.t.} \quad & w^Tx+b=0.
\end{aligned}
$$

> [!proof]+ Solution
> 构造 Lagrange Function:
>
> $$
> L(w,b,\lambda) = \frac{1}{2}\|w\|^2 + \lambda(w^Tx+b).
> $$
>
> 再构造对偶问题.
>
> Inner optimization:
>
> $$
> \nabla_w L(w,b,\lambda) = w + \lambda x = 0
> \Rightarrow w^* = -\lambda x.
> $$
>
> Outer optimization:
>
> $$
> L_{\omega^*}(\lambda) = -\frac12(x^Tx)\lambda^2+\lambda b
> \Rightarrow \lambda^* = \arg\min_\lambda L_{\omega^*}(\lambda).
> $$

上例很好地体现了 Lagrange dual problem 的优势: 其有效地将原问题转化为 inner 和 outer 两个相对更好解决的问题:

- Inner problem 由前面的证明已知, 是一个无约束问题.
- Outer problem 在代入 inner problem 之后得到一个更为简单的优化问题.

### 4.4 Lagrange Duality for SVM

回忆原 SVM 优化问题为:

$$
\begin{aligned}
[\dagger^1]:\quad
\min_{w,b,z} \quad & \frac{1}{2} \|w\|^2 + \sum_{i=1}^n z_i \\
\text{s.t.} \quad &  z_i \geq 1 - y^{(i)} (w^T x^{(i)} + b), \quad i = 1, \ldots, n, \\
& z_i \geq 0, \quad i = 1, \ldots, n.
\end{aligned}
$$

写作 Lagrange multiplier form:

$$
\begin{aligned}
L(w,b,z,\lambda,c)
&= \frac12 \|w\|^2 + \sum_{i=1}^n z_i + \sum_{i=1}^n c_iz_i+ \sum_{i=1}^n \lambda_i(z_i - (1 - y_i (w^T x_i + b))) \\
&= \frac12 w^Tw + \sum_{i=1}^n (1+c_i+\lambda_i)z_i - \sum_{i=1}^n \lambda_i (1 - y_i (w^T x_i + b)).
\end{aligned}
$$

进行 Lagrange duality.

**Inner Problem.**

$$
\begin{aligned}
\begin{cases}
\nabla_w L(w,b,z,\lambda,c) = w+ \sum_{i=1}^n \lambda_i y_i x_i = 0, \\
\nabla_b L(w,b,z,\lambda,c) = \sum_{i=1}^n \lambda_i y_i = 0, \\
\lambda_z L(w,b,z,\lambda,c) = 1+c_i+\lambda_i = 0, \quad i=1,\cdots,n.
\end{cases}
\end{aligned}
$$

**Outer Problem.**

Bring the inner problem into the outer problem:

$$
\begin{aligned}
L(w,b,z,\lambda,c)
&= \frac{1}{2}w^Tw + w^T \left( \sum_{i=1}^n \lambda_i y_i x_i \right) + \sum_{i=1}^n \lambda_i \\
&= \frac{1}{2} \left( -\sum_{i=1}^n \lambda_i y_i x_i \right)^T \left( -\sum_{i=1}^n \lambda_i y_i x_i \right) \\
&\quad + \left( -\sum_{i=1}^n \lambda_i y_i x_i \right)^T \left( \sum_{i=1}^n \lambda_i y_i x_i \right) + \sum_{i=1}^n \lambda_i \\
&= -\frac12 \left( \sum_{i=1}^n \lambda_i y_i x_i \right)^T \left( \sum_{i=1}^n \lambda_i y_i x_i \right) + \sum_{i=1}^n \lambda_i \\
&= -\frac12 \sum_{i=1}^n \sum_{j=1}^n  (y_i y_j x_i^T x_j)\lambda_i \lambda_j + \sum_{i=1}^n \lambda_i,
\end{aligned}
$$

subject to

$$
\sum_{i=1}^n \lambda_i y_i = 0.
$$

故得到最终的对偶优化问题:

$$
\begin{aligned}
\max_{\lambda} \quad & -\frac12 \sum_{i=1}^n \sum_{j=1}^n  (y_i y_j x_i^T x_j)\lambda_i \lambda_j + \sum_{i=1}^n \lambda_i \\
\text{s.t.} \quad & \sum_{i=1}^n \lambda_i y_i = 0.
\end{aligned}
$$

这一对偶问题是一个非常典型的二次规划问题 (Quadratic Programming Problem), 具有成熟算法可以解决. 因此可以认为已经得到了最优解 $\lambda^*$, 进而得到最优的 $w^*$ 和 $b^*$.

**Definition (Support Vector Machine).** 上述约束优化问题称为支持向量机.

## 5. Notes on SVM

1. 最终得到的决策超平面为:

   $$
   f(x) = w^Tx+b = \sum_{i=1}^n \lambda_i y_i x_i^Tx + b.
   $$

2. 关于支持向量: 通过优化计算可以发现, 最终得到的 $\lambda^*$ 是稀疏的, 即只有少数 $\lambda_i$ 不为 $0$. 这些 $\lambda_i$ 对应的样本点 $x_i$ 就是支持向量, 它们是决策超平面的关键点. 事实上, 这些支持向量就是接近决策边界的点, 它们支持着决策边界.

## Related Notes

- [Kernel Methods](../Kernel/Kernel-Methods.md)
- [Linear Models for Classification](./Linear-Models-for-Classification.md)
- [Convex Optimization CMU](../../ConvexOptimization/)
