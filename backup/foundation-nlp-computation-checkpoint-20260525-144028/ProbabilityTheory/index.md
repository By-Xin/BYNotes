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

Probability theory notes covering convergence, limit theorems, distribution transformations, exponential families, and random variable generation.

## Start Here

For statistical learning algorithms, start with limit theorems and convergence, then distribution tools, then simulation methods.

1. [Limit Theorems and Convergence](./Limit/)
2. [Distribution Theory](./Distribution/)
3. [Random Variable Generation](./Simulation/)

## Module Map

| Module                                      | Scope                                                   | Why it matters for statistical learning                                    |
| ------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| [Limit Theorems and Convergence](./Limit/)  | Convergence modes, inequalities, and CLT                | Asymptotic approximation, estimator behavior, and generalization arguments |
| [Distribution Theory](./Distribution/)      | Change of variables and exponential families            | Likelihood models, GLMs, and probabilistic classifiers                     |
| [Random Variable Generation](./Simulation/) | Inverse transform, recursive CDF, and normal simulation | Data simulation, Monte Carlo checks, and probabilistic intuition           |

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

### [Random Variable Generation](./Simulation/)

| Area                  | Note                                                                                                       | Status |
| --------------------- | ---------------------------------------------------------------------------------------------------------- | ------ |
| Discrete simulation   | [Generating Discrete Random Variables](./Simulation/Generating-Discrete-Random-Variables.md)               | draft  |
| Continuous simulation | [Generating Continuous Random Variables](./Simulation/Generating-Continuous-Random-Variables.md)           | draft  |
| Inverse transform     | [Generating Exponential Random Variables from Uniforms](./Simulation/Generate-Exponential-from-Uniform.md) | draft  |
| Inverse transform     | [Generating Geometric Random Variables from Uniforms](./Simulation/Generate-Geometric-from-Uniform.md)     | draft  |
| Recursive CDF         | [Generating Poisson Random Variables from Uniforms](./Simulation/Generate-Poisson-from-Uniform.md)         | draft  |
| Recursive CDF         | [Generating Binomial Random Variables from Uniforms](./Simulation/Generate-Binomial-from-Uniform.md)       | draft  |
| Normal simulation     | [Box-Muller Transformation](./Simulation/Box-Muller-Transformation.md)                                     | draft  |

## Concept Map

- Convergence: pointwise, uniform, mean-square, almost sure, in probability, and in distribution.
- Limit theorems: Chebyshev inequality, laws of large numbers, and central limit theorems.
- Distribution transformations: change of variables, Jacobian correction, and exponential-family representation.
- Simulation: inverse transform, recursive CDF methods, rejection sampling, and Box-Muller normal generation.

## Related Topics

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
