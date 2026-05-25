---
title: "Linear Models for Classification"
aliases:
  - "Linear_Model_Classification"
  - "Logistics"
  - "Logistic Regression"
  - "Perceptron"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/classification
  - topic/linear-models
---

## 1. Logistic Regression

首先考虑二元分类问题.

沿用之前的记号, 我们希望通过对一系列特征 $x$ 的线性组合的某种函数形式 $h_{\theta}(x)$ 来预测 $y$. 在 0-1 分类问题中,

$$
h_\theta(x) = g(\theta^T x).
$$

其中, 记 $x_0=1$, 故

$$
\theta^T x= \sum_{i=0}^n \theta_i x_i.
$$

这里的 $g(z)$ 是一个将输出归一化到 $0$ 到 $1$ 区间的函数, 称为 logistic 函数. 其中一个比较常用的函数是 sigmoid 函数:

$$
g(\theta^T x) := \text{sigmoid} (\theta^T x) = \frac{1}{1+e^{-\theta^T x}}.
$$

特别指出, sigmoid 函数的导数形式具有较好的性质:

$$
\text{sigmoid}'(z) = \text{sigmoid}(z)(1-\text{sigmoid}(z)).
$$

### 1.1 Maximum Likelihood

由于 $y$ 是一个 0-1 变量, 而 $h_{\theta}$ 是 0 到 1 区间的连续取值, 因此可以将 $h_{\theta}$ 看成是 $y=1$ 的概率, 而 $1-h_{\theta}$ 是 $y=0$ 的概率, 即:

$$
p(y|x;\theta) = (h_{\theta}(x))^y(1-h_{\theta}(x))^{1-y}, \qquad y=0 \text{ or } 1.
$$

上面是针对一个样本例子而言的. 若进一步考虑所有样本, 假设样本之间独立同分布, 那么似然函数为:

$$
\begin{aligned}
L(\theta) &= \prod_{i=1}^n p(y^{(i)}|x^{(i)};\theta).
\end{aligned}
$$

进一步得到对数似然:

$$
\begin{aligned}
l(\theta)
&= \log L(\theta) \\
&= \sum_{i=1}^n \log p(y^{(i)}|x^{(i)};\theta) \\
&= \sum _{i=1}^n y^{(i)}\log h_\theta(x^{(i)}) + (1-y^{(i)})\log (1-h_\theta(x^{(i)})).
\end{aligned}
$$

### 1.2 Gradient Descent

在这里的极大值优化场景下, GD 为:

$$
\theta := \theta + \alpha \nabla_\theta l(\theta).
$$

因此得到 SGD 优化过程:

$$
\theta_j : = \theta_j + \alpha (y^{(i)} - h_\theta(x^{(i)}))x^{(i)}_j.
$$

若与 OLS 的 SGD 比较, 会发现二者的公式完全相同. 唯一变化的是这里的 $h_\theta(x^{(i)})$, 即预测值经过非线性的 sigmoid 函数映射, 而 OLS 中的 $h_\theta(x^{(i)})$ 为 $\theta^Tx^{(i)}$.

这也揭示二者都属于同一类算法, 即线性回归和逻辑回归都属于广义线性模型 (GLM).

### 1.3 Newton Method

Newton 法本身是用来求解函数零点的, 其具体形式为:

$$
\theta := \theta - \frac{f(\theta)}{f'(\theta)}.
$$

在优化算法中, 其本质原理在于目标函数的极值点可能出现在函数导数为 $0$ 的点. 因此我们借用 Newton 算法寻找导函数的零点. 在这种情况下的优化算法具体为:

$$
\theta := \theta - \frac{l'(\theta)}{l''(\theta)}.
$$

推广到 $\theta$ 为向量的情况则有:

$$
\theta:= \theta - H^{-1}\nabla_\theta l(\theta).
$$

其中 $H$ 为 Hessian 矩阵, 表示二阶导数矩阵:

$$
H_{ij} = \frac{\partial^2 l(\theta)}{\partial \theta_i \partial \theta_j}.
$$

牛顿法的收敛速度更快, 但由于要计算一个 Hessian 矩阵, 所以计算量更大.

这里通过牛顿法求解对数似然函数最大值的方法也称为 *Fisher scoring method*.

## 2. Perceptron

在处理 0-1 分类问题中, perceptron 规定 logistic 函数 $g$ 为:

$$
g(z) =
\begin{cases}
1 & \text{if } z \geq 0, \\
0 & \text{if } z<0.
\end{cases}
$$

因此以此可以得到 $h_\theta(x)  =g(\theta^T x)$ 及其更新函数:

$$
\theta_j := \theta_j + \alpha(y^{(i)} - h_\theta(x^{(i)}))x_j^{(i)}.
$$

目前为止, 分类问题有两种思路:

- 以 logistic regression 为代表: 通过数据学习概率 $p(y|x)$.
- 以 perceptron 为代表: 通过数据直接学习从数据特征 $\mathcal{X}$ 的空间到标签 $y\in\{-1,1\}$ 的映射.

## Related Notes

- [Linear Regression](./Linear.Linear-Regression.md)
- [Generalized Linear Models](./Linear.Generalized-Linear-Models.md)
- [Gaussian Discriminant Analysis](./Classification.Gaussian-Discriminant-Analysis.md)
