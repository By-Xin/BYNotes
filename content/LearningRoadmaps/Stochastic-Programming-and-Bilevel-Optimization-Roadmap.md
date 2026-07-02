---
title: "Stochastic Programming and Bilevel Optimization Roadmap"
aliases:
  - "Study Roadmap: Stochastic Programming and Bilevel Optimization"
  - "CSBO and MLMC Roadmap"
  - "Stochastic Programming / Bilevel / MLMC Syllabus"
type: "roadmap-note"
status: "draft"
tags:
  - roadmap
  - topic/stochastic-programming
  - topic/bilevel-optimization
  - topic/mlmc
---
这份 roadmap 将若干学习材料组织成一个偏 graduate / PhD 入门到进阶的 syllabus，而不是单纯堆资源。

目标是围绕两个相互连接的方向建立背景：

1. **Stochastic Programming / Multistage Stochastic Programming / MLMC**
2. **Bilevel Optimization / Stochastic Bilevel / Hypergradient**

这两个方向的交汇点是：conditional stochastic optimization 可以和 stochastic bilevel 联系起来，contextual stochastic bilevel 又进一步连接到 three-stage / multistage stochastic programming。

---

# 总体结构

这份学习大纲分成 8 个模块：

1. 基础优化与随机优化
2. Stochastic Programming 入门
3. Multistage Stochastic Programming 与 SDDP
4. MLMC / randomized telescoping
5. Classical Bilevel Optimization
6. Gradient-based Bilevel / Hypergradient
7. Stochastic Bilevel / Conditional Stochastic Optimization
8. 交叉前沿：CSBO、MCCO 与 MLMC-based stochastic methods

最重要的逻辑是：stochastic programming、bilevel optimization 和 MLMC estimator 共同指向 conditional stochastic / bilevel / MLMC 的技术交界处。

---

# Module 0. 预备知识：凸优化、随机优化、oracle complexity

这一部分是后续内容的预备层。若缺少这部分背景，sample complexity、biased oracle、lower bound、MLMC gradient method 等内容会很难衔接。

## 0.1 John Duchi, Introductory Lectures on Stochastic Optimization

类型：讲义 / 公开 lecture notes
优先级：高
用途：补 stochastic convex optimization、SGD、mirror descent、sample complexity、probabilistic analysis。

URL: [https://web.stanford.edu/~jduchi/PCMIConvex/Duchi16.pdf](https://web.stanford.edu/~jduchi/PCMIConvex/Duchi16.pdf)

配套页面：
URL: [https://stanford.edu/~jduchi/PCMIConvex/](https://stanford.edu/~jduchi/PCMIConvex/)

Duchi 这套 PCMI 讲义专门讲 stochastic convex optimization 的分析工具和算法，适合作为后面 CSO、biased stochastic gradient、MLMC gradient 的基础。([Stanford University][1])

建议读法：

* Lecture 1：stochastic optimization 的基本模型
* Lecture 2：stochastic subgradient / mirror descent
* Lecture 3：sample complexity / high probability bound
* Technical lemmas 可以先后置

学习目标：能够解释：

$$
\min_x \mathbb E_\xi[f(x,\xi)]
$$

为什么通常会出现 $\epsilon^{-2}$ 这种 sampling scale。

---

## 0.2 Sébastien Bubeck, Convex Optimization: Algorithms and Complexity

类型：短书 / monograph
优先级：高
用途：理解 black-box oracle、first-order complexity、lower bound、stochastic gradient。

URL: [https://arxiv.org/abs/1405.4980](https://arxiv.org/abs/1405.4980)

PDF:
URL: [https://sbubeck.com/Bubeck15.pdf](https://sbubeck.com/Bubeck15.pdf)

这本书从 black-box optimization 开始，系统讲 gradient descent、accelerated methods、mirror descent、stochastic gradient 等内容。它特别适合理解一个重要观点：**lower bound 不是脱离 oracle model 独立存在的东西**。([arXiv][2])

建议读：

* Chapter 1：basic convexity and black-box model
* Gradient descent / accelerated gradient 部分
* Stochastic gradient 部分
* Lower bound 部分先读直觉，证明可后置

---

# Module 1. Stochastic Programming 入门

这一模块是第一条主线的基础，需要掌握 stochastic programming 的语言：recourse、SAA、scenario tree、nonanticipativity、value function。

---

## 1.1 Shapiro & Philpott, A Tutorial on Stochastic Programming

类型：tutorial
优先级：非常高
用途：先建立 stochastic programming 的整体直觉。

URL: [https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf](https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf)

这是短 tutorial，比教材友好。适合在正式读 Birge–Louveaux 或 Shapiro 那本书之前先过一遍。

建议读法：

* 一次性快速读完
* 证明可先略读
* 重点理解 two-stage stochastic programming 的建模语言

---

## 1.2 Birge & Louveaux, Introduction to Stochastic Programming

类型：教材
优先级：最高
用途：stochastic programming 入门主教材。

URL: [https://link.springer.com/book/10.1007/978-1-4614-0237-4](https://link.springer.com/book/10.1007/978-1-4614-0237-4)

Springer 页面明确说明这本书适合作为 stochastic programming 的 first course，背景要求是基本线性规划、初等分析和概率论。([Springer][3])

建议读：

* Chapter 1：Introduction
* Chapter 2：Basic properties and examples
* Chapter 3：Two-stage recourse problems
* Chapter 4：The deterministic equivalent problem
* Chapter 5 或相关章节：decomposition / L-shaped method
* SAA 相关章节
* Multistage 部分先读 formulation，不急着读算法细节

核心公式是：

$$
\min_{x\in X}
c^\top x+\mathbb E_\xi[Q(x,\xi)]
$$

其中

$$
\begin{aligned}
Q(x,\xi)
&= \min_y \left\{
q(\xi)^\top y:
W(\xi)y=h(\xi)-T(\xi)x,\ y\ge 0
\right\}.
\end{aligned}
$$

这就是 recourse value function。后面 bilevel 和 multistage 都会围绕这种“外层依赖内层优化对象”的结构展开。

---

## 1.3 Shapiro, Dentcheva, Ruszczyński, Lectures on Stochastic Programming: Modeling and Theory

类型：理论教材
优先级：高，但不建议一开始硬啃
用途：理论查阅主书。

SIAM 第三版页面：
URL: [https://epubs.siam.org/doi/book/10.1137/1.9781611976595](https://epubs.siam.org/doi/book/10.1137/1.9781611976595)

2009 版公开 PDF：
URL: [https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/4/1470/files/2021/03/SPbook.pdf](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/4/1470/files/2021/03/SPbook.pdf)

这本比 Birge–Louveaux 更理论，覆盖 stochastic programming 的 formulation、SAA、optimality、risk measure、multistage 等。SIAM 页面也说明它是对 contemporary stochastic programming models and ideas 的严谨介绍。([BPB][4])

建议读：

* Chapter 1：Stochastic programming models
* SAA 相关章节
* Multistage stochastic programs 相关章节
* SDDP 相关部分后面再读

这本可作为后续写笔记、查定义、查 theorem 的工具书。

---

# Module 2. SAA、scenario tree 与 multistage complexity

这个模块解释一个常见背景问题：为什么传统 multistage stochastic programming 会被认为有 curse of dimensionality / curse of stages。

---

## 2.1 Kim, Pasupathy, Henderson, A Guide to Sample Average Approximation

类型：survey / tutorial
优先级：高
用途：系统理解 SAA。

URL: [https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf](https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf)

这篇 review 的目标就是解释 SAA principle、什么时候用 SAA、为什么 SAA 有用以及理论性质。([People at Cornell][5])

建议读：

* SAA 的基本 principle
* consistency
* finite sample guarantee 的直觉
* 与 stochastic approximation 的区别

学习目标：能够解释：

$$
\mathbb E[f(x,\xi)]
\quad\longrightarrow\quad
\frac1N\sum_{i=1}^N f(x,\xi_i).
$$

---

## 2.2 Shapiro & Nemirovski, On Complexity of Stochastic Programming Problems

类型：复杂度论文
优先级：中高
用途：理解 two-stage 和 multistage 的复杂度差别。

URL: [https://optimization-online.org/wp-content/uploads/2004/10/978.pdf](https://optimization-online.org/wp-content/uploads/2004/10/978.pdf)

这篇文章讨论 stochastic programming 的计算复杂度，并指出 two-stage linear stochastic programs with recourse 通常可以用 Monte Carlo sampling 得到合理精度，而 general multistage stochastic programs 一般非常困难。([Optimization Online][6])

建议读：

* Introduction
* Two-stage complexity discussion
* Multistage complexity discussion
* proof 可后置

---

## 2.3 Shapiro, On Complexity of Multistage Stochastic Programs

类型：核心背景论文
优先级：高
用途：理解 conditional sampling SAA 为什么导致多阶段样本复杂度递推。

PDF:
URL: [https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf](https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf)

Journal 页面：
URL: [https://www.sciencedirect.com/science/article/abs/pii/S0167637705000325](https://www.sciencedirect.com/science/article/abs/pii/S0167637705000325)

这篇文章估计用 conditional sampling SAA 求解 multistage stochastic programming 时所需的 sample sizes。([Optimization Online][7])

建议读：

* Introduction
* Problem formulation
* Main theorem
* 证明部分先略读

读这篇时只抓一个问题：为什么每增加一层 conditional expectation，就好像多乘一个 sampling factor？

这也是后续 CSO / MLMC-based multistage work 试图重新分析的 common belief。

---

# Module 3. Multistage Stochastic Programming、DP、SDDP

这一模块用于理解传统 multistage stochastic programming 的算法路线：dynamic programming、nested Benders、SDDP。

---

## 3.1 Vincent Leclère, Stochastic and Dynamic Programming

类型：公开课程 / slides / practical work
优先级：非常高
用途：课程化学习 two-stage、dynamic programming、decomposition、SDDP。

课程页面：
URL: [https://leclere.github.io/teaching/OS](https://leclere.github.io/teaching/OS)

另一课程页面：
URL: [https://cermics.enpc.fr/~leclerev/OptimizationSaclay.html](https://cermics.enpc.fr/~leclerev/OptimizationSaclay.html)

这个课程页面包括 stochastic optimization introduction、two-stage problems、dynamic programming、decomposition methods、SDDP 等 slides 和实践材料。([leclere.github.io][8])

建议读：

* Introduction to stochastic optimization
* Two-stage problems
* Dynamic Programming
* Decomposition Methods
* SDDP

这是本路线中值得认真浏览的公开课之一。

---

## 3.2 MIT OCW 6.231, Dynamic Programming and Stochastic Control

类型：公开课
优先级：中高
用途：补 DP / stochastic control / Bellman equation / value iteration。

课程主页：
URL: [https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/)

Lecture slides：
URL: [https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/pages/lecture-notes/](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/pages/lecture-notes/)

Complete lecture notes：
URL: [https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/resources/mit6_231f15_notes/](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/resources/mit6_231f15_notes/)

MIT OCW 页面提供完整 lecture slides、assignments、exams 和 lecture notes，内容包括 finite horizon DP、Bellman equation、value iteration 等。([MIT OpenCourseWare][9])

建议读：

* Lecture 1–3：finite horizon DP
* Lecture 10 左右：value iteration / infinite horizon
* 不必一开始读 stochastic control 全部内容

学习 DP 的理由是：randomized level difference 与 MDP / value iteration 中的 sum of differences / variance reduction 之间有自然类比；理解这个类比至少需要 DP 语言。

---

## 3.3 SDDP tutorial / implementation resources

类型：教程 / 软件文档
优先级：中
用途：理解 SDDP 的算法直觉。

SDDP.jl theory intro：
URL: [https://sddp.dev/stable/explanation/theory_intro/](https://sddp.dev/stable/explanation/theory_intro/)

Introduction to SDDP slides：
URL: [https://cermics.enpc.fr/~delara/TEACHING/VL_MPRO_slides.pdf](https://cermics.enpc.fr/~delara/TEACHING/VL_MPRO_slides.pdf)

SDDP.jl 的 tutorial 用 simplified implementation 解释 stochastic dual dynamic programming 的算法机制。([sddp.dev][10])

建议用途：

* 软件细节可后置
* 只用来理解 forward pass、backward pass、cutting plane、value function approximation

---

## 3.4 Lan, Complexity of Stochastic Dual Dynamic Programming

类型：理论论文
优先级：中
用途：理解 SDDP complexity。

URL: [https://arxiv.org/abs/1912.07702](https://arxiv.org/abs/1912.07702)

PDF:
URL: [https://par.nsf.gov/servlets/purl/10232279](https://par.nsf.gov/servlets/purl/10232279)

这篇论文分析 deterministic DDP 和 SDDP 的 iteration complexity，并说明在 stagewise independence 假设下，SDDP 类方法适合处理多阶段问题，但复杂度通常与每阶段状态维度有关。([arXiv][11])

建议读：

* Abstract
* Introduction
* 了解 SDDP 为什么适合 many-stage but low-state-dimension problems

---

## 3.5 Lan & Zhou, Dynamic Stochastic Approximation for Multi-stage Stochastic Optimization

类型：理论论文
优先级：中高
用途：理解 stochastic approximation 路线如何处理 multistage problem。

Springer 页面：
URL: [https://link.springer.com/article/10.1007/s10107-020-01489-y](https://link.springer.com/article/10.1007/s10107-020-01489-y)

arXiv：
URL: [https://arxiv.org/abs/1707.03324](https://arxiv.org/abs/1707.03324)

PDF:
URL: [https://optimization-online.org/wp-content/uploads/2017/07/6125.pdf](https://optimization-online.org/wp-content/uploads/2017/07/6125.pdf)

这篇文章提出 DSA，用 stochastic first-order method 处理 convex multistage stochastic optimization；对于 three-stage 问题给出 $\mathcal O(1/\epsilon^4)$ 的 scenario complexity。([Springer][12])

建议读：

* Introduction
* Problem formulation
* Complexity statement
* 暂时不读技术证明

这篇是理解 MLMC-style multistage methods 的重要 baseline。

---

# Module 4. MLMC / randomized telescoping

这是后续 MLMC-based stochastic optimization 方法的核心技术背景，建议先单独学习，而不是直接从应用论文切入。

---

## 4.1 Giles, Multilevel Monte Carlo Methods

类型：综述 / survey
优先级：最高
用途：系统理解 MLMC。

Acta Numerica PDF：
URL: [https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf](https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf)

Cambridge 页面：
URL: [https://www.cambridge.org/core/journals/acta-numerica/article/multilevel-monte-carlo-methods/C5AF9A57ED8FF8FDF08074C1071C5511](https://www.cambridge.org/core/journals/acta-numerica/article/multilevel-monte-carlo-methods/C5AF9A57ED8FF8FDF08074C1071C5511)

Giles 个人 MLMC 页面：
URL: [https://people.maths.ox.ac.uk/gilesm/mlmc.html](https://people.maths.ox.ac.uk/gilesm/mlmc.html)

Cambridge 摘要说得很清楚：MLMC 通过大量 low-accuracy / low-cost simulations 加少量 high-accuracy / high-cost simulations 显著降低计算成本。([Cambridge University Press & Assessment][13])

需要掌握这个分解：

$$
\begin{aligned}
\mathbb E[P_L]
&= \mathbb E[P_0]
+ \sum_{\ell=1}^{L}\mathbb E[P_\ell-P_{\ell-1}].
\end{aligned}
$$

这是 neighboring-level difference 思想的基础版本。

---

## 4.2 Rhee & Glynn, Unbiased Estimation with Square Root Convergence

类型：核心论文
优先级：高
用途：理解 randomized telescoping / random level estimator。

PDF:
URL: [https://chrhee.github.io/papers/RheeGlynn13a.pdf](https://chrhee.github.io/papers/RheeGlynn13a.pdf)

Stanford 页面：
URL: [https://web.stanford.edu/~glynn/papers/2015/RheeG15.html](https://web.stanford.edu/~glynn/papers/2015/RheeG15.html)

Journal 页面：
URL: [https://pubsonline.informs.org/doi/10.1287/opre.2015.1404](https://pubsonline.informs.org/doi/10.1287/opre.2015.1404)

Rhee–Glynn 用一串 approximation 构造 unbiased estimator，这正是 randomized telescoping 的核心思想。([chrhee.github.io][14])

需要理解：

$$
Y = Y_0+\sum_{k=1}^{\infty}(Y_k-Y_{k-1})
$$

然后随机抽 $K$，构造类似：

$$
Y_0+\frac{Y_K-Y_{K-1}}{p_K}.
$$

这和 MLMC gradient / randomized level estimator 里的

$$
\frac{\widehat Q_k-\widehat Q_{k-1}}{p_k}
$$

是同一个思想家族。

---

# Module 5. Classical Bilevel Optimization

现在进入第二条主线。这里先暂时不处理 stochastic 和 deep learning 应用，而是先学习 classical bilevel 的数学语言。

---

## 5.1 Beck & Schmidt, A Gentle and Incomplete Introduction to Bilevel Optimization

类型：lecture notes
优先级：最高
用途：bilevel 入门第一材料。

PDF:
URL: [https://optimization-online.org/DB_FILE/2021/06/8450.pdf](https://optimization-online.org/DB_FILE/2021/06/8450.pdf)

另一个 PDF：
URL: [https://www.lamsade.dauphine.fr/poc/sites/default/files/bilevel-optimization.pdf](https://www.lamsade.dauphine.fr/poc/sites/default/files/bilevel-optimization.pdf)

这份讲义正式引入 bilevel optimization，并用例子解释 upper level、lower level、solution concepts、single-level reformulations、linear bilevel、mixed-integer linear bilevel 等。([Optimization Online][15])

建议读：

* Chapter 1：Introduction
* Chapter 2：Solution concepts
* Chapter 3：Single-level reformulations
* Chapter 4：Some theory on linear bilevel problems
* 后面的 MILP bilevel 先选读

需要掌握：

$$
\min_{x,y} F(x,y)
\quad
\operatorname{s.t.}
\quad
y\in S(x),
$$

其中

$$
S(x)=\arg\min_z f(x,z).
$$

关键点是：
**lower-level optimality 不是普通 constraint，而是一个 solution set mapping。**

---

## 5.2 Dempe, Bilevel Optimization: Theory, Algorithms and Applications

类型：survey / overview
优先级：高
用途：建立 classical bilevel 全貌。

URL: [https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf](https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf)

这篇综述适合了解 bilevel 的理论、算法、应用和参考文献。([Optimization Online][16])

建议读：

* Introduction
* Linear bilevel programming
* Nonlinear bilevel programming
* Optimality conditions
* Algorithms
* Applications

重点概念：

* optimistic bilevel
* pessimistic bilevel
* KKT reformulation
* optimal value function reformulation
* lower-level nonuniqueness
* bilevel hardness

---

## 5.3 Dempe & Zemkoho, Bilevel Optimization: Advances and Next Challenges

类型：论文集 / reference book
优先级：中
用途：后期查方向。

URL: [https://link.springer.com/book/10.1007/978-3-030-52119-6](https://link.springer.com/book/10.1007/978-3-030-52119-6)

Springer 页面说明这本书覆盖 bilevel optimization 的主要算法方法，包括 local、global、heuristic techniques，也覆盖 linear、nonlinear、optimistic、pessimistic、mixed-integer bilevel optimization。([Springer][17])

建议用途：

* 不必从头通读
* 当作 reference
* 以后遇到某个子方向再回来查

---

## 5.4 Sinha, Malo, Deb, A Review on Bilevel Optimization: From Classical to Evolutionary Approaches and Applications

类型：review
优先级：中
用途：快速看应用和算法谱系。

arXiv:
URL: [https://arxiv.org/abs/1705.06270](https://arxiv.org/abs/1705.06270)

这篇 review 从 classical 到 evolutionary methods 都有覆盖，适合快速了解 bilevel 的应用面。([arXiv][18])

建议读：

* Introduction
* Basic concepts
* Classical methods
* Applications
* Evolutionary 部分可跳过

---

# Module 6. KKT reformulation、MPEC、implicit function

这是 bilevel 的数学核心。MPEC 的细节可以后置，但需要知道为什么 KKT reformulation 是 classical bilevel 的基本手段。

如果 lower-level 是凸优化，并且满足适当 constraint qualification，那么

$$
y\in\arg\min_y f(x,y)
$$

可以用 KKT 条件替换：

$$
\nabla_y f(x,y)+A^\top \lambda=0,
$$

$$
Ay\le b,\quad \lambda\ge 0,\quad \lambda_i(Ay-b)_i=0.
$$

于是 bilevel 变成 single-level problem with complementarity constraints，也就是 MPEC / MPCC。

---

## 6.1 Kim, Leyffer, Munson, MPEC Methods for Bilevel Optimization Problems

类型：survey / methods paper
优先级：中
用途：理解 bilevel 到 MPEC 的转换。

URL: [https://wiki.mcs.anl.gov/leyffer/images/8/8d/MPEC-survey.pdf](https://wiki.mcs.anl.gov/leyffer/images/8/8d/MPEC-survey.pdf)

建议用途：

* 读 introduction
* 看 bilevel 到 MPEC 的 reformulation
* 了解 complementarity constraints 为什么麻烦

---

## 6.2 Luo, Pang, Ralph, Mathematical Programs with Equilibrium Constraints

类型：经典书
优先级：低到中，后期 reference
用途：MPEC 理论。

Preview:
URL: [https://api.pageplace.de/preview/DT0400.9780511899003_A25932741/preview-9780511899003_A25932741.pdf](https://api.pageplace.de/preview/DT0400.9780511899003_A25932741/preview-9780511899003_A25932741.pdf)

这本比较深入。当前阶段只需要知道它是 MPEC 的经典 reference，不建议在第一轮完整通读。

---

# Module 7. Gradient-based Bilevel / Hypergradient / ML 中的 bilevel

这一模块把 bilevel 和现代 ML / differentiable optimization 连接起来。它和 CSBO、meta-learning、decision-focused learning 都有关。

---

## 7.1 University of Toronto CSC2541 Lecture 11: Bilevel Optimization

类型：公开课 slides
优先级：高
用途：快速理解 ML 里的 bilevel、implicit differentiation、unrolling。

Lecture 11 PDF:
URL: [https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf)

2022 课程页面：
URL: [https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2022/](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2022/)

这份 slides 直接把 bilevel optimization 放在 neural network training dynamics 和 hyperparameter optimization 的语境里讲。2022 课程页面也说明，bilevel optimization 是 objective depends on the optimal solution to another optimization problem 的问题，典型例子是 hyperparameter optimization。([U of T Computer Science][19])

建议读：

* Bilevel formulation
* Hyperparameter optimization example
* Implicit differentiation
* Unrolling

---

## 7.2 Pedregosa, Hyperparameter Optimization with Approximate Gradient

类型：经典论文
优先级：高
用途：理解 approximate hypergradient。

PDF:
URL: [https://proceedings.mlr.press/v48/pedregosa16.pdf](https://proceedings.mlr.press/v48/pedregosa16.pdf)

arXiv:
URL: [https://arxiv.org/abs/1602.02355](https://arxiv.org/abs/1602.02355)

这篇论文提出用 inexact gradient information 优化连续超参数，并允许在模型参数尚未完全收敛时更新超参数。([Proceedings of Machine Learning Research][20])

需要掌握这个推导：

lower level：

$$
w^*(\lambda)=
\arg\min_w L_{\mathrm{train}}(w,\lambda).
$$

first-order condition：

$$
\nabla_w L_{\mathrm{train}}(w^*(\lambda),\lambda)=0.
$$

implicit differentiation：

$$
\begin{aligned}
\frac{dw^*}{d\lambda}
&= -\left[
\nabla^2_{ww}L_{\mathrm{train}}
\right]^{-1}
\nabla^2_{\lambda w}L_{\mathrm{train}}.
\end{aligned}
$$

upper gradient：

$$
\nabla_\lambda L_{\mathrm{val}}(w^*(\lambda),\lambda).
$$

---

## 7.3 Franceschi et al., Bilevel Programming for Hyperparameter Optimization and Meta-Learning

类型：经典 ML bilevel 论文
优先级：高
用途：理解 bilevel 如何统一 hyperparameter optimization 和 meta-learning。

arXiv:
URL: [https://arxiv.org/abs/1806.04910](https://arxiv.org/abs/1806.04910)

PDF:
URL: [https://proceedings.mlr.press/v80/franceschi18a/franceschi18a.pdf](https://proceedings.mlr.press/v80/franceschi18a/franceschi18a.pdf)

这篇论文用 bilevel programming 统一 gradient-based hyperparameter optimization 和 meta-learning。([arXiv][21])

建议读：

* Introduction
* Bilevel formulation
* Approximate bilevel problem
* Meta-learning example
* 证明可以后置

---

## 7.4 Chen et al., Gradient-based Bi-level Optimization for Deep Learning: A Survey

类型：survey
优先级：中
用途：总览 deep learning 中的 bilevel solvers。

arXiv:
URL: [https://arxiv.org/abs/2207.11719](https://arxiv.org/abs/2207.11719)

HTML:
URL: [https://arxiv.org/html/2207.11719v4](https://arxiv.org/html/2207.11719v4)

这篇 survey 系统介绍 gradient-based bilevel optimization 在 deep learning 里的定义、任务分类和 solvers，包括 explicit gradient、proxy update、implicit function update、closed-form update 等。([arXiv][22])

建议读：

* Section 2：formal definition
* Section 3：task formulation
* Section 4：solvers
* 后面的应用按需读

---

# Module 8. Bilevel under uncertainty / stochastic bilevel

这一模块把第二条主线和第一条主线开始接起来。

---

## 8.1 Beck, Ljubić, Schmidt, A Survey on Bilevel Optimization Under Uncertainty

类型：survey
优先级：高
用途：连接 bilevel 和 uncertainty。

ScienceDirect:
URL: [https://www.sciencedirect.com/science/article/pii/S0377221723000073](https://www.sciencedirect.com/science/article/pii/S0377221723000073)

Preprint PDF:
URL: [https://opus4.kobv.de/opus4-trr154/files/491/bilevel-under-uncertainty-survey-preprint.pdf](https://opus4.kobv.de/opus4-trr154/files/491/bilevel-under-uncertainty-survey-preprint.pdf)

这篇 survey 专门讨论 bilevel optimization under uncertainty，是 bilevel 与 stochastic / robust / uncertain decision-making 交叉的好入口。([ScienceDirect][23])

建议读：

* Introduction
* Uncertainty enters upper level / lower level / both
* Stochastic bilevel 部分
* Robust bilevel 部分可以选读

---

## 8.2 Hu et al., Contextual Stochastic Bilevel Optimization

类型：前沿论文
优先级：高，但放在后面读
用途：连接 CSO、bilevel、uncertainty 和 MLMC。

arXiv:
URL: [https://arxiv.org/abs/2310.18535](https://arxiv.org/abs/2310.18535)

PDF:
URL: [https://arxiv.org/pdf/2310.18535](https://arxiv.org/pdf/2310.18535)

NeurIPS PDF:
URL: [https://proceedings.neurips.cc/paper_files/paper/2023/file/f77d9409647c096789067c09455858a2-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/f77d9409647c096789067c09455858a2-Paper-Conference.pdf)

这篇论文提出 CSBO，也就是 lower-level problem conditioned on contextual information and upper-level decision variable 的 stochastic bilevel framework，并用 MLMC 设计 gradient method。([arXiv][24])

建议读：

* Introduction
* Problem formulation
* Relation to CSO / meta-learning / personalized federated learning
* MLMC method intuition
* theorem 可以先不细读

---

# Module 9. Conditional Stochastic Optimization 与 MLMC-based stochastic methods

这是路线最后的交叉部分。如果前面的 stochastic programming、MLMC、bilevel 背景不足，直接读这里会比较困难。

---

## 9.1 Hu, Chen, He, Sample Complexity of Sample Average Approximation for Conditional Stochastic Optimization

类型：核心论文
优先级：高
用途：理解 CSO 和 $\epsilon^{-4}$ 的来源。

arXiv:
URL: [https://arxiv.org/abs/1905.11957](https://arxiv.org/abs/1905.11957)

SIAM 页面：
URL: [https://epubs.siam.org/doi/10.1137/19M1284865](https://epubs.siam.org/doi/10.1137/19M1284865)

这篇论文研究 CSO：

$$
\min_{x\in\mathcal X}
\mathbb E_\xi
f_\xi
\left(
\mathbb E_{\eta|\xi}[g_\eta(x,\xi)]
\right).
$$

arXiv 摘要里明确说，它在不同结构假设下分析 SAA sample complexity，一般情况有 $\mathcal O(d/\epsilon^4)$ 类型复杂度，smoothness 和 quadratic growth 可以改善复杂度。([arXiv][25])

建议读：

* Introduction
* CSO formulation
* Main complexity results
* numerical experiments 可略读

---

## 9.2 Hu, Zhang, Chen, He, Biased Stochastic First-Order Methods for Conditional Stochastic Optimization and Applications in Meta Learning

类型：核心论文
优先级：高
用途：理解 biased gradient oracle。

arXiv:
URL: [https://arxiv.org/abs/2002.10790](https://arxiv.org/abs/2002.10790)

这篇论文的核心是：CSO 因为 composition structure 很难构造 unbiased gradient estimator，所以用 biased stochastic gradient，并分析 bias–variance tradeoff 和复杂度。([arXiv][26])

建议读：

* Introduction
* Why unbiased gradient is hard
* BSGD algorithm
* Bias–variance tradeoff
* lower bound 部分先读结论

---

## 9.3 Hu, Chen, He, On the Bias-Variance-Cost Tradeoff of Stochastic Optimization

类型：非常核心论文
优先级：最高
用途：理解 MLMC gradient methods 的方法论核心。

NeurIPS 页面：
URL: [https://proceedings.neurips.cc/paper/2021/hash/b986700c627db479a4d9460b75de7222-Abstract.html](https://proceedings.neurips.cc/paper/2021/hash/b986700c627db479a4d9460b75de7222-Abstract.html)

PDF:
URL: [https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf)

这篇论文研究 MLMC gradient methods，并把 bias、variance、oracle cost 三者放在统一 tradeoff 框架里。它还明确说这种 setting 捕捉了 conditional stochastic optimization、bilevel optimization、DRO 等问题。([NeurIPS Proceedings][27])

这是后半段最值得精读的一篇。

需要读懂 bias、variance、cost 为什么构成三维 tradeoff，而不是普通统计里的 bias–variance tradeoff。

---

## 9.4 Hu, Wang, Chen, He, Multi-level Monte-Carlo Gradient Methods for Stochastic Optimization with Biased Oracles

类型：进阶论文
优先级：中高
用途：系统扩展 MLMC gradient with biased oracles。

arXiv:
URL: [https://arxiv.org/abs/2408.11084](https://arxiv.org/abs/2408.11084)

OpenReview PDF:
URL: [https://openreview.net/pdf?id=8mjQQDzU1a](https://openreview.net/pdf?id=8mjQQDzU1a)

这篇论文系统研究 biased stochastic oracles 下的 MLMC gradient methods，覆盖 strongly convex、convex、nonconvex，并讨论 CSO、DRO、shortfall risk optimization、contrastive learning 等应用。([arXiv][28])

建议读：

* 建议在 9.3 之后再读
* 重点看 general framework 和 application table
* 证明后置

---

## 9.5 Şen, Hu, Kuhn, Multistage Conditional Compositional Optimization

类型：前沿论文
优先级：高，但最后读
用途：从 CSO / MLMC 走回 multistage。

arXiv:
URL: [https://arxiv.org/abs/2604.14075](https://arxiv.org/abs/2604.14075)

PDF:
URL: [https://optimization-online.org/wp-content/uploads/2026/04/mcco-1.pdf](https://optimization-online.org/wp-content/uploads/2026/04/mcco-1.pdf)

这篇 2026 预印本提出 MCCO，把 multistage stochastic programming 和 conditional stochastic optimization 的特征结合起来；摘要明确说 naive nested sampling 的 scenario complexity 随 nests 指数增长，而他们用 MLMC 技术把复杂度改成随精度多项式增长。([arXiv][29])

建议读：

* 最后读
* 先读 Introduction 和 formulation
* 可作为最终 integrative reading

---

# 一条推荐阅读顺序

实际执行时，不建议按模块编号线性阅读；更稳妥的顺序是：

## 第一阶段：建立 stochastic programming 语言

1. Shapiro & Philpott tutorial
   URL: [https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf](https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf)

2. Birge & Louveaux, Introduction to Stochastic Programming
   URL: [https://link.springer.com/book/10.1007/978-1-4614-0237-4](https://link.springer.com/book/10.1007/978-1-4614-0237-4)

3. Kim–Pasupathy–Henderson, A Guide to SAA
   URL: [https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf](https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf)

4. Leclère, Stochastic and Dynamic Programming slides
   URL: [https://leclere.github.io/teaching/OS](https://leclere.github.io/teaching/OS)

---

## 第二阶段：建立 bilevel 语言

5. Beck & Schmidt, A Gentle and Incomplete Introduction to Bilevel Optimization
   URL: [https://optimization-online.org/DB_FILE/2021/06/8450.pdf](https://optimization-online.org/DB_FILE/2021/06/8450.pdf)

6. Dempe, Bilevel Optimization: Theory, Algorithms and Applications
   URL: [https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf](https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf)

7. Toronto CSC2541 Lecture 11, Bilevel Optimization
   URL: [https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf)

8. Pedregosa, Hyperparameter Optimization with Approximate Gradient
   URL: [https://proceedings.mlr.press/v48/pedregosa16.pdf](https://proceedings.mlr.press/v48/pedregosa16.pdf)

---

## 第三阶段：补 multistage 和 MLMC

9. Shapiro, On Complexity of Multistage Stochastic Programs
   URL: [https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf](https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf)

10. MIT OCW 6.231 Dynamic Programming and Stochastic Control
    URL: [https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/)

11. Giles, Multilevel Monte Carlo Methods
    URL: [https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf](https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf)

12. Rhee & Glynn, Unbiased Estimation with Square Root Convergence
    URL: [https://chrhee.github.io/papers/RheeGlynn13a.pdf](https://chrhee.github.io/papers/RheeGlynn13a.pdf)

---

## 第四阶段：进入交叉前沿

13. Beck–Ljubić–Schmidt, Bilevel Optimization Under Uncertainty
    URL: [https://opus4.kobv.de/opus4-trr154/files/491/bilevel-under-uncertainty-survey-preprint.pdf](https://opus4.kobv.de/opus4-trr154/files/491/bilevel-under-uncertainty-survey-preprint.pdf)

14. Hu–Chen–He, Sample Complexity of SAA for CSO
    URL: [https://arxiv.org/abs/1905.11957](https://arxiv.org/abs/1905.11957)

15. Hu–Zhang–Chen–He, Biased Stochastic First-Order Methods for CSO
    URL: [https://arxiv.org/abs/2002.10790](https://arxiv.org/abs/2002.10790)

16. Hu–Chen–He, Bias-Variance-Cost Tradeoff
    URL: [https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf)

17. Hu et al., Contextual Stochastic Bilevel Optimization
    URL: [https://arxiv.org/pdf/2310.18535](https://arxiv.org/pdf/2310.18535)

18. Şen–Hu–Kuhn, Multistage Conditional Compositional Optimization
    URL: [https://optimization-online.org/wp-content/uploads/2026/04/mcco-1.pdf](https://optimization-online.org/wp-content/uploads/2026/04/mcco-1.pdf)

---

# 最小必读清单

如果时间有限，可以只保留下面 10 个：

1. Duchi stochastic optimization notes
   URL: [https://web.stanford.edu/~jduchi/PCMIConvex/Duchi16.pdf](https://web.stanford.edu/~jduchi/PCMIConvex/Duchi16.pdf)

2. Shapiro & Philpott tutorial
   URL: [https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf](https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf)

3. Birge & Louveaux textbook
   URL: [https://link.springer.com/book/10.1007/978-1-4614-0237-4](https://link.springer.com/book/10.1007/978-1-4614-0237-4)

4. Leclère stochastic and dynamic programming course
   URL: [https://leclere.github.io/teaching/OS](https://leclere.github.io/teaching/OS)

5. Beck & Schmidt bilevel notes
   URL: [https://optimization-online.org/DB_FILE/2021/06/8450.pdf](https://optimization-online.org/DB_FILE/2021/06/8450.pdf)

6. Dempe bilevel overview
   URL: [https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf](https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf)

7. Toronto bilevel lecture
   URL: [https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf)

8. Giles MLMC survey
   URL: [https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf](https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf)

9. Rhee & Glynn randomized telescoping
   URL: [https://chrhee.github.io/papers/RheeGlynn13a.pdf](https://chrhee.github.io/papers/RheeGlynn13a.pdf)

10. Hu–Chen–He bias–variance–cost
    URL: [https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf)

这个最小清单覆盖了：

* stochastic optimization
* stochastic programming
* bilevel
* MLMC
* biased oracle

---

# 学完后应该形成的知识地图

最后应能把这些内容放进同一张图里：

## Stochastic Optimization

解决：

$$
\min_x \mathbb E[f(x,\xi)].
$$

主要工具：

* SGD
* SAA
* stochastic mirror descent
* oracle complexity

---

## Stochastic Programming

解决：

$$
\min_x c^\top x+\mathbb E[Q(x,\xi)].
$$

主要对象：

* recourse value function
* SAA
* scenario tree
* decomposition

---

## Multistage Stochastic Programming

解决：

$$
\begin{aligned}
Q_t(x_{t-1},\xi_t)
&= \min_{x_t}
\left\{
c_t^\top x_t+
\mathbb E[Q_{t+1}(x_t,\xi_{t+1})\mid \xi_t]
\right\}.
\end{aligned}
$$

主要困难：

* conditional sampling
* scenario tree explosion
* nonanticipativity
* value function approximation
* curse of stages

---

## Bilevel Optimization

解决：

$$
\min_{x,y} F(x,y)
\quad
\operatorname{s.t.}
\quad
y\in\arg\min_z f(x,z).
$$

主要困难：

* lower-level solution mapping
* nonunique lower-level solutions
* optimistic / pessimistic solution
* KKT reformulation
* MPEC

---

## Gradient-based Bilevel

解决：

$$
\min_\lambda L_{\mathrm{val}}(w^*(\lambda),\lambda),
\quad
w^*(\lambda)=\arg\min_w L_{\mathrm{train}}(w,\lambda).
$$

主要工具：

* implicit differentiation
* unrolling
* hypergradient
* approximate inverse Hessian

---

## MLMC / Randomized Telescoping

解决：high-accuracy estimator 太贵。

主要思想：

$$
Y_L = Y_0+\sum_{\ell=1}^L(Y_\ell-Y_{\ell-1}),
$$

用 level randomization 降低 expected cost。

---

## CSO / bilevel / MLMC 的交叉点

核心是三类结构的叠加：

* conditional stochastic structure
* inner optimization / bilevel structure
* multilevel estimator

也就是说，这份 roadmap 不是围绕某一篇论文，而是在搭建一个研究交叉区的基础：**随机优化、随机规划、bilevel、MLMC、oracle complexity 的交叉地带**。这条线技术上较深，但对后续理解 optimization theory、decision-focused learning、stochastic bilevel 和 biased oracle methods 都有帮助。

[1]: https://web.stanford.edu/~jduchi/PCMIConvex/Duchi16.pdf?utm_source=chatgpt.com "Introductory Lectures on Stochastic Optimization"
[2]: https://arxiv.org/abs/1405.4980?utm_source=chatgpt.com "Convex Optimization: Algorithms and Complexity"
[3]: https://link.springer.com/book/10.1007/978-1-4614-0237-4?utm_source=chatgpt.com "Introduction to Stochastic Programming | Springer Nature Link"
[4]: https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/4/1470/files/2021/03/SPbook.pdf?utm_source=chatgpt.com "LECTURES ON STOCHASTIC PROGRAMMING - CDN"
[5]: https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf?utm_source=chatgpt.com "A Guide to Sample-Average Approximation"
[6]: https://optimization-online.org/wp-content/uploads/2004/10/978.pdf?utm_source=chatgpt.com "On complexity of stochastic programming problems"
[7]: https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf?utm_source=chatgpt.com "On Complexity of Multistage Stochastic Programs"
[8]: https://leclere.github.io/teaching/OS?utm_source=chatgpt.com "Stochastic Optimization"
[9]: https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/pages/lecture-notes/?utm_source=chatgpt.com "Lecture Slides | Dynamic Programming and Stochastic ..."
[10]: https://sddp.dev/stable/explanation/theory_intro/?utm_source=chatgpt.com "Introductory theory"
[11]: https://arxiv.org/abs/1912.07702?utm_source=chatgpt.com "Complexity of Stochastic Dual Dynamic Programming"
[12]: https://link.springer.com/article/10.1007/s10107-020-01489-y?utm_source=chatgpt.com "Dynamic stochastic approximation for multi-stage stochastic ..."
[13]: https://www.cambridge.org/core/journals/acta-numerica/article/multilevel-monte-carlo-methods/C5AF9A57ED8FF8FDF08074C1071C5511?utm_source=chatgpt.com "Multilevel Monte Carlo methods | Acta Numerica"
[14]: https://chrhee.github.io/papers/RheeGlynn13a.pdf?utm_source=chatgpt.com "Unbiased Estimation with Square Root Convergence for ..."
[15]: https://optimization-online.org/DB_FILE/2021/06/8450.pdf?utm_source=chatgpt.com "A Gentle and Incomplete Introduction to Bilevel Optimization"
[16]: https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf?utm_source=chatgpt.com "Bilevel optimization: theory, algorithms and applications"
[17]: https://link.springer.com/book/10.1007/978-3-030-52119-6?utm_source=chatgpt.com "Bilevel Optimization: Advances and Next Challenges"
[18]: https://arxiv.org/abs/1705.06270?utm_source=chatgpt.com "A Review on Bilevel Optimization: From Classical to Evolutionary Approaches and Applications"
[19]: https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf?utm_source=chatgpt.com "Lecture 11 - Bilevel Optimization"
[20]: https://proceedings.mlr.press/v48/pedregosa16.pdf?utm_source=chatgpt.com "Hyperparameter optimization with approximate gradient"
[21]: https://arxiv.org/abs/1806.04910?utm_source=chatgpt.com "Bilevel Programming for Hyperparameter Optimization and Meta-Learning"
[22]: https://arxiv.org/abs/2207.11719?utm_source=chatgpt.com "Gradient-based Bi-level Optimization for Deep Learning: A Survey"
[23]: https://www.sciencedirect.com/science/article/pii/S0377221723000073?utm_source=chatgpt.com "A survey on bilevel optimization under uncertainty"
[24]: https://arxiv.org/abs/2310.18535?utm_source=chatgpt.com "Contextual Stochastic Bilevel Optimization"
[25]: https://arxiv.org/abs/1905.11957?utm_source=chatgpt.com "Sample Complexity of Sample Average Approximation for Conditional Stochastic Optimization"
[26]: https://arxiv.org/abs/2002.10790?utm_source=chatgpt.com "Biased Stochastic First-Order Methods for Conditional Stochastic Optimization and Applications in Meta Learning"
[27]: https://proceedings.neurips.cc/paper/2021/hash/b986700c627db479a4d9460b75de7222-Abstract.html?utm_source=chatgpt.com "On the Bias-Variance-Cost Tradeoff of Stochastic ..."
[28]: https://arxiv.org/abs/2408.11084?utm_source=chatgpt.com "Multi-level Monte-Carlo Gradient Methods for Stochastic Optimization with Biased Oracles"
[29]: https://arxiv.org/abs/2604.14075?utm_source=chatgpt.com "Multistage Conditional Compositional Optimization"
