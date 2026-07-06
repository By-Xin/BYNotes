---
title: "Fisher Information"
aliases:
  - "Fisher_Information"
  - "Fisher信息"
  - "费舍尔信息量"
  - "StatisticalInference/Information.Fisher-Information"
course: "Statistical Inference"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-inference
  - topic/fisher-information
  - topic/estimation
---

## 1. Definition

**Definition (Fisher Information).** Given a random sample $\mathbf{X} = (X_1, \cdots, X_n)^T$ from a distribution with pdf $f(\mathbf{x}|\theta)$. Accordingly, calculate the joint pdf / likelihood function and take the logarithm to get the log-likelihood function:

$$
l(\theta) = \log f(\mathbf{X}|\theta) = \sum_{i=1}^n \log f(X_i|\theta).
$$

Then the Fisher Information of $\theta$ is defined as

$$
\mathcal{I}(\theta) = \mathbb{E}_{\theta}\left[\left(\frac{\partial}{\partial\theta} l(\theta)\right)^2\right] = -\mathbb{E}_{\theta}\left[\frac{\partial^2}{\partial\theta^2} l(\theta)\right].
$$

## 2. Identity Between the Two Forms

> [!proof]+ Proof of the last equation
> For pdf of $x$, $\int_\mathbb{R} f({x}; \theta)\,\mathrm{d}{x} \equiv 1$. Take the derivative with respect to $\theta$ on both sides:
>
> $$
> \begin{aligned}
> 0 &= \int_\mathbb{R} \frac{\partial}{\partial\theta} f({x}; \theta) \,  \mathrm{d}{x}  \\
> &= \int_\mathbb{R} \left(\frac{\partial}{\partial\theta}\log f({x}; \theta)\right) f({x}; \theta) \,  \mathrm{d}{x} \quad \small\text{(Fisher Trick)}.
> \end{aligned}
> $$
>
> Take the derivative with respect to $\theta$ again on both sides:
>
> $$
> \begin{aligned}
> 0 &= \int_\mathbb{R} \frac{\partial}{\partial\theta} \left(\frac{\partial \log f({x}; \theta)}{\partial\theta}\cdot f({x}; \theta) \right)\,  \mathrm{d}{x}  \\
> &= \int_\mathbb{R} \frac{\partial^2}{\partial\theta^2}\log f({x}; \theta) f({x}; \theta) \,  \mathrm{d}{x} \\
> &\quad + \int_\mathbb{R} \left(\frac{\partial}{\partial\theta}\log f({x}; \theta)\right) \cdot \left(\frac{\partial}{\partial\theta} f({x}; \theta)\right) \,  \mathrm{d}{x} \\
> &= \mathbb{E}\left[\frac{\partial^2}{\partial\theta^2}\log f(\mathbf{X}; \theta)\right] + \underbrace{\int_\mathbb{R} \left(\frac{\partial}{\partial\theta}\log f({x}; \theta)\right) \cdot \left(\frac{\partial}{\partial\theta} f({x}; \theta)\right) \,  \mathrm{d}{x}}_\triangle.
> \end{aligned}
> $$
>
> Recall the Fisher trick:
>
> $$
> \frac{\partial}{\partial\theta} f({x}; \theta) = \frac{\partial}{\partial\theta}\log f({x}; \theta) \cdot f({x}; \theta).
> $$
>
> The term $\triangle$ can be written as
>
> $$
> \begin{aligned}
> \triangle
> &= \int_\mathbb{R} \left(\frac{\partial}{\partial\theta}\log f({x}; \theta)\right) \cdot \left(\frac{\partial}{\partial\theta}\log f({x}; \theta)\cdot f({x}; \theta)\right) \,  \mathrm{d}{x} \\
> &= \mathbb{E}\left[\left(\frac{\partial}{\partial\theta}\log f(\mathbf{X}; \theta)\right)^2\right].
> \end{aligned}
> $$
>
> Thus,
>
> $$
> 0 = \mathbb{E}\left[\frac{\partial^2}{\partial\theta^2}\log f(\mathbf{X}; \theta)\right] + \mathbb{E}\left[\left(\frac{\partial}{\partial\theta}\log f(\mathbf{X}; \theta)\right)^2\right].
> $$
>
> $\square$

> [!note] Note: Fisher information conventions
> There are several ways to define Fisher Information.
>
> - The first one is derived directly from the pdf of a distribution, i.e. the population distribution.
> - The second way is to view it from a sampling perspective. Then $f(\mathbf{x}|\theta)$ is replaced by the likelihood function $L(\theta|\mathbf{x})$, or regarded as the pdf of the joint distribution.
>
> In the likelihood convention,
>
> $$
> \tilde I(\theta) = \mathbb{E}_{\theta}\left[\left(\frac{\partial}{\partial\theta}\log L(\theta|\mathbf{X})\right)^2\right] = -\mathbb{E}_{\theta}\left[\frac{\partial^2}{\partial\theta^2}\log L(\theta|\mathbf{X})\right].
> $$
>
> The two definitions are essentially equivalent, as the likelihood function is just the pdf of the sample:
>
> $$
> \frac{\partial \log L(\theta|\mathbf{X})}{\partial\theta} = \sum_{i=1}^n \frac{\partial \log f(X_i|\theta)}{\partial\theta}.
> $$
>
> Thus for Fisher Information,
>
> $$
> \tilde I(\theta) = nI(\theta).
> $$
>
> We have to pay attention to the dimension or meaning of the function when calculating Fisher Information, and we have to be consistent. Usually, the log-likelihood function is used in practice.

## Related Notes

- [Cramér-Rao Lower Bound](../EstimationTheory/Cramer-Rao-Lower-Bound.md)
- [Sufficiency](./Sufficiency.md)
- [UMVUE](../EstimationTheory/UMVUE.md)
