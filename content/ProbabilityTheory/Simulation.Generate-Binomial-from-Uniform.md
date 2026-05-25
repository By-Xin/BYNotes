---
title: "Generating Binomial Random Variables from Uniforms"
aliases:
  - "从 U(0,1) 生成二项分布随机变量"
  - "Generating Binomial Random Variable"
  - "二项分布随机数生成"
course: "Probability Theory"
type: "method-note"
status: "draft"
tags:
  - course/probability-theory
  - topic/random-variable-generation
  - topic/discrete-simulation
---

## 1. Model Overview

- 与泊松分布的生成方法类似.
- 注意的是当 $np$ 或泊松分布中的 $\lambda$ 较大时, 算法有较大的改进空间. 但讲义中并未提及, 故略去.

## 2. Simulation Goal

Generate a binomial $(n,p)$ random variable $X$:

$$
P\{X=i\}=\frac{n !}{i !(n-i) !} p^i(1-p)^{n-i}, \quad i=0,1,\ldots,n.
$$

## 3. Simulation Method

同样采用递归形式:

$$
P\{X=i+1\}=\frac{n-i}{i+1} \frac{p}{1-p} P\{X=i\}.
$$

> [!note] Note: Constant factor
> 在算法实现时, 注意到 $p/(1-p)$ 为常数, 与 $i$ 无关, 故可以另记之方便计算.

Algorithm:

1. Generate a random number $U$.
2. Set $c=p /(1-p)$, $i=0$, $\mathrm{pr} =(1-p)^n$, $F= \mathrm{pr}$.
3. If $U<F$, set $X=i$ and stop.
4. Set $\mathrm{pr}=[c(n-i) /(i+1)] \mathrm{pr}$, $F=F+\mathrm{pr}$, $i=i+1$.
5. Go to Step 3.

## 4. Remarks

- 这里 $c$ 即为上述的常数项, $\mathrm{pr}$ 为递归形式的 $P\{X=i\}$, $F$ 为累积的分布函数.
- 要注意到循环的次数总是比确定的 $X$ 值大一. 显然, 即使 $X=0$, 也要经过一次循环比较才能确定.
- 根据二项分布的性质, 当 $p>1/2$ 时可以通过上述算法生成 $Y\sim b(n,1-p)$, $X=n-Y$ 即为所求.
- 另一种实现方法为模拟 $n$ 次实验的结果.

## 5. Code

```matlab
% set up storage space for the variables
X = zeros(1, 100);

% These are the x's in the domain
x = 0:2;

% These are the probability masses.
pr = [0.3 0.2 0.5];

% Generate 100 rv's from the desired distribution.
for i = 1:100
  u = rand;
  if u <= pr(1)
    X(i) = x(1);
  elseif u <= sum(pr(1:2))
    X(i) = x(2);
  else
    X(i) = x(3);
  end
end
```

## Related Notes

- [Generating Discrete Random Variables](./Simulation.Generating-Discrete-Random-Variables.md)
- [Generating Poisson Random Variables from Uniforms](./Simulation.Generate-Poisson-from-Uniform.md)
- [Central Limit Theorem](./Limit.Central-Limit-Theorem.md)
