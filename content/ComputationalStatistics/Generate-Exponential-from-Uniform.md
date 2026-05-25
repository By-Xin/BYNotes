---
title: "Generating Exponential Random Variables from Uniforms"
aliases:
  - "从 U(0,1) 生成指数分布随机变量"
  - "Generating Exponential Random Variable"
  - "指数分布随机数生成"
  - "ProbabilityTheory/Simulation.Generate-Exponential-from-Uniform"
  - "ProbabilityTheory/Simulation/Generate-Exponential-from-Uniform"
course: "Computational Statistics"
type: "method-note"
status: "draft"
tags:
  - course/computational-statistics
  - topic/random-variable-generation
  - topic/inverse-transform
---

## 1. Goal

Generate a random variable $X\sim\mathrm{exp}(\lambda)$ with CDF:

$$
F(x)=1-e^{-\lambda x}.
$$

## 2. Inverse Transform

Let

$$
u=F(x)=1-e^{-\lambda x}.
$$

Solving for $x$ gives:

$$
x=-\frac1\lambda \log (1-u).
$$

Equivalently:

$$
\boxed {X=-\frac1\lambda \log (u)}.
$$

## 3. Code

```matlab
% set up the parameters.
lam = 2;

% generate the rv's
uni = rand(1, n);
X = -log(uni) / lam;
```

## Related Notes

- [Generating Continuous Random Variables](./Generating-Continuous-Random-Variables.md)
- [Change of Variables for Probability Distributions](../ProbabilityTheory/Distribution/Change-of-Variables.md)
