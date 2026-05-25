---
title: "Tree-Based Models"
aliases:
  - "Tree-based_Models"
  - "Tree-based Models"
  - "Decision Trees"
  - "Random Forest"
  - "StatisticalLearningAlgorithms/Nonparametric.Tree-Based-Models"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/tree-models
  - topic/nonparametric-models
---

## 1. Decision Trees

Pros:

- Explainable.
- Can handle both numerical and categorical data.

Cons:

- Non-robust, easily affected by noise.
  - Use ensemble methods to reduce variance.
- Complex trees can be overfitting.
  - Prune trees to simplify.
- Not easy to parallelize in computing.

## 2. Random Forest

- Train multiple decision trees to improve robustness.
  - Each tree is trained independently.
  - Majority voting for classification; average for regression.
- Randomness:
  - Bagging: random sampling training sets with replacement.
  - Random feature selection.

## 3. Gradient Boosting Decision Trees

- Train multiple decision trees sequentially:
  - $F_t(x)$ is the sum of all previous trees.
  - Train a new tree $f_t(x)$ on the residual: $\{x_i, y_i - F_{t-1}(x_i)\}$.
  - $F_{t+1} = F_t + f_t$.

## Related Notes

- [Ensemble Learning](../Ensemble/Ensemble-Learning.md)
- [Bagging and Pasting](../Ensemble/Bagging-and-Pasting.md)
- [Gradient Boosting](../Ensemble/Gradient-Boosting.md)
