---
title: "Generating Discrete Random Variables"
aliases:
  - "离散随机变量的生成"
  - "离散随机变量生成"
  - "Generating Discrete Random Variables"
  - "逆变换法"
  - "ProbabilityTheory/Simulation.Generating-Discrete-Random-Variables"
course: "Probability Theory"
type: "method-note"
status: "draft"
tags:
  - course/probability-theory
  - topic/random-variable-generation
  - topic/discrete-simulation
---

## 1. Inverse Transform Method

### 1.1 Model Overview

不论何种随机变量, 定有一个相对应的分布函数, 且由分布函数的性质可以确定其在 $(0,1)$ 区间是单调递增的, 故具有广义反函数. 模拟的思路即为通过生成均匀分布随机数 $U(0,1)$ 模拟其分布函数数值 $F$, 再通过寻找分布函数的反函数确定其随机变量 $X$ 的数值.

### 1.2 Simulation Goal

生成一系列离散型随机变量 $X$, 其概率密度函数服从:

$$
P\{X=x_j\}=p_j, \quad j=0,1,\cdots, \quad \sum_j p_j=1.
$$

### 1.3 Simulation Method

1. Generate a random number $U \sim U(0,1)$.
2. Let:

$$
\begin{aligned}
X=
\begin{cases}
x_0 & \text{if } U<p_0, \\
x_1 & \text{if } p_0 \leq U<p_0+p_1, \\
\vdots & \\
x_j & \text{if } \sum_{i=0}^{j-1} p_i \leq U<\sum_{i=0}^j p_i, \\
\vdots &
\end{cases}
\end{aligned}
$$

3. For $0<a<b<1$, $P\{a\le U <b\}=b-a$, so:

$$
\begin{aligned}
P\left\{X=x_j\right\}
&=P\left\{\sum_{i=0}^{j-1} p_i \leq U<\sum_{i=0}^j p_i\right\} \\
&=p_j.
\end{aligned}
$$

此时的 $X$ 即为所求.

### 1.4 Notes

Algorithm expression:

1. Generate a random number $U$.
2. If $U<p_0$, set $X=x_0$ and stop.
3. If $U<p_0+p_1$, set $X=x_1$ and stop.
4. If $U<p_0+p_1+p_2$, set $X=x_2$ and stop.

若 $x_i$ 是顺序排列的, 即 $x_0<x_1<\cdots$, 且记 $F(x_k)=\sum_{i=0}^kp_i$, 则:

$$
X=x_j, \quad \mathrm{if} \quad F(x_{j-1}) \leq U<F(x_j).
$$

换言之, 该过程即为寻找 $F^{-1}(U)$ 对应的 $X$.

### 1.5 Example: Generate a Given Discrete Distribution

要求: 生成随机变量 $X$ 满足:

$$
\begin{aligned}
p_1=0.20, \quad p_2=0.15, \quad p_3=0.25, \quad p_4=0.40, \quad \text{where } p_j=P\{X=j\}.
\end{aligned}
$$

**Solution 1.**

1. Generate $U$.
2. If $U<0.20$, set $X=1$ and stop.
3. If $U<0.35$, set $X=2$ and stop.
4. If $U<0.60$, set $X=3$ and stop.
5. Otherwise set $X=4$.

**Solution 2.**

1. Generate $U$.
2. If $U<0.40$, set $X=4$ and stop.
3. If $U<0.65$, set $X=3$ and stop.
4. If $U<0.85$, set $X=1$ and stop.
5. Otherwise set $X=2$.

### 1.6 Example: Generate a Geometric Random Variable

See [Generating Geometric Random Variables from Uniforms](./Generate-Geometric-from-Uniform.md).

要求: 生成随机变量 $X$ 满足参数为 $p$ 的几何分布:

$$
\begin{aligned}
P\{X=i\}=p q^{i-1}, \quad i \geq 1, \quad \text{where } q=1-p.
\end{aligned}
$$

由几何分布的含义, $X$ 可认为是 $n$ 次独立实验中首次成功的时间, 且每次实验的成功概率为 $p$, 故有:

$$
\begin{aligned}
\sum_{i=1}^{j-1} P\{X=i\}
&=1-P\{X>j-1\} \\
&=1-P\{\text{first } j-1 \text{ trials are all failures}\} \\
&=1-q^{j-1}, \quad j \geq 1.
\end{aligned}
$$

故可以生成随机数 $U$ 并令:

$$
1-q^{j-1} \leq U<1-q^j \Rightarrow q^j<1-U \leq q^{j-1}.
$$

Therefore,

$$
X=\operatorname{Min}\left\{j: q^j<1-U\right\}. \quad(\star)
$$

下需解出 $j$ 的具体数值. 由对数函数的单调性, 对 $(\star)$ 式集合中不等式两侧求对数:

$$
\begin{aligned}
X
&=\operatorname{Min}\{j: j \log (q)<\log (1-U)\} \\
&=\operatorname{Min}\left\{j: j>\frac{\log (1-U)}{\log (q)}\right\}.
\end{aligned}
$$

若用记号 $\operatorname{Int}(x)$ 表示不大于 $x$ 的最大整数, 则有:

$$
X=\operatorname{Int}\left(\frac{\log (1-U)}{\log (q)}\right)+1.
$$

其等价于:

$$
\boxed{X \equiv \operatorname{Int}\left(\frac{\log (U)}{\log (q)}\right)+1}.
$$

## 2. Generate a Poisson Random Variable

See [Generating Poisson Random Variables from Uniforms](./Generate-Poisson-from-Uniform.md).

### 2.1 Model Overview

- 该算法的思路与 4.1 一致: 通过生成 $U$ 模拟泊松分布的分布函数, 再寻找其对应的自变量值 $X$. 不同之处在于泊松分布的函数正常计算较为复杂, 故采取递推方式计算.
- 递推的思路: 首先仍生成一均匀分布 $U$ 代表泊松分布函数, 然后开始循环讨论. 从 $F(i)=P\{X=i\},i=0$ 开始, 看 $F(i)$ 的值是否大于生成的 $U$ 的值. 若是则该 $i$ 即为想要模拟的 $x$, 若不是则 $i++$, 继续讨论.
- 简而言之, 对于递推形式, 算法的核心在于依次比较 $F(0),F(1),F(2),\cdots$ 与 $U$ 的大小, 第一个使得 $F(i)>U$ 的 $i$ 即为所求的 $x$.

### 2.2 Simulation Goal

Generate a random variable $X$ following a Poisson distribution with parameter $\lambda$:

$$
p_i=P\{X=i\}=e^{-\lambda} \frac{\lambda^i}{i! } \quad i=0,1,\ldots.
$$

### 2.3 Simulation Method

采用递推的方式进行计算:

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

### 2.4 Code

```matlab
function x = cspoirnd(lam, n)
x = zeros(1, n);
j = 1;
while j < n
  flag = 1;
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

## 3. Generate a Binomial Random Variable

See [Generating Binomial Random Variables from Uniforms](./Generate-Binomial-from-Uniform.md).

### 3.1 Model Overview

- 与泊松分布的生成方法类似.
- 注意的是当 $np$ 或泊松分布中的 $\lambda$ 较大时, 算法有较大的改进空间. 但讲义中并未提及, 故略去.

### 3.2 Simulation Goal

Generate a binomial $(n,p)$ random variable $X$:

$$
P\{X=i\}=\frac{n !}{i !(n-i) !} p^i(1-p)^{n-i}, \quad i=0,1,\ldots,n.
$$

### 3.3 Simulation Method

采用递归形式:

$$
P\{X=i+1\}=\frac{n-i}{i+1} \frac{p}{1-p} P\{X=i\}.
$$

Algorithm:

1. Generate a random number $U$.
2. Set $c=p /(1-p)$, $i=0$, $\mathrm{pr} =(1-p)^n$, $F= \mathrm{pr}$.
3. If $U<F$, set $X=i$ and stop.
4. Set $\mathrm{pr}=[c(n-i) /(i+1)] \mathrm{pr}$, $F=F+\mathrm{pr}$, $i=i+1$.
5. Go to Step 3.

### 3.4 Remarks

- 这里 $c$ 即为上述的常数项, $\mathrm{pr}$ 为递归形式的 $P\{X=i\}$, $F$ 为累积的分布函数.
- 要注意到循环的次数总是比确定的 $X$ 值大一. 显然, 即使 $X=0$, 也要经过一次循环比较才能确定.
- 根据二项分布的性质, 当 $p>1/2$ 时可以通过上述算法生成 $Y\sim b(n,1-p)$, $X=n-Y$ 即为所求.
- 另一种实现方法为模拟 $n$ 次实验的结果.

### 3.5 Code

```matlab
X = zeros(1, 100);
x = 0:2;
pr = [0.3 0.2 0.5];

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

- [Generating Continuous Random Variables](./Generating-Continuous-Random-Variables.md)
- [Generating Geometric Random Variables from Uniforms](./Generate-Geometric-from-Uniform.md)
- [Generating Poisson Random Variables from Uniforms](./Generate-Poisson-from-Uniform.md)
- [Generating Binomial Random Variables from Uniforms](./Generate-Binomial-from-Uniform.md)
