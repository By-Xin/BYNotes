---
title: "Linear Regression"
aliases:
  - "Linear_Regression"
  - "OLS"
  - "Ordinary Least Squares"
  - "StatisticalLearningAlgorithms/Linear.Linear-Regression"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/linear-models
  - topic/regression
---

## 1. OLS

$$
h(x) = \sum_{i=0}^n \theta_i x_i = \theta^T x.
$$

其中称 $\theta$ 为参数; 特别地, $\theta_0$ 称为截距项 (intercept term), 其对应的 $x$ 为 $1$.

### 1.1 OLS Cost Function

$$
J(\theta) = \frac{1}{2}\sum_{i=1}^{n}(h_{\theta}(x^{(i)})-y^{(i)})^2.
$$

### 1.2 Gradient Descent

[[5.Gradient-Descent|Gradient descent 的一般形式]]:

$$
\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta).
$$

其中 $j=1,2,\ldots,p$, 也就是同步更新所有的特征.

#### 1.2.1 OLS Case

对损失函数关于某个特征求偏导有:

$$
\begin{aligned}
\frac{\partial}{\partial \theta_{j}} J(\theta)
&=\frac{\partial}{\partial \theta_{j}} \frac{1}{2}\left(h_{\theta}(x)-y\right)^{2} \\
&=2 \cdot \frac{1}{2}\left(h_{\theta}(x)-y\right) \cdot \frac{\partial}{\partial \theta_{j}}\left(h_{\theta}(x)-y\right) \\
&=\left(h_{\theta}(x)-y\right) \cdot \frac{\partial}{\partial \theta_{j}}\left(\sum_{i=0}^{n} \theta_{i} x_{i}-y\right) \\
&=\left(h_{\theta}(x)-y\right) \cdot x_{j}.
\end{aligned}
$$

因此对于一个样本 $i$ 的每个特征 $j$, 梯度下降的更新公式为:

$$
\theta_{j}:=\theta_{j}+\alpha\left(y^{(i)}-h_{\theta}(x^{(i)})\right) \cdot x_{j}^{(i)}.
$$

这一更新公式符合最小均方误差 (MSE), 因此也称为 LMS (least mean square) 更新规则, 或 Widrow-Hoff 规则.

#### 1.2.2 Batch Gradient Descent

算法描述:

```text
Repeat until convergence {
  θ := θ + α Σᵢ₌₁ⁿ (y⁽ⁱ⁾ - hθ(x⁽ⁱ⁾))x⁽ⁱ⁾
}
```

对应更新式为:

$$
\theta := \theta + \alpha \sum_{i=1}^n (y^{(i)} -  h_\theta(x^{(i)}))x^{(i)}.
$$

批量梯度下降法每次迭代都要用到所有训练样本, 所以当训练集很大时会很慢.

#### 1.2.3 Stochastic Gradient Descent

算法描述:

```text
Loop {
  for i = 1 to n {
    θ := θ + α(y⁽ⁱ⁾ - hθ(x⁽ⁱ⁾))x⁽ⁱ⁾
  }
}
```

对应更新式为:

$$
\theta := \theta + \alpha(y^{(i)} - h_\theta(x^{(i)}))x^{(i)}.
$$

随机梯度下降法每次只用一个样本来更新参数, 而不是用所有样本.

## 2. Matrix Calculus Notes

定义:

$$
\nabla_A f(A) =
\begin{bmatrix}
\frac{\partial f}{\partial A_{11}} & \frac{\partial f}{\partial A_{12}} & \cdots & \frac{\partial f}{\partial A_{1n}} \\
\frac{\partial f}{\partial A_{21}} & \frac{\partial f}{\partial A_{22}} & \cdots & \frac{\partial f}{\partial A_{2n}} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f}{\partial A_{m1}} & \frac{\partial f}{\partial A_{m2}} & \cdots & \frac{\partial f}{\partial A_{mn}}
\end{bmatrix}.
$$

例如, 若 $f(A) = \frac23 A_{11} + 5A_{12}^2 + A_{21}A_{22}$, 则

$$
\nabla_A f(A) =
\begin{bmatrix}
\frac23 & 10A_{12} \\
A_{22} & A_{21}
\end{bmatrix}.
$$

> [!note] Note: Source omission
> The original note marks the later statistics discussion as omitted.

## Related Notes

- [Locally Weighted Linear Regression](./Locally-Weighted-Linear-Regression.md)
- [Regularization](./Regularization.md)
- [Linear Models for Classification](../Classification/Linear-Models-for-Classification.md)
