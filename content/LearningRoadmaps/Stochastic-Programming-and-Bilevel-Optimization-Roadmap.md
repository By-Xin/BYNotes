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
> [!quote] Last week, I attended a talk around Stochastic Optimization and Multistage Stochastic Programming. The talk was interesting, but I did not enjoy it, given my limited background, lol. Since the summer break is coming, I decided to turn this confusion into a small reading plan, and here's what ChatGPT suggests for this summer.

This roadmap discusses around two connected topics:

1. **Stochastic Programming / Multistage Stochastic Programming / MLMC**
2. **Bilevel Optimization / Stochastic Bilevel / Hypergradient**

---

# General Structure

This roadmap generally is composed of the following 8 sections:

1. Optimization and Stochastic Optimization Basics
2. Stochastic Programming
3. Multistage Stochastic Programming, and SDDP
4. MLMC / randomized telescoping
5. Classical Bilevel Optimization
6. Gradient-based Bilevel / Hypergradient
7. Stochastic Bilevel / Conditional Stochastic Optimization
8. Frontiers: CSBO, MCCO, and MLMC-based stochastic methods

---

# Module 0.  Prerequisites: Convex Optimization, Stochastic Optimization, Oracle Complexity

## 0.1 John Duchi, Introductory Lectures on Stochastic Optimization

Type: lecture notes / public course notes
Priority: high
Use: background for stochastic convex optimization, stochastic subgradient methods, mirror descent, sample complexity, and probabilistic analysis.

PDF: [Introductory Lectures on Stochastic Optimization](https://web.stanford.edu/~jduchi/PCMIConvex/Duchi16.pdf)
Course page: [Introductory Lectures on Stochastic Convex Optimization](https://stanford.edu/~jduchi/PCMIConvex/)

These PCMI lecture notes by John Duchi provide a compact introduction to stochastic optimization from the viewpoint of convex analysis and first-order methods. The notes start from basic convex analysis, then move to subgradient methods, stochastic subgradient methods, mirror descent, adaptive metrics, and finally optimality guarantees and sample complexity. For my purpose, they are a good starting point before reading more specialized material on conditional stochastic optimization, biased stochastic gradients, and multilevel Monte Carlo gradient estimators.

Suggested reading plan:

- Sections 1–2: basic setup and convex analysis background
- Section 3: [[7.Subgradient-Methods|subgradient and stochastic subgradient methods]]
- Section 4: mirror descent and adaptive metrics
- Section 5: optimality guarantees and sample complexity
- Technical appendices: keep as references and return to them when needed

---

## 0.2 Sébastien Bubeck, Convex Optimization: Algorithms and Complexity

Type: short book / monograph
Priority: high
Use: background for black-box optimization, oracle complexity, first-order methods, lower bounds, and stochastic gradient methods.

arXiv: [Convex Optimization: Algorithms and Complexity](https://arxiv.org/abs/1405.4980)
PDF: [Author-hosted PDF](https://sbubeck.com/Bubeck15.pdf)

This monograph by Sébastien Bubeck gives a systematic introduction to convex optimization from the viewpoint of algorithms and complexity. It starts with the black-box model and then develops the main ideas behind cutting-plane methods, [[5.Gradient-Descent|gradient descent, accelerated gradient methods]], mirror descent, [[23.Frank-Wolfe-Method|Frank-Wolfe]], and stochastic optimization.

For my purpose, this book is especially useful for building the right conceptual framework: lower bounds are not abstract barriers floating outside the problem. They are meaningful only after the oracle model, the function class, and the allowed type of information have been specified. This perspective is important before reading more specialized work on stochastic gradients, biased oracles, and conditional stochastic optimization.

Suggested reading plan:

- Chapter 1: basic convexity and the black-box model
- Gradient descent and accelerated gradient sections
- Mirror descent and non-Euclidean methods
- Stochastic gradient and mini-batch sections
- Lower-bound arguments: read first for intuition; postpone technical proofs if necessary

---

# Module 1. Stochastic Programming Introduction

This module is the basis of the first regime around stochastic programming, topics including recourse, SAA, scenario tree, nonanticipativity, value function, etc.

---

## 1.1 Römisch, A Tutorial on Stochastic Programming

Type: tutorial slides / workshop notes
Priority: very high
Use: building a first global picture of stochastic programming.

URL: [Stochastic Programming: Tutorial, Part I](https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf)

This short tutorial by W. Römisch is a friendly entry point to stochastic programming. It starts from the classical newsvendor example and then introduces the main modeling ideas: here-and-now decisions, recourse actions, two-stage stochastic programs, chance constraints, multistage models, and risk-averse formulations. For me, it works well as a first pass before reading heavier textbooks such as Birge–Louveaux or Shapiro et al.

Suggested reading plan:

- Read it once quickly from beginning to end.
- Focus on the modeling language of two-stage stochastic programming.
- Skim the technical propositions and return to them later if needed.

---

## 1.2 Birge & Louveaux, Introduction to Stochastic Programming

Type: textbook
Priority: essential
Use: the main introductory textbook for stochastic programming.

URL: [https://link.springer.com/book/10.1007/978-1-4614-0237-4](https://link.springer.com/book/10.1007/978-1-4614-0237-4)

This is a standard first textbook on stochastic programming. It is suitable for building a systematic understanding of how uncertainty is modeled in optimization, especially through two-stage recourse problems, deterministic equivalents, decomposition methods, and multistage formulations.

Suggested reading:

- Introduction and examples
- Basic properties
- Two-stage recourse problems
- Deterministic equivalent formulations
- Decomposition and the L-shaped method
- Sampling-based approximation methods
- Multistage formulation, with algorithmic details postponed


---

## 1.3 Shapiro, Dentcheva, Ruszczyński, Lectures on Stochastic Programming: Modeling and Theory

Type: theoretical textbook
Priority: high, but not for the very first pass
Use: a main reference for stochastic programming theory.

SIAM third edition:
URL: [https://epubs.siam.org/doi/book/10.1137/1.9781611976595](https://epubs.siam.org/doi/book/10.1137/1.9781611976595)

2009 public PDF:
URL: [https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/4/1470/files/2021/03/SPbook.pdf](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/4/1470/files/2021/03/SPbook.pdf)

This book is more theoretical than Birge and Louveaux. It gives a rigorous treatment of stochastic programming models, sample average approximation, optimality theory, risk measures, and multistage stochastic programs. I would use it mainly as a reference book after getting some basic intuition from shorter tutorials and introductory materials.

Suggested reading:

- Chapter 1: stochastic programming models
- Sample average approximation chapters
- Multistage stochastic programs
- Risk measures, if needed later
- SDDP-related material can be postponed


---

# Module 2. SAA, Scenario Trees, and Multistage Complexity

This module explains why traditional multistage stochastic programming is often considered difficult, especially because of scenario tree growth and the curse of dimensionality.


---

## 2.1 Kim, Pasupathy, Henderson, A Guide to Sample Average Approximation

Type: survey / tutorial
Priority: high
Use: understanding sample average approximation.

URL: [https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf](https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf)

This tutorial gives a clear introduction to the sample average approximation principle. It explains why replacing an expectation by a finite sample average can be useful, what kinds of convergence results are available, and how SAA differs from stochastic approximation.

Suggested reading:

- Basic SAA principle
- Consistency
- Finite-sample guarantees
- Comparison with stochastic approximation


---

## 2.2 Shapiro & Nemirovski, On Complexity of Stochastic Programming Problems

Type: complexity paper
Priority: medium-high
Use: understanding the complexity gap between two-stage and multistage stochastic programming.

URL: [https://optimization-online.org/wp-content/uploads/2004/10/978.pdf](https://optimization-online.org/wp-content/uploads/2004/10/978.pdf)

This paper discusses computational complexity in stochastic programming. It is useful for understanding why two-stage stochastic programs can often be handled with sampling-based methods, while general multistage stochastic programs are much more difficult.

Suggested reading:

- Introduction
- Two-stage complexity discussion
- Multistage complexity discussion
- Proofs can be postponed


---

## 2.3 Shapiro, On Complexity of Multistage Stochastic Programs

Type: core background paper
Priority: high
Use: understanding why conditional sampling becomes difficult in multistage problems.

PDF:
URL: [https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf](https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf)

Journal page:
URL: [https://www.sciencedirect.com/science/article/abs/pii/S0167637705000325](https://www.sciencedirect.com/science/article/abs/pii/S0167637705000325)

This paper studies sample size requirements for solving multistage stochastic programs with conditional sampling and SAA. It is useful for understanding why nested conditional expectations are often associated with rapidly growing sampling costs.

Suggested reading:

- Introduction
- Problem formulation
- Main theorem
- Proofs can be skimmed in the first pass


---

# Module 3. Multistage Stochastic Programming, Dynamic Programming, and SDDP

This module introduces the traditional algorithmic language for multistage stochastic programming: dynamic programming, nested Benders decomposition, and stochastic dual dynamic programming.


---

## 3.1 Vincent Leclère, Stochastic and Dynamic Programming

Type: public course / slides / practical materials
Priority: very high
Use: course-style introduction to two-stage models, dynamic programming, decomposition, and SDDP.

Course page:
URL: [https://leclere.github.io/teaching/OS](https://leclere.github.io/teaching/OS)

Another course page:
URL: [https://cermics.enpc.fr/~leclerev/OptimizationSaclay.html](https://cermics.enpc.fr/~leclerev/OptimizationSaclay.html)

This course provides a structured entry point to stochastic optimization and dynamic programming. It includes materials on two-stage stochastic problems, dynamic programming, decomposition methods, and SDDP.

Suggested reading:

- Introduction to stochastic optimization
- Two-stage problems
- Dynamic programming
- Decomposition methods
- SDDP


---

## 3.2 MIT OCW 6.231, Dynamic Programming and Stochastic Control

Type: public course
Priority: medium-high
Use: background on dynamic programming, stochastic control, Bellman equations, and value iteration.

Course page:
URL: [https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/)

Lecture slides:
URL: [https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/pages/lecture-notes/](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/pages/lecture-notes/)

Complete lecture notes:
URL: [https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/resources/mit6_231f15_notes/](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/resources/mit6_231f15_notes/)

This OCW course is a standard reference for dynamic programming and stochastic control. For this roadmap, the main goal is not to master all of stochastic control, but to learn the basic language of finite-horizon DP, Bellman equations, and value iteration.

Suggested reading:

- Lectures 1–3: finite-horizon dynamic programming
- Value iteration / infinite-horizon dynamic programming
- Stochastic control topics can be read selectively


---

## 3.3 SDDP Tutorial and Implementation Resources

Type: tutorial / software documentation
Priority: medium
Use: understanding the algorithmic intuition behind SDDP.

SDDP.jl theory introduction:
URL: [https://sddp.dev/stable/explanation/theory_intro/](https://sddp.dev/stable/explanation/theory_intro/)

Introduction to SDDP slides:
URL: [https://cermics.enpc.fr/~delara/TEACHING/VL_MPRO_slides.pdf](https://cermics.enpc.fr/~delara/TEACHING/VL_MPRO_slides.pdf)

These resources are useful for building intuition about stochastic dual dynamic programming. The software details can be postponed; the main point is to understand the forward pass, backward pass, cutting planes, and value function approximation.

Suggested reading:

- Theory introduction
- Forward and backward passes
- Cutting-plane approximation
- Simple examples before software details


---

## 3.4 Lan, Complexity of Stochastic Dual Dynamic Programming

Type: theoretical paper
Priority: medium
Use: understanding complexity results for SDDP-type methods.

URL: [https://arxiv.org/abs/1912.07702](https://arxiv.org/abs/1912.07702)

PDF:
URL: [https://par.nsf.gov/servlets/purl/10232279](https://par.nsf.gov/servlets/purl/10232279)

This paper studies the iteration complexity of deterministic DDP and SDDP. It is useful for understanding why SDDP is well suited to many-stage problems with relatively low-dimensional state spaces.

Suggested reading:

- Abstract
- Introduction
- Main complexity statements
- Detailed proofs can be postponed


---

## 3.5 Lan & Zhou, Dynamic Stochastic Approximation for Multi-stage Stochastic Optimization

Type: theoretical paper
Priority: medium-high
Use: understanding how stochastic approximation can be used for multistage stochastic optimization.

Springer page:
URL: [https://link.springer.com/article/10.1007/s10107-020-01489-y](https://link.springer.com/article/10.1007/s10107-020-01489-y)

arXiv:
URL: [https://arxiv.org/abs/1707.03324](https://arxiv.org/abs/1707.03324)

PDF:
URL: [https://optimization-online.org/wp-content/uploads/2017/07/6125.pdf](https://optimization-online.org/wp-content/uploads/2017/07/6125.pdf)

This paper proposes dynamic stochastic approximation for convex multistage stochastic optimization. It is a useful baseline for later reading on MLMC-style methods for multistage problems.

Suggested reading:

- Introduction
- Problem formulation
- Main complexity statements
- Technical proofs can be postponed


---

# Module 4. MLMC and Randomized Telescoping

This module provides the technical background for MLMC-based stochastic optimization methods. It is better to study MLMC separately before reading papers that apply it to stochastic optimization or bilevel problems.


---

## 4.1 Giles, Multilevel Monte Carlo Methods

Type: survey
Priority: essential
Use: systematic introduction to multilevel Monte Carlo.

Acta Numerica PDF:
URL: [https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf](https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf)

Cambridge page:
URL: [https://www.cambridge.org/core/journals/acta-numerica/article/multilevel-monte-carlo-methods/C5AF9A57ED8FF8FDF08074C1071C5511](https://www.cambridge.org/core/journals/acta-numerica/article/multilevel-monte-carlo-methods/C5AF9A57ED8FF8FDF08074C1071C5511)

Giles's MLMC page:
URL: [https://people.maths.ox.ac.uk/gilesm/mlmc.html](https://people.maths.ox.ac.uk/gilesm/mlmc.html)

This survey is the standard starting point for multilevel Monte Carlo. The main idea is to combine many cheap low-accuracy simulations with fewer expensive high-accuracy simulations, using differences between neighboring levels to reduce computational cost.

Suggested reading:

- Introduction
- Basic MLMC estimator
- Cost and variance decomposition
- Applications can be read selectively


---

## 4.2 Rhee & Glynn, Unbiased Estimation with Square Root Convergence

Type: core paper
Priority: high
Use: understanding randomized telescoping and random-level estimators.

PDF:
URL: [https://chrhee.github.io/papers/RheeGlynn13a.pdf](https://chrhee.github.io/papers/RheeGlynn13a.pdf)

Stanford page:
URL: [https://web.stanford.edu/~glynn/papers/2015/RheeG15.html](https://web.stanford.edu/~glynn/papers/2015/RheeG15.html)

Journal page:
URL: [https://pubsonline.informs.org/doi/10.1287/opre.2015.1404](https://pubsonline.informs.org/doi/10.1287/opre.2015.1404)

This paper introduces an important unbiased estimation idea based on randomized telescoping sums. It is useful preparation for understanding randomized-level estimators in MLMC gradient methods.

Suggested reading:

- Introduction
- Basic construction of unbiased estimators
- Randomized telescoping idea
- Technical conditions can be revisited later


---

# Module 5. Classical Bilevel Optimization

This module starts the second main thread of the roadmap. The goal is to learn the mathematical language of classical bilevel optimization before moving to stochastic and machine learning applications.


---

## 5.1 Beck & Schmidt, A Gentle and Incomplete Introduction to Bilevel Optimization

Type: lecture notes
Priority: essential
Use: first introduction to bilevel optimization.

PDF:
URL: [https://optimization-online.org/DB_FILE/2021/06/8450.pdf](https://optimization-online.org/DB_FILE/2021/06/8450.pdf)

Another PDF:
URL: [https://www.lamsade.dauphine.fr/poc/sites/default/files/bilevel-optimization.pdf](https://www.lamsade.dauphine.fr/poc/sites/default/files/bilevel-optimization.pdf)

These lecture notes give a gentle introduction to bilevel optimization. They explain upper-level and lower-level problems, solution concepts, single-level reformulations, linear bilevel programming, and mixed-integer linear bilevel models.

Suggested reading:

- Chapter 1: introduction
- Chapter 2: solution concepts
- Chapter 3: single-level reformulations
- Chapter 4: linear bilevel problems
- Mixed-integer bilevel material can be read selectively


---

## 5.2 Dempe, Bilevel Optimization: Theory, Algorithms and Applications

Type: survey / overview
Priority: high
Use: building a broad view of classical bilevel optimization.

URL: [https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf](https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf)

This survey is useful for seeing the full landscape of bilevel optimization, including theory, algorithms, applications, and references. It can be read after the Beck and Schmidt notes, or used as a reference while reading them.

Suggested reading:

- Introduction
- Linear bilevel programming
- Nonlinear bilevel programming
- Optimality conditions
- Algorithms
- Applications


---

## 5.3 Dempe & Zemkoho, Bilevel Optimization: Advances and Next Challenges

Type: edited reference book
Priority: medium
Use: reference for later study.

URL: [https://link.springer.com/book/10.1007/978-3-030-52119-6](https://link.springer.com/book/10.1007/978-3-030-52119-6)

This book collects advanced topics in bilevel optimization, including local, global, and heuristic methods, as well as linear, nonlinear, optimistic, pessimistic, and mixed-integer bilevel optimization. It is not necessary to read it from beginning to end.

Suggested use:

- Keep it as a reference
- Return to it when a specific subtopic becomes relevant
- Do not include it in the first reading pass


---

## 5.4 Sinha, Malo, Deb, A Review on Bilevel Optimization: From Classical to Evolutionary Approaches and Applications

Type: review
Priority: medium
Use: quick overview of applications and algorithm families.

arXiv:
URL: [https://arxiv.org/abs/1705.06270](https://arxiv.org/abs/1705.06270)

This review covers both classical and evolutionary approaches to bilevel optimization. For this roadmap, it is most useful as a broad overview of applications and algorithmic categories.

Suggested reading:

- Introduction
- Basic concepts
- Classical methods
- Applications
- Evolutionary methods can be skipped in the first pass


---

# Module 6. KKT Reformulation, MPEC, and Implicit Function Ideas

This module introduces the mathematical bridge from bilevel optimization to single-level reformulations. The full theory of MPEC can be postponed, but it is important to know why KKT reformulation is a standard tool in classical bilevel optimization.


---

## 6.1 Kim, Leyffer, Munson, MPEC Methods for Bilevel Optimization Problems

Type: survey / methods paper
Priority: medium
Use: understanding how bilevel problems can be reformulated as MPECs.

URL: [https://wiki.mcs.anl.gov/leyffer/images/8/8d/MPEC-survey.pdf](https://wiki.mcs.anl.gov/leyffer/images/8/8d/MPEC-survey.pdf)

This paper explains how bilevel optimization problems can be reformulated as mathematical programs with equilibrium constraints. It is mainly useful for understanding the role of complementarity constraints and why they create additional algorithmic difficulties.

Suggested reading:

- Introduction
- Bilevel-to-MPEC reformulation
- Complementarity constraints
- Algorithmic details can be postponed


---

## 6.2 Luo, Pang, Ralph, Mathematical Programs with Equilibrium Constraints

Type: classic book
Priority: low to medium
Use: later reference for MPEC theory.

Preview:
URL: [https://api.pageplace.de/preview/DT0400.9780511899003_A25932741/preview-9780511899003_A25932741.pdf](https://api.pageplace.de/preview/DT0400.9780511899003_A25932741/preview-9780511899003_A25932741.pdf)

This is a classic reference on mathematical programs with equilibrium constraints. It is too detailed for the first pass, but useful to know as a later theoretical reference.

Suggested use:

- Do not read from beginning to end now
- Use as a reference when MPEC theory becomes necessary


---

# Module 7. Gradient-Based Bilevel Optimization, Hypergradients, and Machine Learning

This module connects bilevel optimization with modern machine learning, differentiable optimization, hyperparameter optimization, and meta-learning.


---

## 7.1 University of Toronto CSC2541 Lecture 11: Bilevel Optimization

Type: public lecture slides
Priority: high
Use: quick introduction to bilevel optimization in machine learning.

Lecture 11 PDF:
URL: [https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf)

2022 course page:
URL: [https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2022/](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2022/)

These slides explain bilevel optimization in the context of neural network training dynamics and hyperparameter optimization. They are useful for quickly understanding how implicit differentiation and unrolling appear in machine learning.

Suggested reading:

- Bilevel formulation
- Hyperparameter optimization example
- Implicit differentiation
- Unrolling


---

## 7.2 Pedregosa, Hyperparameter Optimization with Approximate Gradient

Type: classic paper
Priority: high
Use: understanding approximate hypergradients.

PDF:
URL: [https://proceedings.mlr.press/v48/pedregosa16.pdf](https://proceedings.mlr.press/v48/pedregosa16.pdf)

arXiv:
URL: [https://arxiv.org/abs/1602.02355](https://arxiv.org/abs/1602.02355)

This paper studies hyperparameter optimization using approximate gradient information. It is useful for understanding how hyperparameters can be updated even when the lower-level model parameters are not solved exactly.

Suggested reading:

- Introduction
- Bilevel formulation of hyperparameter optimization
- Approximate gradient method
- Numerical examples
- Technical derivations can be revisited later


---

## 7.3 Franceschi et al., Bilevel Programming for Hyperparameter Optimization and Meta-Learning

Type: classic machine learning bilevel paper
Priority: high
Use: understanding how bilevel programming unifies hyperparameter optimization and meta-learning.

arXiv:
URL: [https://arxiv.org/abs/1806.04910](https://arxiv.org/abs/1806.04910)

PDF:
URL: [https://proceedings.mlr.press/v80/franceschi18a/franceschi18a.pdf](https://proceedings.mlr.press/v80/franceschi18a/franceschi18a.pdf)

This paper presents bilevel programming as a common framework for gradient-based hyperparameter optimization and meta-learning. It is a good bridge between classical bilevel optimization and modern ML applications.

Suggested reading:

- Introduction
- Bilevel formulation
- Approximate bilevel problem
- Meta-learning example
- Proofs can be postponed


---

## 7.4 Chen et al., Gradient-based Bi-level Optimization for Deep Learning: A Survey

Type: survey
Priority: medium
Use: overview of gradient-based bilevel solvers in deep learning.

arXiv:
URL: [https://arxiv.org/abs/2207.11719](https://arxiv.org/abs/2207.11719)

HTML:
URL: [https://arxiv.org/html/2207.11719v4](https://arxiv.org/html/2207.11719v4)

This survey gives a systematic overview of gradient-based bilevel optimization in deep learning. It covers definitions, task formulations, solver families, and applications.

Suggested reading:

- Section 2: formal definition
- Section 3: task formulation
- Section 4: solvers
- Applications can be read selectively


---

# Module 8. Bilevel Optimization Under Uncertainty

This module connects the bilevel thread with uncertainty, stochastic models, and robust decision-making.


---

## 8.1 Beck, Ljubić, Schmidt, A Survey on Bilevel Optimization Under Uncertainty

Type: survey
Priority: high
Use: connecting bilevel optimization with uncertainty.

ScienceDirect:
URL: [https://www.sciencedirect.com/science/article/pii/S0377221723000073](https://www.sciencedirect.com/science/article/pii/S0377221723000073)

Preprint PDF:
URL: [https://opus4.kobv.de/opus4-trr154/files/491/bilevel-under-uncertainty-survey-preprint.pdf](https://opus4.kobv.de/opus4-trr154/files/491/bilevel-under-uncertainty-survey-preprint.pdf)

This survey focuses on bilevel optimization under uncertainty. It is a good entry point for understanding how uncertainty can enter the upper level, the lower level, or both levels of a bilevel problem.

Suggested reading:

- Introduction
- Sources of uncertainty in bilevel optimization
- Stochastic bilevel optimization
- Robust bilevel optimization can be read selectively


---

## 8.2 Hu et al., Contextual Stochastic Bilevel Optimization

Type: frontier paper
Priority: high, but best read later
Use: connecting CSO, bilevel optimization, uncertainty, and MLMC.

arXiv:
URL: [https://arxiv.org/abs/2310.18535](https://arxiv.org/abs/2310.18535)

PDF:
URL: [https://arxiv.org/pdf/2310.18535](https://arxiv.org/pdf/2310.18535)

NeurIPS PDF:
URL: [https://proceedings.neurips.cc/paper_files/paper/2023/file/f77d9409647c096789067c09455858a2-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/f77d9409647c096789067c09455858a2-Paper-Conference.pdf)

This paper studies contextual stochastic bilevel optimization, where the lower-level problem depends on contextual information and the upper-level decision variable. It connects stochastic bilevel optimization with CSO-style structures and MLMC-based gradient methods.

Suggested reading:

- Introduction
- Problem formulation
- Connections to CSO, meta-learning, and personalized federated learning
- MLMC method intuition
- Theorems can be read later


---

# Module 9. Conditional Stochastic Optimization and MLMC-Based Stochastic Methods

This module is the final intersection of the roadmap. It is better to read it after gaining some background in stochastic programming, bilevel optimization, and MLMC.


---

## 9.1 Hu, Chen, He, Sample Complexity of Sample Average Approximation for Conditional Stochastic Optimization

Type: core paper
Priority: high
Use: understanding conditional stochastic optimization and the role of nested expectations.

arXiv:
URL: [https://arxiv.org/abs/1905.11957](https://arxiv.org/abs/1905.11957)

SIAM page:
URL: [https://epubs.siam.org/doi/10.1137/19M1284865](https://epubs.siam.org/doi/10.1137/19M1284865)

This paper studies sample average approximation for conditional stochastic optimization. It is useful for understanding why conditional expectation structures lead to more demanding sampling requirements than standard stochastic optimization.

Suggested reading:

- Introduction
- CSO formulation
- Main complexity results
- Numerical experiments can be skimmed


---

## 9.2 Hu, Zhang, Chen, He, Biased Stochastic First-Order Methods for Conditional Stochastic Optimization and Applications in Meta Learning

Type: core paper
Priority: high
Use: understanding biased stochastic gradients in CSO.

arXiv:
URL: [https://arxiv.org/abs/2002.10790](https://arxiv.org/abs/2002.10790)

This paper studies why unbiased gradient estimators are difficult to construct for conditional stochastic optimization and develops biased stochastic first-order methods. It is a useful bridge from CSO modeling to biased-oracle optimization methods.

Suggested reading:

- Introduction
- Why unbiased gradients are hard in CSO
- BSGD algorithm
- Bias-variance tradeoff
- Lower-bound results can be read selectively


---

## 9.3 Hu, Chen, He, On the Bias-Variance-Cost Tradeoff of Stochastic Optimization

Type: core paper
Priority: essential
Use: understanding the methodological core of MLMC gradient methods.

NeurIPS page:
URL: [https://proceedings.neurips.cc/paper/2021/hash/b986700c627db479a4d9460b75de7222-Abstract.html](https://proceedings.neurips.cc/paper/2021/hash/b986700c627db479a4d9460b75de7222-Abstract.html)

PDF:
URL: [https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf)

This paper develops a framework for stochastic optimization with biased gradient oracles, emphasizing the tradeoff between bias, variance, and oracle cost. It is one of the most important papers in the second half of this roadmap.

Suggested reading:

- Introduction
- Bias-variance-cost framework
- MLMC gradient method
- Applications to CSO, bilevel optimization, and related problems
- Proofs can be postponed


---

## 9.4 Hu, Wang, Chen, He, Multi-level Monte-Carlo Gradient Methods for Stochastic Optimization with Biased Oracles

Type: advanced paper
Priority: medium-high
Use: extending MLMC gradient methods for biased stochastic oracles.

arXiv:
URL: [https://arxiv.org/abs/2408.11084](https://arxiv.org/abs/2408.11084)

OpenReview PDF:
URL: [https://openreview.net/pdf?id=8mjQQDzU1a](https://openreview.net/pdf?id=8mjQQDzU1a)

This paper gives a broader treatment of MLMC gradient methods under biased stochastic oracles. It covers several optimization settings and applications, including CSO, distributionally robust optimization, shortfall risk optimization, and contrastive learning.

Suggested reading:

- Read after 9.3
- Introduction
- General framework
- Application table
- Proofs can be postponed


---

## 9.5 Şen, Hu, Kuhn, Multistage Conditional Compositional Optimization

Type: frontier paper
Priority: high, but read last
Use: connecting CSO, MLMC, and multistage stochastic programming.

arXiv:
URL: [https://arxiv.org/abs/2604.14075](https://arxiv.org/abs/2604.14075)

PDF:
URL: [https://optimization-online.org/wp-content/uploads/2026/04/mcco-1.pdf](https://optimization-online.org/wp-content/uploads/2026/04/mcco-1.pdf)

This paper proposes multistage conditional compositional optimization, combining features of multistage stochastic programming and conditional stochastic optimization. It is best treated as the final integrative reading in this roadmap.

Suggested reading:

- Read last
- Introduction
- Problem formulation
- Main algorithmic idea
- Complexity results can be read after the basic structure is clear


---

# Suggested Reading Order

In practice, it is better not to read the modules strictly in numerical order. A more stable path is the following.


## Stage 1. Build the Language of Stochastic Programming

1. Shapiro & Philpott tutorial
   URL: [https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf](https://www2.mathematik.hu-berlin.de/~romisch/papers/TutSing12.pdf)

2. Birge & Louveaux, Introduction to Stochastic Programming
   URL: [https://link.springer.com/book/10.1007/978-1-4614-0237-4](https://link.springer.com/book/10.1007/978-1-4614-0237-4)

3. Kim, Pasupathy, Henderson, A Guide to SAA
   URL: [https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf](https://people.orie.cornell.edu/shane/pubs/SAAGuide.pdf)

4. Leclère, Stochastic and Dynamic Programming
   URL: [https://leclere.github.io/teaching/OS](https://leclere.github.io/teaching/OS)


## Stage 2. Build the Language of Bilevel Optimization

5. Beck & Schmidt, A Gentle and Incomplete Introduction to Bilevel Optimization
   URL: [https://optimization-online.org/DB_FILE/2021/06/8450.pdf](https://optimization-online.org/DB_FILE/2021/06/8450.pdf)

6. Dempe, Bilevel Optimization: Theory, Algorithms and Applications
   URL: [https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf](https://optimization-online.org/wp-content/uploads/2018/08/6773.pdf)

7. Toronto CSC2541 Lecture 11, Bilevel Optimization
   URL: [https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/slides/lec11.pdf)

8. Pedregosa, Hyperparameter Optimization with Approximate Gradient
   URL: [https://proceedings.mlr.press/v48/pedregosa16.pdf](https://proceedings.mlr.press/v48/pedregosa16.pdf)


## Stage 3. Add Multistage Models and MLMC

9. Shapiro, On Complexity of Multistage Stochastic Programs
   URL: [https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf](https://optimization-online.org/wp-content/uploads/2005/01/1041.pdf)

10. MIT OCW 6.231, Dynamic Programming and Stochastic Control
    URL: [https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/)

11. Giles, Multilevel Monte Carlo Methods
    URL: [https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf](https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf)

12. Rhee & Glynn, Unbiased Estimation with Square Root Convergence
    URL: [https://chrhee.github.io/papers/RheeGlynn13a.pdf](https://chrhee.github.io/papers/RheeGlynn13a.pdf)


## Stage 4. Move to the Intersection

13. Beck, Ljubić, Schmidt, Bilevel Optimization Under Uncertainty
    URL: [https://opus4.kobv.de/opus4-trr154/files/491/bilevel-under-uncertainty-survey-preprint.pdf](https://opus4.kobv.de/opus4-trr154/files/491/bilevel-under-uncertainty-survey-preprint.pdf)

14. Hu, Chen, He, Sample Complexity of SAA for CSO
    URL: [https://arxiv.org/abs/1905.11957](https://arxiv.org/abs/1905.11957)

15. Hu, Zhang, Chen, He, Biased Stochastic First-Order Methods for CSO
    URL: [https://arxiv.org/abs/2002.10790](https://arxiv.org/abs/2002.10790)

16. Hu, Chen, He, Bias-Variance-Cost Tradeoff
    URL: [https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf)

17. Hu et al., Contextual Stochastic Bilevel Optimization
    URL: [https://arxiv.org/pdf/2310.18535](https://arxiv.org/pdf/2310.18535)

18. Şen, Hu, Kuhn, Multistage Conditional Compositional Optimization
    URL: [https://optimization-online.org/wp-content/uploads/2026/04/mcco-1.pdf](https://optimization-online.org/wp-content/uploads/2026/04/mcco-1.pdf)


---

# Minimal Reading List

If time is limited, keep only the following ten items.

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

10. Hu, Chen, He, Bias-Variance-Cost Tradeoff
    URL: [https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b986700c627db479a4d9460b75de7222-Paper.pdf)


---

# Final Picture

This roadmap is not centered on one single paper. It is meant to build the background for a research area where several themes meet:

- stochastic optimization
- stochastic programming
- multistage decision-making
- bilevel optimization
- MLMC and randomized estimators
- biased stochastic oracles

The first part builds the language of stochastic programming and multistage models. The second part introduces bilevel optimization, first from the classical side and then from the machine learning side. The last part connects these two lines through conditional stochastic optimization, biased gradient oracles, and MLMC-based methods.

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
