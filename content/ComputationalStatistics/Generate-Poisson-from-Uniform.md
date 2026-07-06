---
title: "Generating Poisson Random Variables from Uniforms"
aliases:
  - "从 U(0,1) 生成泊松分布随机变量"
  - "Generating Poisson Random Variable"
  - "泊松分布随机数生成"
  - "ProbabilityTheory/Simulation.Generate-Poisson-from-Uniform"
  - "ProbabilityTheory/Simulation/Generate-Poisson-from-Uniform"
course: "Computational Statistics"
type: "method-note"
status: "draft"
tags:
  - course/computational-statistics
  - topic/random-variable-generation
  - topic/discrete-simulation
---

## 1. Model Overview

- 该算法的思路与逆变换法一致: 通过生成 $U$ 模拟泊松分布的分布函数, 再寻找其对应的自变量值 $X$. 不同之处在于泊松分布的函数正常计算较为复杂, 故采取递推方式计算.
- 递推的思路: 首先仍生成一均匀分布 $U$ 代表泊松分布函数, 然后开始循环讨论. 从 $F(i)=P\{X=i\},i=0$ 开始, 看 $F(i)$ 的值是否大于生成的 $U$ 的值. 若是则该 $i$ 即为想要模拟的 $x$, 若不是则 $i++$, 继续讨论.
- 简而言之, 对于递推形式, 算法的核心在于依次比较 $F(0),F(1),F(2),\cdots$ 与 $U$ 的大小, 第一个使得 $F(i)>U$ 的 $i$ 即为所求的 $x$.

## 2. Simulation Goal

Generate a random variable $X$ following a Poisson distribution with parameter $\lambda$:

$$
p_i=P\{X=i\}=e^{-\lambda} \frac{\lambda^i}{i! } \quad i=0,1,\ldots.
$$

## 3. Simulation Method

Since the Poisson CDF involves factorials and is costly to calculate directly, use a recurrence:

$$
\begin{gathered}
\frac{p_{i+1}}{p_i}=\frac{\frac{e^{-\lambda} \lambda^{i+1}}{(i+1) !}}{\frac{e^{-\lambda} \lambda^i}{i !}}=\frac{\lambda}{i+1}, \\
\boxed{p_{i+1}=\frac{\lambda}{i+1} p_i, \quad i \geqslant 0}.
\end{gathered}
$$

Algorithm:

1. Generate a random number $U$.
2. Set $i=0$, $p=e^{-\lambda}$, $F=p$.
3. If $U<F$, set $X=i$ and stop.
4. Set $p=\lambda p /(i+1)$, $F=F+p$, $i=i+1$.
5. Go to Step 3.

## 4. Code

```matlab
% function X = cspoirnd(lam,n)
% This function will generate Poisson(lambda)

function x = cspoirnd(lam, n)
x = zeros(1, n);
j = 1;
while j <= n
  flag = 1;

  % initialize quantities
  u = rand(1);
  i = 0;
  p = exp(-lam);
  F = p;

  while flag
    if u <= F
      x(j) = i;
      flag = 0;
      j = j + 1;
    else
      p = lam * p / (i + 1);
      i = i + 1;
      F = F + p;
    end
  end
end
```

## Related Notes

- [Generating Discrete Random Variables](./Generating-Discrete-Random-Variables.md)
- [Generating Binomial Random Variables from Uniforms](./Generate-Binomial-from-Uniform.md)
