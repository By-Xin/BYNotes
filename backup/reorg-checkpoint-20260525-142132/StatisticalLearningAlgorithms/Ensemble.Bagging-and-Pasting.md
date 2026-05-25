---
title: "Bagging and Pasting"
aliases:
  - "Bagging_and_Pasting"
  - "Bagging and Pasting"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/ensemble-learning
  - topic/bagging
---

## 1. Idea

- Bagging and pasting are two ensemble methods that build multiple instances of a model and combine them to get a more accurate and stable prediction.
- We train multiple models using the same algorithm, but with different samples of the training data.
- During sampling to create a dataset, we can either:
  - sample with replacement, i.e. bagging;
  - sample without replacement, i.e. pasting.

> [!note] Note: Bagging vs pasting
> Both bagging and pasting allow training instances to be sampled several times across multiple models, but only bagging allows training instances to be sampled several times for the same model.

## 2. Out-of-Bag Evaluation

In bagging, some instances may be sampled several times for some models, while others may not be sampled at all. The instances that are not sampled for a particular model are called out-of-bag instances. These instances can be used to evaluate the model without the need for a separate validation set.

## Related Notes

- [Ensemble Learning](./Ensemble.Ensemble-Learning.md)
- [Boosting](./Ensemble.Boosting.md)
