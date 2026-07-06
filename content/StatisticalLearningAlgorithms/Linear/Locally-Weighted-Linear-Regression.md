---
title: "Locally Weighted Linear Regression"
aliases:
  - "Locally_Weighted_Linear_Regression"
  - "LWLR"
  - "LWR"
  - "局部线性回归"
  - "StatisticalLearningAlgorithms/Linear.Locally-Weighted-Linear-Regression"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/linear-models
  - topic/regression
  - topic/nonparametric-regression
---

## 1. Motivation

希望在设计回归方程时, 若考虑当前某点的作用, 希望距离该点临近的点提供更大的信息权重, 距离该点较远的点提供较小的信息权重.

### 1.1 Underfitting and Overfitting

- underfitting
- overfitting

## 2. LWR Loss Function

$$
J(\theta) = \sum_i \omega^{(i)}(y^{(i)} - \theta^T x^{(i)})^2.
$$

$\omega^{(i)}$ 是人为设计的一个参数, 其中一种比较成熟的设计为[[Kernel-Methods|高斯核]]:

$$
\omega^{(i)} = \exp \left( - \frac{ (x^{(i)} - x) ^2}{2 \tau^2} \right).
$$

其中称 $\tau$ 为带宽, 用来控制 $\omega^{(i)}$ 的衰减速度. $\tau$ 越大, $\omega^{(i)}$ 衰减越慢; $\tau$ 越小, $\omega^{(i)}$ 衰减越快.

若用矩阵形式表达, 则为:

$$
J(\theta) = (y - X\theta)^T W (y-X\theta).
$$

$$
\theta = (X^{T}WX)^{-1}X^{T}Wy.
$$

## 3. Python Implementation

记数据样本量为 $m$.

```python
# coding = utf-8
import numpy as np
import scipy.stats as stats
from math import *
import matplotlib.pyplot as plt

def getw(x0, x, k):
    """
    :param x0: 1*m is the current sample point
    :param x: n*m is the whole sample set
    :param k: Gaussian kernel bandwidth, i.e. tau
    :return: w: n*n
    """
    w = np.zeros([m, m])
    for i in range(m):
        w[i, i] = exp((np.linalg.norm(x0 - x[i]) ** 2) / (-2 * k ** 2))
    return w

def getyvalue(x1, x, y, k):
    """
    :param x1: n*2
    :param x: m*2
    :param y: m*1
    :param k: Gaussian kernel bandwidth, i.e. tau
    """
    y_value = np.zeros(m)
    w = np.zeros([m, m])

    for i in range(m):
        w = getw(x[i], x, k)
        theta = np.linalg.inv(x1.T.dot(w).dot(x1)).dot(x1.T).dot(w).dot(y)
        y_value[i] = theta[0] + theta[1] * x[i]
    return y_value

if __name__ == "__main__":
    x = np.arange(1, 101)
    x = np.array([float(i) for i in x])
    y = x + [10 * sin(0.3 * i) for i in x] + stats.norm.rvs(size=100, loc=0, scale=1.5)

    x = x.reshape(-1, 1)
    x1 = np.c_[np.ones((100, 1)), x]
    y = y.reshape(-1, 1)
    m = len(x)

    y_lwlr = np.zeros(m)
    y_lwlr = getyvalue(x1, x, y, k=1.2)
    plt.figure(figsize=(12, 6))
    plt.scatter(x, y)
    plt.plot(x, y_lwlr, "r")
    plt.show()
```

说明:

- 在上面的代码实现中, 并没有使用循环迭代收敛求解, 而是通过类似统计学的方法推导出 LWLR 的解析解, 直接通过矩阵计算完成. 代码中的循环都是为了生成矩阵元素等.
- 全部计算流程和典型的 $(X^TX)^{-1}X^TY$ 别无二致, 只不过相比之下多了几个关于 $X$ 的运算.
- 这个运算相当于每次提取一个样本, 和全部样本集合进行一个矩阵运算, 再通过 Gaussian 核得到一个权重, 记为权重矩阵的一个元素, 以此类推得到整个权重.

## Related Notes

- [Linear Regression](./Linear-Regression.md)
- [Step Functions](../Nonparametric/Step-Functions.md)
- [Smoothing Splines](../Nonparametric/Smoothing-Splines.md)
