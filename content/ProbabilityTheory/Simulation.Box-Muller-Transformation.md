---
title: "Box-Muller Transformation"
aliases:
  - "Box-Muller 变换"
  - "Box-Muller变换"
  - "极坐标法"
  - "Polar Method"
  - "正态随机数生成"
course: "Probability Theory"
type: "method-note"
status: "draft"
tags:
  - course/probability-theory
  - topic/random-variable-generation
  - topic/normal-simulation
---

## 1. Background

### 1.1 Polar Coordinates

$$
R^2=X^2+Y^2.
$$

$$
\tan\Theta = \frac Y X.
$$

### 1.2 Normal Distribution

由于 $X,Y$ 独立, 其联合概率密度函数为:

$$
\begin{aligned}
f(x, y)
&=\frac{1}{\sqrt{2 \pi}} e^{-x^2 / 2} \frac{1}{\sqrt{2 \pi}} e^{-y^2 / 2} \\
&=\frac{1}{2 \pi} e^{-\left(x^2+y^2\right) / 2}.
\end{aligned}
$$

### 1.3 Function Transformation

$$
P(X\in C, Y\in D)=\iint_{X\in C, Y\in D}f(x,y)dxdy
$$

$$
=\iint_{u\in C^\prime, v\in D^\prime} f(g_1(u,v),g_2(u,v))|J|dudv.
$$

## 2. Box-Muller Transformation

将 $X,Y$ 的联合密度函数转化到极坐标系中. 令 $d=x^2+y^2$ and $\theta=\arctan(y/x)$, then:

$$
f(d, \theta)=\frac{1}{2} \frac{1}{2 \pi} e^{-d / 2}, \quad 0<d<\infty, 0<\theta<2 \pi.
$$

注意到, 上述密度函数可以认为是均值为 $2$ 的指数分布 $\frac12e^{-d/2}$ 与 $(0,2\pi)$ 的均匀分布 $\frac1{2\pi}$ 的密度函数乘积. Thus:

- $R^2$ 与 $\Theta$ 彼此独立.
- $R^2$ 服从均值为 $2$ 的指数分布.
- $\Theta$ 服从 $(0,2\pi)$ 的均匀分布.

Algorithm:

1. Generate random numbers $U_1, U_2$.
2. Let

$$
R^2=-2\log U_1, \quad \Theta=2\pi U_2.
$$

3. Let

$$
\begin{aligned}
X&=R \cos \Theta=\sqrt{-2 \log U_1} \cos \left(2 \pi U_2\right), \\
Y&=R \sin \Theta=\sqrt{-2 \log U_1} \sin \left(2 \pi U_2\right).
\end{aligned}
\quad(\star)
$$

> [!note] Note: Efficiency issue
> Box-Muller 变换在计算时的效率较低, 这是因为 Step 3 涉及三角函数 $\cos,\sin$ 的计算. 为了改进这一特点, 下文不再生成随机角度 $\Theta$, 而是直接通过模拟直角三角形的三边长度生成随机三角函数 $\cos\Theta,\sin\Theta$.

## 3. Polar Method

### 3.1 Improvement Idea

不再计算模拟的随机角度的三角函数, 而是通过模拟单位圆直接计算三角函数的具体数值.

### 3.2 Steps

引入单位圆. 若 $U\sim(0,1)$, 则 $2U-1\sim(-1,1)$, 故令:

$$
\begin{aligned}
V_1&=2 U_1-1, \\
V_2&=2 U_2-1.
\end{aligned}
$$

不断生成随机数对 $(V_1,V_2)$ 并保留满足 $V_1^2+V_2^2\leq 1$ 的部分, 则有 $(V_1,V_2)$ 在单位圆上均匀分布.

对于该随机数对 $(V_1,V_2)$ 对应的极坐标方程, 可知其对应的 $R^2$ 服从 $(0,1)$ 的均匀分布, 而 $\Theta$ 服从 $(0,2\pi)$ 的均匀分布.

模拟 $\sin$ and $\cos$:

$$
\begin{aligned}
\sin \Theta&=\frac{V_2}{R}=\frac{V_2}{\left(V_1^2+V_2^2\right)^{1 / 2}}, \\
\cos \Theta&=\frac{V_1}{R}=\frac{V_1}{\left(V_1^2+V_2^2\right)^{1 / 2}}.
\end{aligned}
$$

对 Box-Muller 的改进: 将上述模拟的 $\sin\Theta,\cos\Theta$ 代入 $(\star)$:

$$
\begin{aligned}
X&=(-2 \log U)^{1 / 2} \frac{V_1}{\left(V_1^2+V_2^2\right)^{1 / 2}}, \\
Y&=(-2 \log U)^{1 / 2} \frac{V_2}{\left(V_1^2+V_2^2\right)^{1 / 2}}.
\end{aligned}
$$

再令 $S=R^2$, 则有:

$$
\begin{aligned}
X&=(-2 \log S)^{1 / 2} \frac{V_1}{S^{1 / 2}}=V_1\left(\frac{-2 \log S}{S}\right)^{1 / 2}, \\
Y&=(-2 \log S)^{1 / 2} \frac{V_2}{S^{1 / 2}}=V_2\left(\frac{-2 \log S}{S}\right)^{1 / 2}.
\end{aligned}
$$

综上, 新的模拟步骤为:

1. Generate random numbers $U_1,U_2$.
2. Let $V_1=2U_1-1$, $V_2=2U_2-1$, and $S=V_1^2+V_2^2$.
3. If $S>1$, return to Step 1.
4. Otherwise generate a pair of standard normal random variables:

$$
X=\sqrt{\frac{-2 \log S}{S}} V_1, \quad Y=\sqrt{\frac{-2 \log S}{S}} V_2.
$$

## Related Notes

- [Change of Variables for Probability Distributions](./Distribution.Change-of-Variables.md)
- [Generating Continuous Random Variables](./Simulation.Generating-Continuous-Random-Variables.md)
- [Generating Exponential Random Variables from Uniforms](./Simulation.Generate-Exponential-from-Uniform.md)
