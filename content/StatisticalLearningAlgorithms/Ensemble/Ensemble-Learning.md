---
title: "Ensemble Learning"
aliases:
  - "Ensemble_Learning"
  - "Ensemble Learning"
  - "集成学习"
  - "StatisticalLearningAlgorithms/Ensemble.Ensemble-Learning"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/ensemble-learning
---

## 1. Core Idea

- In ensemble learning, multiple models are trained and combined to improve the performance of the model.
- Weak and strong learners:
  - **Weak learner.** A model that performs slightly better than random guessing.
  - **Strong learner.** A model that performs well on a given task.
- Ensemble learning performs better when models are diverse and independent.

## 2. Voting

- **Hard voting.** The class with the most votes is predicted.
- **Soft voting.** The class with the highest average probability is predicted.

## 3. Popular Ensemble Algorithms

- [Bagging and Pasting](./Bagging-and-Pasting.md)
- [Boosting](./Boosting.md)
- Stacking
- Random Forest
- [Gradient Boosting](./Gradient-Boosting.md)

## Related Notes

- [Bagging and Pasting](./Bagging-and-Pasting.md)
- [Boosting](./Boosting.md)
- [AdaBoost](./AdaBoost.md)
- [Gradient Boosting](./Gradient-Boosting.md)
