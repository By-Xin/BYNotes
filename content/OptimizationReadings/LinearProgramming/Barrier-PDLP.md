---
title: "Barrier PDLP (arXiv, 2026)"
aliases:
  - "Barrier PDLP"
  - "BPDLP"
  - "A Barrier Primal Dual Hybrid Gradient Method for Solving Linear Programming Problems"
type: "paper-note"
status: "seed"
tags:
  - reading/papers
  - topic/linear-programming
  - topic/first-order-methods
  - topic/barrier-method
---

## Citation

Yingxin Zhou, Stefano Cipolla, and Phan T. Vuong, "A Barrier Primal Dual Hybrid Gradient Method for Solving Linear Programming Problems," _arXiv preprint arXiv:2608.26667_, 2026.

## Abstract

Zhou et al. introduce Barrier PDHG (BPDHG), which adds a logarithmic barrier to the PDHG framework for linear programming. The barrier replaces projection onto the nonnegative orthant with a closed-form proximal update that keeps primal iterates strictly positive. The resulting Barrier PDLP (BPDLP) method combines fixed-barrier BPDHG iterations with adaptive restarts, barrier-parameter updates, and warm starts between barrier stages. As the barrier parameter decreases, the perturbed KKT system approaches the KKT system of the original linear program.

## Slides

[Open the mirrored PDF](slides/Barrier-PDLP-Slides.pdf)

![[slides/Barrier-PDLP-Slides.pdf]]
