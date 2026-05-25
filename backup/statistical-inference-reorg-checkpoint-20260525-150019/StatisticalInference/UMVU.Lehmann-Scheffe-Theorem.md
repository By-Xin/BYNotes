---
title: "Lehmann-Scheffé Theorem"
aliases:
  - "Lehmann-Scheffe_Theorem"
  - "Lehmann-Scheffé_Theorem"
  - "Lehmann-Scheffé Theorem"
course: "Statistical Inference"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-inference
  - topic/umvue
  - topic/sufficiency
---

## 1. Statement

**Theorem (Lehmann-Scheffé Theorem).** Let $\mathbf{X} = (X_1, \cdots, X_n)^T$ be a random sample from a distribution with pdf $f(\mathbf{x} | \theta)$. Suppose $T(\mathbf{X})$ is a complete and sufficient statistic for $\theta$, and $h(T(\mathbf{X}))$ is unbiased for $\theta$. Then $h(T(\mathbf{X}))$ is the unique UMVUE of $\theta$.

## 2. Proof

> [!proof]+ Proof
> Given such $T$, we have to show that for all $\hat{\theta}$ such that $\mathbb{E}[\hat{\theta}] = \theta$, we have $\text{MSE} (h(T)) \leq \text{MSE}(\hat{\theta})$.
>
> According to the Rao-Blackwell Theorem,
>
> $$
> \hat{\theta}_{RB} = \mathbb{E}[\hat{\theta} | T] = \tilde{\theta}(T).
> $$
>
> Then it is a better estimator than $\hat{\theta}$:
>
> $$
> \text{MSE}(\hat{\theta}_{RB}) = \text{MSE}(\tilde{\theta}(T)) \leq \text{MSE}(\hat{\theta}).
> $$
>
> Moreover, both $\hat{\theta}_{RB}$ and $h(T)$ are unbiased for $\theta$:
>
> $$
> \mathbb{E}[h(T) - \tilde{\theta}(T)] = 0.
> $$
>
> Since $T$ is complete and $h(T) - \tilde{\theta}(T)$ is a function of $T$, we have $h(T) = \tilde{\theta}(T)$ almost everywhere.
>
> Therefore, $h(T)$ is the unique UMVUE of $\theta$:
>
> $$
> \text{MSE}(h(T)) = \text{MSE}(\tilde{\theta}(T)) \leq \text{MSE}(\hat{\theta}).
> $$
>
> $\square$

## Related Notes

- [Rao-Blackwell Theorem](./UMVU.Rao-Blackwell-Theorem.md)
- [Sufficiency](./Sufficiency.Sufficiency.md)
- [UMVUE](./UMVU.UMVUE.md)
