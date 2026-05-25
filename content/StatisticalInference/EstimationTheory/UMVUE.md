---
title: "UMVUE"
aliases:
  - "UMVUE"
  - "Uniform Minimum Variance Unbiased Estimator"
  - "一致最小方差无偏估计"
  - "StatisticalInference/UMVU.UMVUE"
course: "Statistical Inference"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-inference
  - topic/umvue
  - topic/estimation
---

## 1. Intuition

Suppose $\mathbf{X} = (X_1, \cdots, X_n)^T$ is a random sample from a distribution with pdf $f(\mathbf{x} | \theta)$. We want to estimate a parameter $\theta$ using $\hat{\theta}(\mathbf{X})$.

To evaluate the quality of $\hat{\theta}(\mathbf{X})$, we may introduce the metric

$$
\text{MSE}(\hat{\theta}(\mathbf{X})) = \mathbb{E}_{\mathbf{X}}[(\hat{\theta}(\mathbf{X}) - \theta)^2].
$$

In this metric,

$$
\hat{\theta}(\mathbf{X}) = \arg\min_{\theta} \text{MSE}(\hat{\theta}(\mathbf{X}))
$$

is the best estimator of $\theta$.

## 2. Definition and Criteria

**Definition (UMVUE).** An estimator $\hat{W}$ is a best unbiased estimator of $\tau(\theta)$ if it satisfies

$$
E[\hat{W}] = \tau(\theta) \quad \text{for all } \theta,
$$

and for any other estimator $W$ with $E[W] = \tau(\theta)$,

$$
\text{Var}(\hat{W}) \leq \text{Var}(W) \quad \text{for all } \theta.
$$

$\hat{W}$ is also called a **uniform minimum variance unbiased estimator (UMVUE)** of $\tau(\theta)$.

There are also some criteria for evaluating the quality of an estimator:

- **Ancillarity.** A statistic $S(\mathbf{X})$ whose distribution does not depend on the parameter $\theta$ is called an ancillary statistic. Such statistic has no information about $\theta$.

  **Example (Ancillary statistic).** If $X_1, X_2 \sim \mathcal{N}(\theta, 1)$, then $S(\mathbf{X}) = X_1-X_2 \sim \mathcal{N}(0, 2)$ is an ancillary statistic. It has no information about $\theta$.

- **Unbiasedness.** An estimator $\hat{\theta}(\mathbf{X})$ is unbiased if $\mathbb{E}_{\mathbf{X}}[\hat{\theta}(\mathbf{X})] = \theta$. Actually, there is no estimator that is uniformly optimal. In most cases, we constrain the estimator to be unbiased and find the best one among them.

- **Sufficiency.** Given $f(\mathbf{x},\theta)$, if $f(\mathbf{x},\theta| S(\mathbf{X}))$ is independent of $\theta$, then $S(\mathbf{X})$ is a sufficient statistic, as all the information about $\theta$ is contained in $S(\mathbf{X})$.

- **Completeness.** A statistic $T(\mathbf{X})$ is complete if for any function $g(t)$, $\mathbb{E}_{\theta}[g(T(\mathbf{X}))] = 0$ implies $g(t) = 0$ almost everywhere, i.e. $\mathbb{P}_{\theta}(g(T(\mathbf{X})) = 0) = 1$.

  **Theorem (Lehmann-Scheffé criterion).** If $T(\mathbf{X})$ is a complete and sufficient statistic, and $h(T(\mathbf{X}))$ is unbiased for $\theta$, then $h(T(\mathbf{X}))$ is the UMVUE of $\theta$.

## 3. Rao-Blackwell Procedure

Rao-Blackwell Procedure is a way to improve an estimator by using a sufficient statistic.

**Theorem (Rao-Blackwell Theorem).** Given an unbiased estimator $\hat{\theta}(\mathbf{X})$ for $\theta$, for any sufficient statistic $S(\mathbf{X})$, let

$$
\hat{\theta}_{RB}(\mathbf{X}) = \mathbb{E}_{\mathbf{X}}[\hat{\theta}(\mathbf{X})|S(\mathbf{X})].
$$

Then $\hat{\theta}_{RB}(\mathbf{X})$ is a better estimator of $\theta$ than $\hat{\theta}(\mathbf{X})$, as

$$
\text{Var}(\hat{\theta}_{RB}(\mathbf{X})) \leq \text{Var}(\hat{\theta}(\mathbf{X})).
$$

Equivalently,

$$
\text{MSE}(\hat{\theta}_{RB}(\mathbf{X})) \leq \text{MSE}(\hat{\theta}(\mathbf{X})).
$$

## 4. Cramér-Rao Lower Bound

Starting from ancillary statistics, we can derive a better and better estimator by the Rao-Blackwell procedure. Is there a limit for the quality of an estimator? The answer is yes, and it is the Cramér-Rao Lower Bound.

Here, we first give a simple version of Cramér-Rao Lower Bound, where we only focus on the parameter $\theta$ rather than a function of $\theta$.

**Theorem (Cramér-Rao Lower Bound, simple version).** Given a random sample $\mathbf{X} = (X_1, \cdots, X_n)^T$ from a distribution with pdf $f(\mathbf{x}|\theta)$. Then for any unbiased estimator $\hat{\theta}(\mathbf{X})$,

$$
\text{Var}(\hat{\theta}(\mathbf{X})) \geq \frac{1}{nI(\theta)},
$$

where $I(\theta)$ is the Fisher Information of $\theta$:

$$
I(\theta) = \mathbb{E}_{\theta}\left[\left(\frac{\partial}{\partial\theta}\log f(\mathbf{X}|\theta)\right)^2\right] = -\mathbb{E}_{\theta}\left[\frac{\partial^2}{\partial\theta^2}\log f(\mathbf{X}|\theta)\right].
$$

## Related Notes

- [Sufficiency](../InformationAndSufficiency/Sufficiency.md)
- [Rao-Blackwell Theorem](./Rao-Blackwell-Theorem.md)
- [Lehmann-Scheffé Theorem](./Lehmann-Scheffe-Theorem.md)
- [Cramér-Rao Lower Bound](./Cramer-Rao-Lower-Bound.md)
- [Fisher Information](../InformationAndSufficiency/Fisher-Information.md)
