---
title: "Generating Geometric Random Variables from Uniforms"
aliases:
  - "从 U(0,1) 生成几何分布随机变量"
  - "Generating Geometric Random Variable"
  - "几何分布随机数生成"
  - "ProbabilityTheory/Simulation.Generate-Geometric-from-Uniform"
  - "ProbabilityTheory/Simulation/Generate-Geometric-from-Uniform"
course: "Computational Statistics"
type: "method-note"
status: "draft"
tags:
  - course/computational-statistics
  - topic/random-variable-generation
  - topic/inverse-transform
---

## 1. Goal

Generate a random variable $X$ satisfying the geometric distribution with parameter $p$:

$$
\begin{aligned}
P\{X=i\}=p q^{i-1}, \quad i \geq 1, \quad \text{where } q=1-p.
\end{aligned}
$$

## 2. Derivation

由几何分布的含义, $X$ 可认为是 $n$ 次独立实验中首次成功的时间, 且每次实验的成功概率为 $p$, 故有:

$$
\begin{aligned}
\sum_{i=1}^{j-1} P\{X=i\}
&=1-P\{X>j-1\} \\
&=1-P\{\text{first } j-1 \text{ trials are all failures}\} \\
&=1-q^{j-1}, \quad j \geq 1.
\end{aligned}
$$

Thus generate a random number $U$ and let:

$$
1-q^{j-1} \leq U<1-q^j \Rightarrow q^j<1-U \leq q^{j-1}.
$$

Therefore:

$$
X=\operatorname{Min}\left\{j: q^j<1-U\right\}. \quad(\star)
$$

Taking log on both sides:

$$
\begin{aligned}
X
&=\operatorname{Min}\{j: j \log (q)<\log (1-U)\} \\
&=\operatorname{Min}\left\{j: j>\frac{\log (1-U)}{\log (q)}\right\}.
\end{aligned}
$$

If $\operatorname{Int}(x)$ means the largest integer not greater than $x$, then:

$$
X=\operatorname{Int}\left(\frac{\log (1-U)}{\log (q)}\right)+1.
$$

Equivalently:

$$
\boxed{X \equiv \operatorname{Int}\left(\frac{\log (U)}{\log (q)}\right)+1}.
$$

## Related Notes

- [Generating Discrete Random Variables](./Generating-Discrete-Random-Variables.md)
- [Generating Exponential Random Variables from Uniforms](./Generate-Exponential-from-Uniform.md)
