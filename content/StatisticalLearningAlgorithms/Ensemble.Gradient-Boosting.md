---
title: "Gradient Boosting"
aliases:
  - "Gradient_Boosting"
  - "Gradient Boosting"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/ensemble-learning
  - topic/boosting
---

## 1. Idea

Similar to [AdaBoost](./Ensemble.AdaBoost.md), **Gradient Boosting** is an ensemble learning method that adds models to the ensemble so that the new model corrects the errors of its predecessor.

The difference is that AdaBoost increases the weights of the misclassified instances, while Gradient Boosting fits the new model to the residual errors made by the previous model.

## 2. Implementations

Popular implementations of Gradient Boosting include:

- GBDT, i.e. Gradient Boosting Decision Trees.
- XGBoost.

## Related Notes

- [Boosting](./Ensemble.Boosting.md)
- [Tree-Based Models](./Nonparametric.Tree-Based-Models.md)
