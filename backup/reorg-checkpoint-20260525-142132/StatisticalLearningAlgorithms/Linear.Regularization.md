---
title: "Regularization"
aliases:
  - "Regularization"
  - "Ridge Regression"
  - "LASSO"
  - "Elastic Net"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/regularization
  - topic/linear-models
---

> [!quote] References
> - Lecture: 张颢, <https://www.bilibili.com/video/BV1ga4y157L5?p=8&vd_source=8a00dab0be94d29388f2286892ba8d50>

## 1. Ridge Regression / Tikhonov Regularization

沿用 Note 4 的记号, 我们的目标是最小化:

$$
\begin{aligned}
\min_{f_X} \quad & \frac1n \sum_{k=1}^n L(f_X(x_k), y_k) \\
\text{s.t.} \quad & f_X(x) \in \mathcal{F}.
\end{aligned}
$$

经过一定的泛函等技巧, 并确定 MSE 为 loss 的具体形式, 以线性情况为例, 可以得到:

$$
\begin{aligned}
\min_{\theta} \quad & \frac1n \sum_{k=1}^n (y_k - \theta^T x_k)^2 \\
\text{s.t.} \quad & \theta \in \Omega.
\end{aligned}
$$

参考 bias-variance tradeoff, 我们需要尽可能简化模型的形式. 在经过泛函对应后, 即为限制 $\theta$ 的大小. 这里最开始是以二范数为例, 即得到 Tikhonov Regularization 的形式:

$$
\begin{aligned}
\min_{\theta} \quad & \frac1n \sum_{k=1}^n (y_k - \theta^T x_k)^2 \\
\text{s.t.} \quad & \|\theta\|_2^2 \leq r.
\end{aligned}
$$

对其具体形式进行进一步求解:

$$
\begin{aligned}
\min_{\theta} \quad & (X\theta - y)^T(X\theta - y) \\
\text{s.t.} \quad & \theta^T\theta \leq r.
\end{aligned}
$$

再次引入 Lagrange 乘子, 得到:

$$
\begin{aligned}
L(\theta, \lambda) &= (X\theta - y)^T(X\theta - y) + \lambda(\theta^T\theta - r), \\
\nabla_{\theta} L(\theta, \lambda) &= \cdots = 2X^TX\theta - 2X^Ty + 2\lambda\theta = 0, \\
\Rightarrow \quad & \theta_{\text{Ridge}} = (X^TX + \underbrace{\lambda I}_{\text{Diagonal Loading}})^{-1}X^Ty.
\end{aligned}
$$

说明:

- OLS 的最小二乘解是 unbiased 的, 然而这里的结果是有偏的.
- 正如 bias-variance tradeoff 所说, 这里通过牺牲一定的 bias 来降低 variance, 从而提高整体的泛化能力, 因为 variance 更无法控制.

### 1.1 SVD and L2 Regularization

**SVD 原理.**

- 对于对称矩阵 $A=A^T$:

  $$
  A = U\Lambda U^T = \sum_{i=1}^n \lambda_i u_i u_i^T,
  $$

  其中 $\Lambda=\text{diag}(\lambda_1,\ldots,\lambda_n)$, $UU^T=I$.

- 对于 normal 矩阵 $A^TA=AA^T$:

  $$
  A = U^{-1}\Lambda U,
  $$

  其中 $\Lambda=\text{diag}(\lambda_1,\ldots,\lambda_n)$, $UU^{-1}=I$.

- 对于一般方阵:

  $$
  A = U^{-1}\Lambda U,
  $$

  其中 $\Lambda=\text{diag}(J_1,\ldots,J_k)$, $J_k$ 为 Jordan Block. 这里称 $\Lambda$ 为 *Jordan Canonical Form*.

- **Singular Value Decomposition.** 对于一般矩阵 $A \in \mathbb R^{m\times n}$:

  $$
  A = U\Sigma V^T,
  $$

  其中 $UU^T = I$, $VV^T = I$, $\Sigma = \begin{bmatrix} \Lambda & 0 \\ 0 & 0 \end{bmatrix}$; 且 $\Lambda$ 为一个 diagonal matrix, 其阶对应着 $A$ 的 rank.

**SVD 解释 L2 Regularization.**

已知 Ridge Regression 结果:

$$
\theta_{\text{Ridge}} = (X^TX + \lambda I)^{-1}X^Ty.
$$

对 $X$ 进行 SVD, 假设 column full rank:

$$
\begin{aligned}
X &= U\Sigma V^T, \\
\text{where } \Sigma &= \begin{bmatrix} \Lambda \\ 0 \end{bmatrix} \text{ thus } \Sigma^T\Sigma = \Lambda^2.
\end{aligned}
$$

因而有:

$$
X^TX = V\Sigma^T U^T U\Sigma V^T = V\Sigma^T \Sigma V^T  = V \Lambda^2 V^T.
$$

代入 Ridge Regression 结果:

$$
\begin{aligned}
(X^TX + \lambda I)^{-1}&= (V \Lambda^2 V^T + \lambda VV^T)^{-1} = V {(\Lambda^2 + \lambda I)} ^{-1}V^T.
\end{aligned}
$$

其中 ${(\Lambda^2 + \lambda I)}$ 是一个对角矩阵, 其逆是方便求解的.

故:

$$
\begin{aligned}
\theta_{\text{Ridge}}
&= (X^TX + \lambda I)^{-1}X^Ty \\
&= V {(\Lambda^2 + \lambda I)} ^{-1}V^T V \Sigma U^T y \\
&= V \left({(\Lambda^2 + \lambda I)} ^{-1} \Sigma \right)\left( U^T y \right) \\
&= V
\begin{bmatrix}
\frac{\lambda_1}{\lambda_1^2 + \lambda} & 0 & \cdots & 0 \\
0 & \frac{\lambda_2}{\lambda_2^2 + \lambda} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \frac{\lambda_n}{\lambda_n^2 + \lambda}
\end{bmatrix} U^T y \\
&= \sum_{i=1}^n \boxed{\frac{\lambda_i}{\lambda_i^2 + \lambda}} u_i u_i^T y \\
&:= \sum_{i=1}^n \boxed{\frac{\lambda_i}{\lambda_i^2 + \lambda}} ~ \tilde y_i.
\end{aligned}
$$

从这里可见:

- $\lambda = 0$ 就相当于原始 OLS, 也就是对 $y$ 进行一个坐标变换.
- $\lambda$ 很大时, 参照 Lagrange 函数, 发现相当于惩罚使得前项并不重要.
- $\lambda$ 在正常范围内时, $\lambda_i$ 需要纳入考量.
  - 这里的 $\lambda_i$ 是数据特征矩阵 $X$ SVD 的结果, 相当于是数据的特征.
  - $\lambda_i$ 作为 SVD 的结果表示对应数据的权重. 当 $\lambda_i$ 较大时, $\lambda$ 对于数值的影响较小.
  - 反之 $\lambda_i$ 较小时, 说明这些数据本身对于原训练集的重要性不那么大, 有可能这些 feature 本身就是噪声. 这时 $\lambda$ 相对起到关键作用.
  - 当 $\lambda_i$ 较小时, 分母上为 $\lambda_i^2$, 更小, 因此原先可能出现数值不稳定的情况, 即几乎不可逆等. $\lambda$ 的引入控制了这个问题.

> [!note] Note: Link to Laplace smoothing
> This stabilization role is reminiscent of Laplace smoothing.

## 2. LASSO Regularization

- **Ridge.** 回顾 L2 regularization 的优化目标:

  $$
  \begin{aligned}
  \min_{\theta} \quad & (X\theta - y)^T(X\theta - y) \\
  \text{s.t.} \quad & \theta^T\theta \leq r.
  \end{aligned}
  $$

  可以发现, 其可行域 $\theta^T\theta \leq r$ 为一个圆形区域; 其解集 $(X\theta - y)^T(X\theta - y)$ 为一系列关于 $\theta$ 的二次曲线.

  事实上, 椭圆等高线与圆形可行域相切的点即为最优解.

- **LASSO (Least Absolute Shrinkage and Selection Operator).** Tibshirani, 1996.

  与 Ridge Regression 相比, LASSO 的惩罚项为 L1 范数:

  $$
  \begin{aligned}
  \min_{\theta} \quad & \frac1n \sum_{k=1}^n (y_k - \theta^T x_k)^2 \\
  \text{s.t.} \quad & \|\theta\|_1 \leq r.
  \end{aligned}
  $$

  因此其可行域为菱形, 而等高线不变.

  与 Ridge Regression 相比, LASSO 的解更容易出现在坐标轴附近, 因此更加稀疏, 即更多的 $\theta_i$ 为 $0$.

  LASSO 对模型起到了 **selection** 的作用, 而且这种变量选择是自动的.

## 3. $L_q$ Regularization and Elastic Net

### 3.1 $L_q$ Regularization

其约束形式为

$$
\|\theta\|_q \leq r.
$$

### 3.2 Elastic Net

其约束形式为

$$
\alpha \|\theta\|_1 + (1-\alpha) \|\theta\|_2 \leq r.
$$

## 4. Regularization Theory

### 4.1 Weight Decay

- 上面提到的 L1, L2 等都是通过限制参数的大小实现其目的, 即 weight decay.
- Weight decay 只是 regularization 的一种.

### 4.2 Dropout

- 为了保证模型的泛化能力及其弹性, 有时在一定的训练后会随机去掉一定数据, 这就是 dropout.
- Dropout 相当于一个随机 selection.

### 4.3 Noise Injection

- 在 CV 等训练过程中, 可以注入一定的噪声信息, 从而提高模型的鲁棒性.
- 事实上, Ridge Regression 也是广义的 noise injection 的一种.

## Related Notes

- [Linear Regression](./Linear.Linear-Regression.md)
- [Kernel Methods](./Kernel.Kernel-Methods.md)
- [Naive Bayes Classifier](./Classification.Naive-Bayes-Classifier.md)
