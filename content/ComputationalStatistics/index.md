---
title: "Computational Statistics"
aliases:
  - "Random Variable Generation"
  - "ProbabilityTheory/Simulation"
  - "ProbabilityTheory/Simulation/index"
type: "course-index"
status: "active"
tags:
  - course/computational-statistics
  - topic/random-variable-generation
---

Computational statistics notes for simulation, random variable generation, Monte Carlo sanity checks, and probability-driven numerical methods.

## Start Here

For statistical learning algorithms, use this section after the basic probability distribution tools.

1. [Generating Discrete Random Variables](./Generating-Discrete-Random-Variables.md)
2. [Generating Continuous Random Variables](./Generating-Continuous-Random-Variables.md)
3. [Box-Muller Transformation](./Box-Muller-Transformation.md)

## Module Map

| Theme                   | Scope                                              | Why it matters for statistical learning                       |
| ----------------------- | -------------------------------------------------- | ------------------------------------------------------------- |
| Discrete simulation     | Inverse transform and recursive CDF methods        | Synthetic categorical/count data and sanity checks            |
| Continuous simulation   | Inverse transform and distribution transformations | Sampling continuous assumptions and transformed variables     |
| Normal random variables | Box-Muller and normal simulation                   | Gaussian model checks, residual simulation, and CLT intuition |

## Notes

| Area                  | Note                                                                                            | Status |
| --------------------- | ----------------------------------------------------------------------------------------------- | ------ |
| Discrete simulation   | [Generating Discrete Random Variables](./Generating-Discrete-Random-Variables.md)               | draft  |
| Continuous simulation | [Generating Continuous Random Variables](./Generating-Continuous-Random-Variables.md)           | draft  |
| Inverse transform     | [Generating Exponential Random Variables from Uniforms](./Generate-Exponential-from-Uniform.md) | draft  |
| Inverse transform     | [Generating Geometric Random Variables from Uniforms](./Generate-Geometric-from-Uniform.md)     | draft  |
| Recursive CDF         | [Generating Poisson Random Variables from Uniforms](./Generate-Poisson-from-Uniform.md)         | draft  |
| Recursive CDF         | [Generating Binomial Random Variables from Uniforms](./Generate-Binomial-from-Uniform.md)       | draft  |
| Normal simulation     | [Box-Muller Transformation](./Box-Muller-Transformation.md)                                     | draft  |

## Statistical Learning Use

- Generate synthetic data for sanity checks.
- Build Monte Carlo intuition for estimators and model assumptions.
- Connect sampling methods to uncertainty and probabilistic modeling.

## Related Modules

- [Distribution Theory](../ProbabilityTheory/Distribution/)
- [Limit Theorems and Convergence](../ProbabilityTheory/Limit/)
- [Statistical Learning Algorithms](../StatisticalLearningAlgorithms/)
