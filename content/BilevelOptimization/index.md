---
title: "Bilevel Optimization (2026 Summer School)"
type: "course-index"
status: "active"
tags:
  - course/bilevel-optimization
---

Notes from the 2026 summer school *Bilevel Optimization: Theory, Algorithms and AI Applications*. The course runs on two threads: a **theory** track deriving optimality conditions for bilevel programs and MPEC / MPCC through variational analysis (normal cones, coderivatives, value functions, partial calmness), and an **algorithms + applications** track on gradient-based methods (hypergradients, implicit differentiation) and their use in hyperparameter optimization, meta-learning, and pruning.

## Notes

| # | Note | Status |
|---|------|--------|
| 1 | [Optimality Conditions for MPECs via Variational Analysis](./1.Optimality-Conditions-for-MPEC-via-Variational-Analysis.md) | draft |
| 2 | [Bilevel Programs: Introduction, Reformulation and Partial Calmness](./2.Bilevel-Programs-Reformulation-and-Partial-Calmness.md) | draft |

## Concept Map

- **Theory — variational analysis**: KKT / Fritz John, constraint qualifications (NNAMCQ / PLICQ, MFCQ); MPCC and its game-theoretic origins (Nash, Stackelberg, Cournot); regular / limiting / Clarke normal cones, Clarke generalized gradient; S- / M- / C-stationarity; MPEC, coderivatives, calmness
- **Theory — bilevel programs**: value-function approach, sensitivity analysis, partial calmness
- **Algorithms**: gradient-based bilevel optimization — hypergradients, implicit differentiation, single- / double-loop methods
- **Applications**: hyperparameter optimization, meta-learning (MAML), model pruning, safe RL

## References

- Summer school: *Bilevel Optimization: Theory, Algorithms and AI Applications* (2026)
- Related roadmap: [Stochastic Programming and Bilevel Optimization Roadmap](../LearningRoadmaps/Stochastic-Programming-and-Bilevel-Optimization-Roadmap.md)

## Planned Notes

- Gradient-based algorithms for bilevel optimization (hypergradients, implicit / iterative differentiation)
- Applications in machine learning (hyperparameter optimization, meta-learning, pruning)
