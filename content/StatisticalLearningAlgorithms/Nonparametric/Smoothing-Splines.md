---
title: "Smoothing Splines"
aliases:
  - "Smoothing_Splines"
  - "Smoothing Splines"
  - "StatisticalLearningAlgorithms/Nonparametric.Smoothing-Splines"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/nonparametric-models
  - topic/splines
---

## 1. Introduction

- When fitting a model, usually we tend to minimize the residual sum of squares (RSS) to get the best fit:

  $$
  \mathrm{RSS} = \sum_{i=1}^N (y_i - g(x_i))^2,
  $$

  where $g(x_i)$ is the predicted value at $x_i$.

- However, we could always squeeze the RSS to $0$ by interpolating all the data points if there is no constraint. This would lead to overfitting.
- Thus, apart from minimizing the RSS, we also want $g$ to be smooth. This is the idea of smoothing splines.

### 1.1 Smoothing Splines

Smoothing splines are to find $g$ that minimizes

$$
\sum_{i=1}^N (y_i - g(x_i))^2 + \lambda \int g''(t)^2 dt,
$$

where $\lambda$ is a nonnegative tuning parameter.

- It takes the form of $\text{Loss} + \lambda \times \text{Penalty}$.
- The penalty term is a roughness penalty that penalizes the wiggliness of $g$.
  - $g''(t)$ is the second derivative of $g$; it measures the amount by which $g$ is not linear, or the curvature of $g$, i.e. how fast $g$'s slope is changing.
  - $\int g''(t)^2 dt$ is the integral of $g''(t)^2$ over the range of $t$; it measures the total change in the slope of $g$ over its entire range.
  - If $g$ is very smooth, then $g'(t)$ is nearly constant, and $g''(t)$ is nearly $0$, so the penalty term is small.
  - If $g$ is very wiggly, then $g''(t)$ is large, and the penalty term is large.
- $\lambda$ controls the trade-off between the two terms, i.e. the bias-variance trade-off.
  - If $\lambda = 0$, then it degenerates to the least squares fit, and consequently leads to interpolation.
  - If $\lambda \rightarrow \infty$, then the penalty term dominates the loss term, and $g$ will be a straight line that passes as closely as possible to the points.

It can be further proved that the solution to the above problem is a **natural cubic spline** with knots at each of the training observations $x_1,\cdots,x_N$.

## 2. Choosing the Smoothing Parameter $\lambda$

- In smoothing splines, $\lambda$ is a tuning parameter that controls the amount of smoothing.
- As $\lambda$ increases from $0$ to $\infty$, the effective degrees of freedom $df_{\lambda}$ decreases from $N$ to $2$.

### 2.1 Effective Degrees of Freedom

Here we try to give a technical definition of effective degrees of freedom.

First, recall the notation. We want to find $g$ that minimizes

$$
\sum_{i=1}^N (y_i - g(x_i))^2 + \lambda \int g''(t)^2 dt,
$$

where $\lambda$ is a nonnegative tuning parameter.

Note the optimal $g(\cdot)$ given a certain $\lambda$ as $g_{\lambda}(\cdot)$, and accordingly the predicted value as $\hat g_{\lambda} \in \mathbb{R}^N$.

It can be proved that

$$
\hat g_{\lambda} = S_{\lambda} y,
$$

where $S_{\lambda}$ is a $N\times N$ matrix that projects the response vector $y$ onto $\hat g_{\lambda}$.

Finally, define the effective degrees of freedom as

$$
\text{df}_{\lambda} = \text{trace}(S_{\lambda}).
$$

### 2.2 Choosing $\lambda$ by Cross-Validation

In smoothing splines, the location of the knots is fixed at the training observations. Yet we have to define the smoothing parameter $\lambda$.

Here we apply LOOCV (leave-one-out cross-validation) to choose $\lambda$, i.e. to minimize

$$
\text{RSS}_{cv} = \sum_{i=1}^N (y_i - \hat g_{\lambda}^{(-i)}(x_i))^2 = \sum_{i=1}^N \left(\frac{y_i - \hat g_{\lambda}(x_i)}{1-S_{\lambda,ii}}\right)^2,
$$

where $\hat g_{\lambda}^{(-i)}$ is the fit obtained from the original data without the $i$th observation $(x_i,y_i)$, and $g_{\lambda}$ is the fit obtained from all of the original data.

The proof of the second equality is sophisticated, yet the conclusion is simple: **the LOOCV error can be computed using the original fit, without having to refit for each value of $\lambda$.**

## Related Notes

- [Regression Splines](./Regression-Splines.md)
- [Step Functions](./Step-Functions.md)
