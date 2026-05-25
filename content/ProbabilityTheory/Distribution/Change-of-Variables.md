---
title: "Change of Variables for Probability Distributions"
aliases:
  - "Probability Distribution Change of Variables"
  - "变量替换"
  - "概率分布变量替换"
  - "Jacobian变换"
  - "ProbabilityTheory/Distribution.Change-of-Variables"
course: "Probability Theory"
type: "topic-note"
status: "draft"
tags:
  - course/probability-theory
  - topic/distribution-theory
  - topic/change-of-variables
---

## 1. Change of Variable Theorem

**Setup.** Assume we have input $z$ with distribution $\pi(z)$, a function $f: \mathbb{R}^n \rightarrow \mathbb{R}^n$, output $x=f(z)$, and $x$ has distribution $p(x)$.

**Example (Linear transformation of a uniform variable).**

$$
z \sim U(0, 1), \quad x = f(z) = 2z+1 \Rightarrow x \sim U(1, 3).
$$

Given that

$$
\int p(x) dx = 1, \quad \int \pi(z) dz = 1,
$$

we have

$$
p(x) = \frac12 \pi(z).
$$

## 2. General Derivation

- Given point $z'$ from distribution $\pi(z')$, point $x'$ from distribution $p(x')$, and known transformation $f$.
- Take a small volume $\Delta z$ around $z'$ to get $(z', z'+\Delta z)$, and accordingly $(x', x'+\Delta x)$.
- Since $\Delta z$ and $\Delta x$ are small, we can assume $(z', z'+\Delta z)$ is uniformly distributed, and so is $(x', x'+\Delta x)$.
- Moreover, since $x$ is transformed from $z$, the probability mass of the small volume should be preserved:

$$
p(x')\Delta x = \pi(z')\Delta z.
$$

Thus,

$$
\boxed{p(x') = \pi(z') \frac{\Delta z}{\Delta x} = \pi(z') \left|\frac{\partial z}{\partial x}\right|}.
$$

As long as $f$ is given, $\frac{\partial z}{\partial x}$ is fixed, so we can get $p(x)$ from $\pi(z)$.

## 3. Multidimensional Formula

**Theorem (Change of variables formula).**

$$
\boxed{p(x) = \pi(z) \left|\det\left(\frac{\partial z}{\partial x}\right)\right| = \pi(z) \left|\det\left(J_{f^{-1}}\right)\right|}.
$$

### 3.1 More Mathematical Form

Assume that we have a mapping rule $z=f_\theta(x)$ over random variables $x$ and $z$. It can be proved that

$$
p_\theta(x) \mathrm{d}x = p(z) \mathrm{d}z.
$$

> [!note] Note: Intuition
> Personally I would say that although the random variable has been transformed from one to another, in a grand view of an event happening, the shift in space would not affect the probabilities. Thus this equation holds. Li Hongyi's explanation is that if we scale down to a very small area $\mathrm{d}x$ and $\mathrm{d}z$, then both approximately follow a uniform distribution, with the same total probability mass.

Thus we get the change of variables formula:

$$
p_\theta(x) = p(f_\theta(x)) \left| \frac{\partial f_\theta(x)}{\partial x} \right|,
$$

where $f_\theta$ is required to be invertible and differentiable.

## Related Notes

- [Box-Muller Transformation](../../ComputationalStatistics/Box-Muller-Transformation.md)
- [Generating Continuous Random Variables](../../ComputationalStatistics/Generating-Continuous-Random-Variables.md)
