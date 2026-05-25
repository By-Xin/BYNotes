---
title: "NLP and Large Language Models"
aliases:
  - "NLP and LLM"
  - "cs.CL NLP LLM"
  - "cs.CL_NLP_LLM"
  - "Computation and Language"
  - "自然语言处理与大语言模型"
type: "course-index"
status: "active"
tags:
  - course/nlp-and-llms
---

Natural language processing and large language model notes covering static embeddings, language models, BERT, LLM training, reasoning, uncertainty, and context engineering.

## Start Here

For a structured pass through NLP and LLMs, read the modules in this order:

1. [Embeddings](./Embeddings/)
2. [Language Models and Pretrained Models](./Models/)
3. [LLM Training and Alignment](./Training/)
4. [LLM Inference and Analysis](./Inference/)

## Module Map

| Module                                             | Scope                                                     |
| -------------------------------------------------- | --------------------------------------------------------- |
| [Embeddings](./Embeddings/)                        | Word vectors, Word2Vec, negative sampling, and GloVe      |
| [Language Models and Pretrained Models](./Models/) | N-gram models, BERT, and pretrained Transformer encoders  |
| [LLM Training and Alignment](./Training/)          | Pretraining, alignment, post-training, and forgetting     |
| [LLM Inference and Analysis](./Inference/)         | Reasoning, uncertainty, context engineering, and analysis |

## Notes

### [Embeddings](./Embeddings/)

| Area             | Note                                                   | Status |
| ---------------- | ------------------------------------------------------ | ------ |
| Overview         | [Word Embeddings](./Embeddings/Word-Embeddings.md)     | draft  |
| Static embedding | [Word2Vec](./Embeddings/Word2Vec.md)                   | draft  |
| Optimization     | [Negative Sampling](./Embeddings/Negative-Sampling.md) | draft  |
| Static embedding | [GloVe](./Embeddings/GloVe.md)                         | draft  |

### [Language Models and Pretrained Models](./Models/)

| Area              | Note                                                         | Status |
| ----------------- | ------------------------------------------------------------ | ------ |
| Language modeling | [N-Gram Language Models](./Models/N-Gram-Language-Models.md) | draft  |
| Pretrained model  | [BERT](./Models/BERT.md)                                     | draft  |

### [LLM Training and Alignment](./Training/)

| Area          | Note                                                                                   | Status |
| ------------- | -------------------------------------------------------------------------------------- | ------ |
| Alignment     | [Pretraining and Alignment for LLMs](./Training/Pretraining-and-Alignment-for-LLMs.md) | draft  |
| Post-training | [Post-Training and Forgetting](./Training/Post-Training-and-Forgetting.md)             | draft  |

### [LLM Inference and Analysis](./Inference/)

| Area        | Note                                                              | Status |
| ----------- | ----------------------------------------------------------------- | ------ |
| Reasoning   | [Deep Reasoning for LLMs](./Inference/Deep-Reasoning-for-LLMs.md) | draft  |
| Uncertainty | [Uncertainty in LLMs](./Inference/Uncertainty-in-LLMs.md)         | draft  |
| Context     | [Context Engineering](./Inference/Context-Engineering.md)         | draft  |

## Concept Map

- Embeddings: one-hot encoding, dense word vectors, Word2Vec, negative sampling, GloVe, and contextual embeddings.
- Language models: N-gram models, Markov assumptions, sparsity, and pretrained Transformer encoders.
- LLM training: pretraining, SFT, RLHF, alignment, knowledge distillation, post-training, and catastrophic forgetting.
- LLM inference: chain of thought, test-time compute, reasoning workflows, uncertainty estimation, semantic entropy, and context engineering.

## Related Topics

- [(Dive-into) Deep Learning](../DeepLearning)
- [Statistical Learning Algorithms](../StatisticalLearningAlgorithms)
- [Probability Theory](../ProbabilityTheory)
- [Statistical Inference](../StatisticalInference)

## Planned Notes

- LLM Sampling Methods
- Latent Space LLM Survey 2024
- Mitigating LLM Hallucinations via Conformal Abstention
- Information Theory for NLP
- Transformer and Attention
