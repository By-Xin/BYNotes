---
title: "Probability Theory"
aliases:
  - "Probability"
  - "math.PR Probability"
  - "math.PR_Probability"
  - "概率论"
type: "course-index"
status: "active"
tags:
  - course/probability-theory
---

Probability theory notes covering convergence, limit theorems, distribution transformations, and exponential families.

## Start Here

For statistical learning algorithms, start with limit theorems and convergence, then distribution tools, then use computational statistics for simulation and sanity checks.

1. [Limit Theorems and Convergence](./Limit/)
2. [Distribution Theory](./Distribution/)
3. [Computational Statistics](../ComputationalStatistics/)

## Module Map

| Module                                     | Scope                                        | Why it matters for statistical learning                                    |
| ------------------------------------------ | -------------------------------------------- | -------------------------------------------------------------------------- |
| [Limit Theorems and Convergence](./Limit/) | Convergence modes, inequalities, and CLT     | Asymptotic approximation, estimator behavior, and generalization arguments |
| [Distribution Theory](./Distribution/)     | Change of variables and exponential families | Likelihood models, GLMs, and probabilistic classifiers                     |

## Notes

### [Limit Theorems and Convergence](./Limit/)

| Area          | Note                                                                          | Status |
| ------------- | ----------------------------------------------------------------------------- | ------ |
| Inequality    | [Chebyshev Inequality](./Limit/Chebyshev-Inequality.md)                       | draft  |
| Convergence   | [Convergence of Random Variables](./Limit/Convergence-of-Random-Variables.md) | draft  |
| Limit theorem | [Central Limit Theorem](./Limit/Central-Limit-Theorem.md)                     | draft  |

### [Distribution Theory](./Distribution/)

| Area               | Note                                                                                       | Status |
| ------------------ | ------------------------------------------------------------------------------------------ | ------ |
| Exponential family | [Exponential Family](./Distribution/Exponential-Family.md)                                 | draft  |
| Transformation     | [Change of Variables for Probability Distributions](./Distribution/Change-of-Variables.md) | draft  |

## Adjacent Foundations

- [Computational Statistics](../ComputationalStatistics/) covers random variable generation, simulation methods, and Monte Carlo checks.

## Concept Map

- Convergence: pointwise, uniform, mean-square, almost sure, in probability, and in distribution.
- Limit theorems: Chebyshev inequality, laws of large numbers, and central limit theorems.
- Distribution transformations: change of variables, Jacobian correction, and exponential-family representation.

## Related Topics

- [Computational Statistics](../ComputationalStatistics)
- [Statistical Inference](../StatisticalInference)
- [Statistical Learning Algorithms](../StatisticalLearningAlgorithms)
- [Stochastic Process](../StochasticProcess)

## Planned Notes

- Law of Large Numbers
- Markov Inequality
- Normal Distribution
- Poisson Distribution
- Binomial Distribution
- Geometric Distribution
