---
title: "End-to-End Decision-Based Cardinality-Constrained Portfolio Optimization"
aliases:
  - "E2E Decision-Based Cardinality-Constrained Portfolio Optimization"
  - "Anis Kwon 2025 cardinality constrained portfolio"
type: "paper-note"
status: "seed"
tags:
  - reading/papers
  - topic/decision-focused-learning
  - topic/portfolio-optimization
  - topic/sparse-optimization
---

> [!summary] Reading status
> Seed note created from the local Beamer deck. The PDF is mirrored into the site so the talk can be viewed from the page.

## Citation

Hassan T. Anis and Roy H. Kwon, "End-to-end, decision-based, cardinality-constrained portfolio optimization," _European Journal of Operational Research_, 320(3), 739-753, 2025.

## Reading Handle

The paper studies decision-focused learning for sparse minimum-variance portfolio optimization. Instead of fitting a covariance model only for prediction accuracy, it trains the factor-risk model through a downstream cardinality-constrained optimizer, using realized portfolio performance as the learning signal.

## Slides

[Open the mirrored PDF](slides/E2E-Cardinality-Portfolio-Slides.pdf)

![[slides/E2E-Cardinality-Portfolio-Slides.pdf]]

## Core Setup

Given an asset covariance matrix $\Sigma \in \mathbb{R}^{N \times N}$, the downstream decision is a long-only sparse portfolio:

$$
\min_{w \in \mathcal{W}_k} w^\top \Sigma w,
\qquad
\mathcal{W}_k
= \{w \in \mathbb{R}_+^N : \mathbf{1}^\top w = 1,\ \lVert w\rVert_0 \le k\}.
$$

The learning problem is hard because the selected support can change discontinuously when the covariance estimate changes.

## Method Snapshot

- Use a factor covariance model $\Sigma_\theta = B\Sigma_f B^\top + \Psi$.
- Replace the original mixed-integer sparse portfolio problem with continuous relaxations that can act as differentiable optimization layers.
- Train the risk-model parameters end to end by backpropagating realized decision loss through the relaxation layer.
- Compare Big-M, SOCP, and SDP relaxation layers against decoupled factor-model baselines.

## Notes To Fill

- Why the loose Big-M relaxation can outperform tighter SOCP/SDP layers out of sample.
- How the circular block bootstrap changes the effective training distribution.
- Whether realized Sharpe ratio is too noisy as a training objective.
- What transaction costs would do if moved from evaluation into the training loss.
