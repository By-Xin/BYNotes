---
title: "Kernel Methods"
aliases:
  - "Kernel_Methods"
  - "Kernel Methods"
  - "Kernel Trick"
  - "核方法"
  - "核技巧"
  - "StatisticalLearningAlgorithms/Kernel.Kernel-Methods"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/kernel-methods
  - topic/rkhs
---

> [!quote] References
> - Lecture: 李政軒, <https://www.youtube.com/watch?v=p4t6O9uRX-U&list=PLt0SBi1p7xrRKE2us8doqryRou6eDY>
> - Reading: John Shawe-Taylor and Nello Cristianini, *Kernel Methods for Pattern Analysis*.
> - Reading: Bernhard Schölkopf and Alexander J. Smola, *Learning with Kernels*.

## 1. Basic Idea

Kernel Method 的核心思想是通过**非线性映射 (Non-linear Mapping)** 将原始数据映射到一个更高维的特征空间 (Feature Space), 使得在该空间中, 原本线性不可分的问题变得线性可分. 然后, 我们可以在这个高维空间中应用线性模型, 例如线性分类器或线性回归, 来处理数据.

具体地, 对于这样的线性不可分数据 $x$, 定义一个映射函数 $\phi: \mathbb{R}^d \to \mathcal{H}$, 将数据点 $x$ 映射到高维 Hilbert 空间 $\mathcal{H}$ 中. 此外定义一个核函数 $\kappa: \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$, 用于衡量输入数据点之间的相似性, 即映射后空间中对应点的内积:

$$
\kappa(x, z) = \langle \phi(x), \phi(z) \rangle.
$$

根据理论可以保证, 任意非线性可分的数据集, 只要选择合适的映射函数 $\phi$ 和核函数 $\kappa$, 就可以将其映射到一个高维空间中, 使得数据在该空间中线性可分. 这使得我们能够利用线性模型来处理复杂的非线性问题.

### 1.1 Feature Mapping

![A classic linearly non-separable problem can become linearly separable after mapping to a higher-dimensional feature space.](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/Figure_1.png)

- 对于原始 $\mathbb{R}^2$ 空间中的数据点 $(x_1, x_2)$, 我们需要使用非线性边界, 例如椭圆 $\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} = 1$, 来进行分类.
- 如果将数据映射到 $\mathbb{R}^3$ 空间, 使用映射函数 $\phi: \mathbb{R}^2 \to \mathbb{R}^3$, $(x_1, x_2) \mapsto (z_1, z_2, z_3) = (x_1^2 , x_2^2 , \sqrt{2} x_1 x_2)$, 则此时的椭圆形边界在新空间中变成了一个平面边界: $z_1/a^2 + z_2/b^2 = 1$.
- 因此, 通过适当的映射函数 $\phi$, 可以将原本线性不可分的问题转化为线性可分的问题.

### 1.2 Kernel Function

同样以上述映射为例, 关注映射前后数据点之间的内积关系.

在原始空间中, 两个数据点 $(x_1, x_2)$ 和 $(x_1', x_2')$ 之间的内积为:

$$
\langle x, x' \rangle = x_1 x_1' + x_2 x_2'.
$$

在映射后的空间中, 对应的两个数据点 $(z_1, z_2, z_3)$ 和 $(z_1', z_2', z_3')$ 之间的内积为:

$$
\langle \phi(x), \phi(x') \rangle = z_1 z_1' + z_2 z_2' + z_3 z_3' = (x_1 x_1' + x_2 x_2')^2.
$$

不难发现, 映射后空间中的内积可以通过原始空间中的内积来表示, 简记为 $\kappa (x, x') = \langle \phi(x), \phi(x') \rangle$. 这个函数 $\kappa(x, x')$ 被称为**核函数 (Kernel Function)**. 在本例中, 具体形式为 $\kappa(x, x') = (x_1 x_1' + x_2 x_2')^2 = (\langle x, x' \rangle)^2$.

**Definition (Kernel Function).** 称函数 $\kappa: \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$ 为 $\mathcal{X}$ 上的**核函数 (Kernel Function)**, 若存在 feature mapping $\phi: \mathcal{X} \to \mathcal{H}$, 使得对于任意 $x, x'\in \mathcal{X}$,

$$
\kappa(x, x') = \langle \phi(x), \phi(x') \rangle.
$$

因此, Kernel Function 变成了高维映射 $\phi$ 的一种替代表示. 只要知道核函数 $\kappa(x, x')$, 就等价于知道了映射 $\phi$ 后的内积关系. 若只关注高维空间中的内积运算, 则无需显式地知道映射 $\phi$ 本身. 这就是核方法的核心思想.

### 1.3 Geometry from Kernels

即使只知道 Feature Space 中的内积关系, 即核函数, 也能推导出一些最重要的几何性质, 例如距离和角度.

**Distance in Feature Space.**

$$
\begin{aligned}
d^2(\phi(x), \phi(x'))
&= \| \phi(x) - \phi(x') \|^2 \\
&= \langle \phi(x), \phi(x) \rangle - 2 \langle \phi(x), \phi(x') \rangle + \langle \phi(x'), \phi(x') \rangle \\
&= \kappa(x, x) - 2 \kappa(x, x') + \kappa(x', x').
\end{aligned}
$$

**Angle in Feature Space.**

$$
\begin{aligned}
\theta
&= \arccos \frac{\langle \phi(x), \phi(x') \rangle}{\|\phi(x)\| \|\phi(x')\|} \\
&= \arccos \frac{\kappa(x, x')}{\sqrt{\kappa(x, x) \kappa(x', x')}}.
\end{aligned}
$$

### 1.4 Gram Matrix

给定一组数据点 $\{x^{(1)}, x^{(2)}, \ldots, x^{(m)}\}$, 可以构造一个 $m \times m$ 的矩阵 $K$:

$$
K =
\begin{bmatrix}
\kappa(x^{(1)}, x^{(1)}) & \kappa(x^{(1)}, x^{(2)}) & \cdots & \kappa(x^{(1)}, x^{(m)}) \\
\kappa(x^{(2)}, x^{(1)}) & \kappa(x^{(2)}, x^{(2)}) & \cdots & \kappa(x^{(2)}, x^{(m)}) \\
\vdots & \vdots & \ddots & \vdots \\
\kappa(x^{(m)}, x^{(1)}) & \kappa(x^{(m)}, x^{(2)}) & \cdots & \kappa(x^{(m)}, x^{(m)})
\end{bmatrix}.
$$

这个矩阵 $K$ 被称为**内积矩阵 (Inner Product Matrix)**, **Gram 矩阵 (Gram Matrix)** 或 **核矩阵 (Kernel Matrix)**. 它包含了所有数据点在 Feature Space 中的内积信息, 因此可以用于计算距离和角度等几何性质.

## 2. Characterization of Kernels

核定理指出, 只要一个函数 $\kappa(x, x')$ 满足有限半正定条件, 就存在一个映射 $\phi$, 使得 $\kappa(x, x') = \langle \phi(x), \phi(x') \rangle$. 这意味着可以通过设计合适的核函数, 来隐式地定义一个高维映射 $\phi$, 而无需显式构造该映射.

**Theorem (Moore-Aronszajn Theorem).** 设 $\mathcal{X}$ 为任意非空集合, 若函数 $\kappa: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ 是对称函数. 则下列命题等价:

1. $\kappa$ 是有限半正定核 (PSD Kernel), 即对于任意有限点集 $\{x^{(1)}, x^{(2)}, \ldots, x^{(m)}\} \subset \mathcal{X}$ 及任意实数系数 $\{c_1, c_2, \ldots, c_m\} \subset \mathbb{R}$,

   $$
   \sum_{i=1}^m \sum_{j=1}^m c_i c_j \kappa(x^{(i)}, x^{(j)}) \geq 0.
   $$

2. 由 $\kappa$ 定义的 Gram 矩阵 $K$ 为半正定矩阵, $K\succeq 0$.
3. 存在一个 Hilbert 空间 $\mathcal{H}$ 和一个特征映射 $\phi: \mathcal{X} \to \mathcal{H}$, 使得对于任意 $x, x' \in \mathcal{X}$,

   $$
   \kappa(x, x') = \langle \phi(x), \phi(x') \rangle_{\mathcal{H}}.
   $$

故此定理保证了, 只要设计的核函数 $\kappa$ 满足有限半正定条件, 就一定存在一个对应的高维映射 $\phi$ 和 Hilbert 空间 $\mathcal{H}$, 使得 $\kappa(x, x')$ 可以表示为 $\phi(x)$ 和 $\phi(x')$ 在该空间中的内积.

### 2.1 Commonly Used Kernels

**Definition (Polynomial Kernel).** 对于任意 $x, x' \in \mathbb{R}^N$ 及常数 $c \geq 0$ 和整数 $d \geq 1$, 定义多项式核为:

$$
\kappa(x, x') = (x^\top x' + c)^d.
$$

例如 $N=2, d=2$, 则

$$
\begin{aligned}
\kappa(x, x')
&= (x_1 x_1' + x_2 x_2' + c)^2 \\
&= x_1^2 x_1'^2 + x_2^2 x_2'^2 + 2 x_1 x_1' x_2 x_2' + 2 c x_1 x_1' + 2 c x_2 x_2' + c^2 \\
&=
\begin{bmatrix}
x_1^2 \\
x_2^2 \\
\sqrt{2} x_1 x_2 \\
\sqrt{2 c} x_1 \\
\sqrt{2 c} x_2 \\
c
\end{bmatrix}^\top
\begin{bmatrix}
x_1'^2 \\
x_2'^2 \\
\sqrt{2} x_1' x_2' \\
\sqrt{2 c} x_1' \\
\sqrt{2 c} x_2' \\
c
\end{bmatrix}.
\end{aligned}
$$

对应的 feature mapping 为:

$$
\phi\left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}\right) =
\begin{bmatrix}
x_1^2 \\
x_2^2 \\
\sqrt{2} x_1 x_2 \\
\sqrt{2 c} x_1 \\
\sqrt{2 c} x_2 \\
c
\end{bmatrix}.
$$

事实上可以计算出, 对于任意 $N$ 维输入和 $d$ 次多项式核, 对应的 feature mapping $\phi$ 会将输入映射到一个维度为 $\binom{N+d}{d}$ 的空间中.

**Definition (Gaussian / RBF Kernel).** 对于任意 $x, x' \in \mathbb{R}^N$ 及常数 $\sigma > 0$, 定义高斯核为:

$$
\kappa(x, x') = \exp\left(-\frac{\|x - x'\|^2}{2 \sigma^2}\right).
$$

**Definition (Laplacian Kernel).** 对于任意 $x, x' \in \mathbb{R}^N$ 及常数 $\sigma > 0$, 定义拉普拉斯核为:

$$
\kappa(x, x') = \exp\left(-\frac{\|x - x'\|_1}{\sigma}\right).
$$

**Definition (Sigmoid Kernel).** 对于任意 $x, x' \in \mathbb{R}^N$ 及常数 $\alpha > 0$ 和 $c \in \mathbb{R}$, 定义 Sigmoid 核为:

$$
\kappa(x, x') = \tanh(\alpha x^\top x' + c).
$$

## 3. Dual Representation and Kernel Trick

考虑在 feature space $\mathcal{H}$ 中的线性函数 $f(x) = w^\top \phi(x) + b$, 其中 $w \in \mathcal{H}$, $b \in \mathbb{R}$. 我们希望仅通过核函数 $\kappa(x, x')$ 来表示这个函数 $f(x)$.

**Theorem (Representer Theorem).** 给定训练数据集 $\{(x^{(i)}, y^{(i)})\}_{i=1}^N$, 假设希望最小化以下正则化经验风险:

$$
J(w) = \sum_{i=1}^N L(y^{(i)}, f(x^{(i)})) + \lambda \|w\|^2,
$$

其中 $L$ 是损失函数, $\lambda > 0$ 是正则化参数. 则最优解 $w^*$ 可以表示为训练数据点在 feature space 中的线性组合:

$$
w^* = \sum_{i=1}^N \alpha_i \phi(x^{(i)}),
$$

其中 $\alpha_i \in \mathbb{R}$ 是系数.

换言之, 最优权重向量 $w^*$ 可以完全由训练数据点的映射 $\phi(x^{(i)})$ 线性组合而成, 即 $w^* \in \text{span}\{x^{(1)}, x^{(2)}, \ldots, x^{(N)}\}$. 这意味着可以将原始优化问题转化为关于系数 $\alpha_i$ 的优化问题.

将 $w^*$ 代入线性函数 $f(x)$ 中, 可得 dual representation:

$$
\begin{aligned}
f(\phi(x))
&= w^{*\top} \phi(x) + b \\
&= \left(\sum_{i=1}^N \alpha_i \phi(x^{(i)})\right)^\top \phi(x) + b \\
&= \sum_{i=1}^N \alpha_i \langle \phi(x^{(i)}), \phi(x) \rangle + b \\
&= \sum_{i=1}^N \alpha_i \kappa(x^{(i)}, x) + b.
\end{aligned}
$$

因此, 线性函数 $f(x)$ 可以表示为核函数 $\kappa(x^{(i)}, x)$ 的线性组合, 其中系数为 $\alpha_i$.

综上, 我们可以通过核函数 $\kappa(x, x')$ 来隐式地处理高维映射 $\phi$, 这就是所谓的**核技巧 (Kernel Trick)**.

## 4. Kernel-Based Linear Regression

给定训练数据集 $\{(\boldsymbol{x_i}, y_i)\}_{i=1}^N$, 其中 $\boldsymbol{x_i}\in \mathbb{R}^d$ 为输入特征, $y_i \in \mathbb{R}$ 为对应目标值. 给定一个核函数 $\kappa: \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$, 对应的映射函数为 $\phi: \mathbb{R}^d \to \mathcal{H}$.

输入矩阵为:

$$
{\Phi} :=
\begin{bmatrix}
1 & \phi(\boldsymbol{x_1})^\top \\
1 & \phi(\boldsymbol{x_2})^\top \\
\vdots & \vdots \\
1 & \phi(\boldsymbol{x_N})^\top
\end{bmatrix}
\in \mathbb{R}^{N \times (D+1)}.
$$

输出标签仍为 $\boldsymbol{y} = [y_1, y_2, \ldots, y_N]^\top \in \mathbb{R}^N$. 假设线性回归模型为:

$$
\boldsymbol{y} = {\Phi} \boldsymbol{w} + \boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}(0, \sigma^2 I).
$$

对应的 OLS 问题为 $\min_{\boldsymbol{w}}\;\|\boldsymbol{y}-\Phi\boldsymbol{w}\|_2^2$, 其 normal equation 为:

$$
\Phi^\top\Phi\,\hat{\boldsymbol{w}}=\Phi^\top\boldsymbol{y}.
$$

若 ${\Phi}^\top {\Phi}$ 可逆, 则有闭式解:

$$
\hat{\boldsymbol{w}} = \left({\Phi}^\top {\Phi}\right)^{-1} {\Phi}^\top \boldsymbol{y}.
$$

根据 Representer Theorem, 最优解 $\boldsymbol{w^*}$ 可以表示为训练数据点在特征空间中的线性组合, 即存在系数向量 $\boldsymbol{\alpha} \in \mathbb{R}^N$, 使得:

$$
\boldsymbol{w^*} = {\Phi}^\top \boldsymbol{\alpha}.
$$

为了求解 $\boldsymbol{\alpha}$, 将 $\boldsymbol{w^*}$ 代入 normal equation:

$$
\|\boldsymbol{y}-\Phi\boldsymbol{w^*}\|_2^2 = \|\boldsymbol{y}-\Phi{\Phi}^\top \boldsymbol{\alpha}\|_2^2.
$$

定义核矩阵 $K = \Phi \Phi^\top \in \mathbb{R}^{N \times N}$, 其中 $K_{ij} = 1 + \kappa(\boldsymbol{x_i}, \boldsymbol{x_j})$. 则上式可写为:

$$
\min_{\boldsymbol{\alpha}} \|\boldsymbol{y} - K \boldsymbol{\alpha}\|_2^2.
$$

对应的 normal equation 为:

$$
K^\top K \,\hat{\boldsymbol{\alpha}} = K^\top \boldsymbol{y}.
$$

若 $K$ 可逆, 则有闭式解:

$$
\hat{\boldsymbol{\alpha}} = K^{-1}  \boldsymbol{y}.
$$

对于任意新的输入样本 $\boldsymbol{x_*}$, 其预测值为:

$$
\begin{aligned}
\hat{y_*}
&= \phi(\boldsymbol{x_*})^\top \boldsymbol{w^*} \\
&= \phi(\boldsymbol{x_*})^\top {\Phi}^\top \hat{\boldsymbol{\alpha}} \\
&= \sum_{i=1}^N \hat{\alpha_i} \left(1 + \kappa(\boldsymbol{x_i}, \boldsymbol{x_*})\right).
\end{aligned}
$$

实践中往往通过 KRR (Kernel Ridge Regression) 来避免核矩阵 $K$ 不可逆的问题, 即在目标函数中加入正则化项 $\lambda \|\boldsymbol{\alpha}\|_2^2$:

$$
\boldsymbol{\alpha} = (K + \lambda I)^{-1} \boldsymbol{y}.
$$

## 5. RKHS and Representer Theorem

关于 RKHS, 我们最终想得到如下目标:

1. 从一个核函数 $\kappa$ 出发, 构造出一个以函数为元素的 Hilbert 空间 $\mathcal{H}$.
2. 该 Hilbert 空间 $\mathcal{H}$ 可以定义一个内积 $\langle \cdot, \cdot \rangle_{\mathcal{H}}$, 使得 $\kappa(x,z) = \langle \kappa(\cdot, x), \kappa(\cdot, z) \rangle_{\mathcal{H}}$.
3. 在该内积下, 任意函数 $f \in \mathcal{H}$ 满足再生性质: $f(x) = \langle f, \kappa(\cdot, x) \rangle_{\mathcal{H}}$.

为了达到这一目标, 整体思路为:

1. 首先定义 PSD 核函数 $\kappa$ 和对应的核截断 $\kappa(\cdot, x)$.
2. 利用核截断构造一个函数线性空间 $\mathcal{F}_\kappa$.
3. 在该函数空间上定义由 kernel 诱导的内积.
4. 用这个内积直接推出 reproducing property.
5. 最后对该空间进行完备化, 得到 RKHS.

更详细的 RKHS 定义和构造见 [RKHS and Representer Theorem](./RKHS-and-Representer-Theorem.md).

## Related Notes

- [RKHS and Representer Theorem](./RKHS-and-Representer-Theorem.md)
- [Support Vector Machine](../Classification/Support-Vector-Machine.md)
- [Regularization](../Linear/Regularization.md)
