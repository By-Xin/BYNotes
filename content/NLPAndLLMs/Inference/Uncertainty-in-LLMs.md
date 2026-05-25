---
title: "Uncertainty in LLMs"
aliases:
  - "Uncertainty in LLMs 综述"
  - "LLM不确定性"
  - "Confidence Estimation"
  - "LLM置信度"
  - "Semantic Entropy"
  - "NLPAndLLMs/Inference.Uncertainty-in-LLMs"
course: "NLP and Large Language Models"
type: "topic-note"
status: "draft"
tags:
  - course/nlp-and-llms
  - topic/llm-inference
  - topic/uncertainty
---

> [!quote] References
> - Paper: Semantic Uncertainty, ICLR 2023.
> - Paper: Detecting Hallucinations in Large Language Models Using Semantic Entropy, Nature 2024.
> - Paper: Scalable Best-of-N Selection for Large Language Models via Self-Certainty.

## 1. Measuring Confidence of LLMs

首先给出背景介绍, 以及一些典型的任务衡量方法. 本小节介绍逻辑及记号主要参考 *Scalable Best-of-N Selection for Large Language Models via Self-Certainty*.

## 2. LLM Background

通常考虑一个自回归形式的语言模型 (Language Model, LM) $p(\cdot \mid x)$, 其中 $x = (x_1, x_2, ..., x_n)$ 是输入序列, 每一个 $x_i\in \mathcal{V}$ 是词汇表 $\mathcal{V}$ 中的一个 token.

语言模型的本质是建模这个 sequence 的联合分布:

$$
L_x = (\ell_1, \ell_2, ..., \ell_n) , \quad \ell_i \in \mathbb{R}^{|\mathcal{V}|}.
$$

其中 $\ell_i$ 是 $x_i$ 的 logits 向量, 其长度等于词汇表大小 $|\mathcal{V}|$, 相当于每个 token 在词汇表中的概率分布.

在得到 $y = (y_1, \cdots, y_m)$ 的输出后, 预测下一个 token 的概率分布为:

$$
p(y_{m+1} \mid x, y_{1}, \cdots, y_m).
$$

这反映了模型基于输入 $x$ 和已生成输出 $y$ 对下一个 token 的预测, or belief.

## 3. Confidence Estimation

这里的 confidence 稍微有别于统计学中频率学派的置信度, 更接近于衡量模型的主观 certainty. 但是某种程度上其也和模型的分布, 以及分布的集中与离散程度有关.

### 3.1 Sentence-Level Probabilistic Confidence

第一类方法是直接使用模型实际生成序列中已采样的 token 来衡量模型在生成该序列时的 confidence.

#### 3.1.1 Average Log-Probability

$$
\text{AvgLogP}:= \frac{1}{n} \sum_{i=1}^{n} \log p(y_i \mid x, y_{\lt i}).
$$

- 该方法直接计算生成每个 token 时的条件概率, 即每一步 softmax probability, 的对数平均值.
- 相当于当前序列对数似然的平均值.
- 该方法简单直接, AvgLogP 越大, 说明模型对生成序列越有信心.

#### 3.1.2 Perplexity

$$
\text{Perplexity}:= \exp\left(-\frac{1}{n} \sum_{i=1}^{n} \log p(y_i \mid x, y_{\lt i})\right).
$$

- 该方法是对 average log-probability 的指数化处理, 二者某种程度上等价.
- Perplexity 越小, 说明模型对生成序列越有信心.

### 3.2 Distributional Confidence

上述两种方法局限于生成序列本身. 但更科学的做法是充分考虑生成时每一个时间步的完整概率分布, 以刻画模型是否更集中地相信某些 token.

Distributional confidence 可以总结为如下范式:

- 设 $P_{y\mid x} = (p(\cdot \mid x), p(\cdot \mid x, y_1), \cdots, p(\cdot \mid x, y_{n-1}))$ 是模型在每个时间步的概率分布.
- $f(\cdot)$ 是一个局部函数, 作用于每个时间步的概率分布 $C:=f(p(\cdot \mid x, y_{\lt i}))$.
- $F(\cdot)$ 是一个汇总函数, 如取平均值, 将局部函数结果汇总为全局 confidence 值.

Thus:

$$
\text{Distributional Confidence} := F\left(f(P_{y\mid x})\right).
$$

以均值汇总为例:

$$
F(C) = \frac{1}{n} \sum_{i=1}^{n} C_i = \frac{1}{n} \sum_{i=1}^{n} f(p(y_i \mid x, y_{\lt i})).
$$

根据 $f(\cdot)$ 不同, 可以得到不同的 distributional confidence 方法. 不过整理可见, 其本质上都是 $\sum^{V}_{j=1} p(j \mid x, y_{\lt i})$ 的某种函数.

#### 3.2.1 KL Divergence

$$
C_i^{\text{KL}} =
\text{KL}(U \| p(\cdot \mid x, y_{\lt i}))
= \sum_{j=1}^{V} \frac{1}{V} \log\left( \frac{1/V}{p(j \mid x, y_{\lt i})} \right)
= -\frac{1}{V} \sum_{j=1}^{V} \log\left( V \cdot p(j \mid x, y_{\lt i}) \right).
$$

- 衡量当前分布与 uniform distribution 的差异.
- 差异越大, 分布越集中, 置信度越高.
- Self-Certainty 就是用 KL divergence 构建的度量.

#### 3.2.2 Gini Impurity

$$
C_i^{\text{Gini}} = \sum_{j=1}^{V} p(j \mid x, y_{\lt i})^2.
$$

- 表示两次随机采样取到不同 token 的概率.
- 越集中, Gini 值越高, 置信度越高.

#### 3.2.3 Entropy

$$
C_i^{\text{Entropy}} = \sum_{j=1}^{V} p(j \mid x, y_{\lt i}) \log p(j \mid x, y_{\lt i}).
$$

- 熵越高, 分布越发散, 越不确定.
- 所以作者用负熵来表示置信度.

#### 3.2.4 Distributional Perplexity

$$
C_i^{\text{DP}} = -\exp\left( -\sum_{j=1}^{V} p(j \mid x, y_{\lt i}) \log p(j \mid x, y_{\lt i}) \right).
$$

- 实际上是将熵指数化后的反向量.
- 越小表示模型更 confident.
- 本质上与负熵类似, 只是数值缩放不同.

## 4. Related Work

下面是一些与模型 confidence 相关的工作.

## 5. Meta-Cognitive Methods: P(True) and P(IK)

Anthropic 提出的两个关于模型在生成回答时自我反思来衡量 confidence 的方法. 核心思想是让模型自己判断其回答的正确性, 以此衡量模型 certainty. 某种意义上这反映了模型自我的元认知能力.

Reference: [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221).

### 5.1 P(True)

#### 5.1.1 Methodology

P(True) 表示模型对其生成的某个答案是否在事实层面上正确所给出的概率估计. 它是关于外部世界事实的判断. 与传统 QA 任务的区别在于, 模型不只是给出答案, 还要对自己生成的答案是否正确做出评估.

Formally:

$$
P(\text{True}) = \mathbb{P}[\text{answer } a \text{ is correct} \mid q, a].
$$

Evaluation workflow:

1. 给定问题 $q$.
2. 采样得到模型答案 $a\sim p(\cdot \mid q)$, 常用 $T=1$ 的采样.
3. 用以下 prompt 让模型判断答案正确性:

```text
Question: {q}
Answer: {a}
Is the proposed answer:
(A) True
(B) False
```

4. 从中提取模型对答案正确性的概率 $P(\text{True})$.

P(True) 的局限:

- 模型难以区分生成来自自己还是来自他人的文本, 会在自我样本上过于自信.
- 任务分布外泛化有限, 仅在见过的任务上表现良好.
- 无监督训练的模型可能只是学会了答案听起来像真的, 而非真的理解语义正确性.
- 不适用于无 ground truth 或多解空间任务.

#### 5.1.2 Experiments

**Evaluation tasks.**

| Dataset | Type | Description |
|---------|------|-------------|
| TriviaQA | Fact QA | Closed-book knowledge retrieval |
| Lambada | Language modeling fill-in | Long-context continuation |
| Codex HumanEval | Code generation | Implement Python functions |
| GSM8k | Math problems | Chain-of-thought reasoning tasks |
| Arithmetic | Basic calculation | Simple integer arithmetic |

所有任务都使用 $T=1$ 采样多个样本, 对其中每一个样本进行自我评估.

**Few-shot vs zero-shot.**

- 在 zero-shot 下, 模型的 $P(\text{True})$ 校准性较差, 预测值集中在中间, 如 0.4 到 0.6.
- Few-shot 提示显著提升校准性和区分度.
- 提供多个候选答案, 如 5 个 $T=1$ 样本, 再要求判断某个答案的真实性, 可进一步提升效果.

**Metrics.**

- Accuracy conditioned on $P(\text{True})>0.5$: 验证那些模型自以为正确的答案的实际正确率.
- Brier Score: $\text{Brier} = \frac{1}{N} \sum_{i=1}^N (P_i - y_i)^2$, where $y_i$ is the actual label and $P_i$ is the predicted probability.
- AUROC: 衡量模型能否把正确和错误样本有效区分开, 但不考虑概率是否校准.
- Calibration Curve and Expected Calibration Error (ECE): 衡量模型输出概率的统计一致性.

### 5.2 P(IK)

P(IK) is $P(\text{I-Know})$, 表示模型认为它是否知道某个问题答案的概率. 与 P(True) 不同, P(IK) 是一个类似前验的考虑, 是在模型生成答案之前就对问题知识状态进行评估.

#### 5.2.1 Methodology

首先定义模型对于 I-Know 的 ground truth:

$$
\text{Ground-truth } P(\text{IK}) =
\mathbb{1}\left[\frac{1}{N} \sum_{i=1}^N \mathbb{1}[a_i \text{ correct}] > 0.5\right].
$$

即对于某个问题, 令模型进行多次采样输出. 如果输出答案经过评价判断发现有超过一半正确, 则认为模型对该问题是 I-Know 的.

得到 ground truth 后, 可以通过有监督方法训练一个语言模型预测 P(I-Know). 具体而言, 在原有语言模型结构上添加一个分类问题的 value head, 该线性层输出一个标量, 用来预测模型对于当前输出的 I-Know 概率.

此外, 这个结构设计相对独立于文本输出, 不改变任何输出策略, 只对模型输出进行一个 I-Know 概率预测.

## 6. Semantic Entropy

Semantic Entropy 是一种基于语义的熵度量方法, 旨在衡量 LLM 在生成自然语言文本时的语义不确定性. 核心思想是将 token 级别的概率分布转化为语义级别的概率分布, 通过对语义类进行聚类和熵计算来评估模型信心.

Reference: [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://arxiv.org/abs/2302.09664).

该文章重点侧重于 Semantic Entropy 在 QA 任务中的表现.

### 6.1 Methodology: Semantic Entropy

核心思想: 将 token 级别的单位判断转化为 semantic class. 例如对于问题 `What is the capital of France?`, 可以定义一个语义等价类 `c = {'Paris', 'The capital of France is Paris', "France's capital is Paris", ...}`. 尽管其 token 层面的表达方式各不相同, 但只要 LM 回答结果落入这个语义类中, 我们就认为是正确答案.

#### 6.1.1 Mathematical Model

记模型输入, 如 QA 问题, 为 $x$. LLM 在 $M$ 次采样后得到输出样本 $s_1, s_2, ..., s_M$. 此外假设可以判断每次输出属于某个语义类 $s_i \in c \in \mathcal{C}$, 其中 $\mathcal{C}$ 是所有语义类集合.

则模型生成某个语义类 $c$ 的总概率可用生成样本中落入该语义类的频率估计:

$$
p(c \mid x) = \frac{1}{M} \sum_{i=1}^{M} \mathbb{I}(s_i \in c).
$$

Semantic Entropy is:

$$
\text{SE}(x) = -\sum_{c \in \mathcal{C}} p(c|x) \log p(c|x).
$$

- 如果模型所有回答都落入同一个语义类, 语义熵为 $0$, 表示模型非常确定.
- 如果模型回答分布在多个语义类中, 语义熵较高, 表示模型不确定.

#### 6.1.2 Implementation Steps

**1. Sampling generation.**

- Goal: use language model $p(y \mid x)$ to generate $M$ samples $s_1, s_2, ..., s_M$ and approximate output distribution.
- Method:
  - Use temperature sampling.
  - Do not use top-k or top-p truncation, to preserve maximum entropy estimation precision.

**2. Semantic clustering.**

- Goal: cluster different output samples into semantic equivalence classes.
- Core idea: two sentences are in the same semantic class iff they satisfy bidirectional entailment:

$$
\text{Entail}(s_i, s_j) \land \text{Entail}(s_j, s_i) = \text{True}.
$$

- Method: use DeBERTa-Large fine-tuned on MNLI as an entailment classifier.
- Clustering method: agglomerative clustering.
  - Initially each sample is its own cluster.
  - Judge all sentence pairs for bidirectional entailment.
  - If two sentences satisfy bidirectional entailment, merge them into one cluster.
  - Repeat until convergence.
- Finally obtain disjoint semantic classes $\mathcal{C} = \{c_1, c_2, ..., c_K\}$. In QA tasks, the number of semantic classes is usually 2-5.
- Time complexity is $\mathcal{O}(M^2)$.

> [!note] Note: NLI, MNLI, and DeBERTa
> **Natural Language Inference (NLI).** NLI takes two sentences A and B and asks whether their relation is entailment, contradiction, or neutral.
>
> **MNLI.** MNLI is a large-scale NLI dataset in GLUE. Each sample is a `(premise, hypothesis)` pair with a relation label. The training set has about 400k examples.
>
> **DeBERTa-Large.** DeBERTa-Large is a Microsoft Transformer model, usually with 24 layers and about 304M parameters. Fine-tuning on MNLI makes it effective for entailment judgments.

**3. Entropy estimation.**

- Goal: calculate each semantic class probability $p(c|x)$ and semantic entropy:

$$
\text{SE}(x) = -\sum_{c \in \mathcal{C}} p(c|x) \log p(c|x).
$$

- Method:
  - For each semantic class $c$:

$$
p(c|x) = \frac{1}{M} \sum_{i=1}^{M} \mathbb{I}(s_i \in c).
$$

  - Substitute into the semantic entropy formula.

### 6.2 Experiments

#### 6.2.1 Experimental Design

- Goal: Can semantic entropy more effectively measure LLM semantic uncertainty? When the model is uncertain, are its answers more semantically diverse?
- Design:
  - Use QA tasks as test platform with explicit correct answers.
  - Compare semantic entropy with traditional token-level entropy, scorers, output similarity, and other methods.
  - Metric: whether it can identify wrong generated answers, i.e. whether high uncertainty implies wrong answers.

#### 6.2.2 Datasets, Models, and Metrics

Datasets:

- TriviaQA: closed-form QA task with standard answers. Uses exact match and string overlap rules to judge correctness.
- CoQA: open-form QA task with multiple reference answers. Authors use MNLI-DeBERTa to judge whether a generated answer is semantically equivalent to any reference answer.

Models:

- GPT-J (6B), GPT-NeoX (20B, 30B).
- Temperature $0.5$, no top-k or top-p truncation.
- Sample 10 times.

Metric:

$$
\text{AUROC} = \mathbb{P}\left\{u(x_{\text{wrong}}) > u(x_{\text{correct}})\right\}.
$$

Here $u(x)$ is the model's uncertainty estimate, such as entropy.

> [!note] Note: Critical concern
> CoQA correctness labels are judged by DeBERTa-MNLI; Semantic Entropy also relies on this NLI model for clustering. Thus AUROC may be inflated and may not fully generalize. SE can predict "what is correct" partly because correctness itself is decided by its downstream model. Other baselines such as token entropy, p(True), and Rouge-L do not depend on DeBERTa, so their results are more purely data-driven. This suggests possible information leakage or a model-collusion structure.

#### 6.2.3 Baselines

Core metric: AUROC.

- Normalised Entropy: calculate token probability entropy and normalize it to $[0,1]$:

$$
\hat H(\mathbf{p}) = - \sum_{i=1}^{K} p_i \log p_i / \log K.
$$

- p(True) Classifier: use a specially trained LLM to judge whether the answer is correct.
- Lexical Similarity (Average Rouge-L): calculate the score of the candidate answer most similar to other answers, reflecting lexical overlap.

#### 6.2.4 Experimental Workflow

1. Take a batch of questions $x$ from TriviaQA or CoQA.
2. For each question, use LLM to generate $M$ answer samples $s_1, s_2, ..., s_M$.
3. For each input-output pair $(x, s_i)$, calculate semantic entropy $\text{SE}(x)$ or other baseline score.
4. Simultaneously calculate whether each input-output is correct, using TriviaQA exact match or CoQA bidirectional entailment judgment.
5. Calculate AUROC and compare different methods.

#### 6.2.5 Results

![Semantic entropy experiment results](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/20250604220523.png)

## 7. Detecting Hallucinations with Semantic Entropy

Follow-up work:

- [Detecting hallucinations in large language models using semantic entropy](https://www.nature.com/articles/s41586-024-07421-0), Nature, Vol. 630, June 2024.

### 7.1 Motivation

LLMs 在生成文本时会出现 hallucination 现象, 即生成内容与事实不符或虚构信息. 其中一种常见幻觉为 **confabulatory hallucination**. 文中定义为: 对同样 prompt 输入, 模型在不同采样种子下输出语义不一致且往往错误的回答.

例如, 反复提问 `Where is the Eiffel Tower?` 时, 模型可能生成不同回答, 如 `Paris`, `It's Paris`, `It's Rome`, `Berlin`, 等等. 其中可能存在正确答案, 也可能没有. Confabulation 强调的是模型回答的不一致性和随机性.

在生成时, 针对同一个输入可能会生成多个不同甚至互斥的回答, 而模型内部并没有明确指定哪一个回答是正确的. 这说明模型是 semantic uncertain 的, 即对同一输入的不同输出在语义上存在不一致. 因此作者希望通过 semantic entropy 来检测这种幻觉现象.

![Confabulatory hallucination and naive/semantic entropy](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/20250604213204.png)

### 7.2 Methodology

文章方法与前文 Semantic Entropy 类似:

1. **Sampling Generation**: For each input $x$, use LLM to generate $M$ samples $\{s_1, s_2, ..., s_M\}$.
2. **Semantic Clustering**: Use an NLI classifier. If two samples $s_i, s_j$ satisfy $\text{Entail}(s_i, s_j) \land \text{Entail}(s_j, s_i) = \text{True}$, cluster them into the same semantic class $c_k$. This obtains disjoint semantic classes $\mathcal{C} = \{c_1, c_2, ..., c_K\}$.
   - The classifier can be an NLI fine-tuned model, such as DeBERTa-Large-MNLI, or an advanced general LLM such as GPT-3.5.
3. **Entropy Estimation**: Estimate $\mathbb{P}(c_k|x) \approx \frac{1}{M} \sum_{i=1}^{M} \mathbb{I}(s_i \in c_k)$, then calculate:

$$
\text{SE}(x) = -\sum_{i=1}^{K} \mathbb{P}(c_k|x) \log \mathbb{P}(c_k|x).
$$

If semantic entropy is high, the probability distribution is scattered, meaning the model has high uncertainty for the input and may have confabulatory hallucination.

### 7.3 Experiments

#### 7.3.1 Datasets

The paper designs experiments to cover two types of tasks:

1. QA tasks:
   - SQuAD v1.1: closed-form QA from Wikipedia.
   - TriviaQA: open-domain QA based on multi-document reasoning.
   - NQ-Open: open QA from Google search logs.
   - BioASQ: biomedical QA, including information retrieval and extraction.
   - SVAMP: elementary school math word problems.
2. Long-form generation tasks:
   - FactualBio: input real person names and use LLMs to generate biographies. Each sentence is manually labeled as true, false, or unverifiable.

![BioASQ task illustration](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/20250604215943.png)

#### 7.3.2 Base Models and Sampling Strategies

| Model | Type | Parameters | Source |
|-------|------|------------|--------|
| LLaMA-2 Chat | Open | 7B, 13B, 70B | Meta |
| Falcon Instruct | Open | 7B, 40B | TII |
| Mistral Instruct | Open | 7B | Mistral |
| GPT-4 | Closed | undisclosed | OpenAI API |

Sampling strategies:

- Top-p: $p=0.9, T=1$.
- Top-k: $k=50, T=1$.
- Temperature: $T=0.1$ as best generation of the model to the context.

#### 7.3.3 Baselines

- Token Entropy: calculate token probability entropy.
- P(True): use classifier to predict the probability that an answer is true.
- Embedding Regression: use semantic embeddings to train a regression model that predicts answer correctness.
- MC Dropout: approximate uncertainty with dropout, using multiple forward passes to calculate entropy.

#### 7.3.4 Metrics and Results

- AUROC: in binary classification, measures how well the model separates correct and wrong answers. Perfect separation gives $\text{AUROC} = 1$, random guessing gives $\text{AUROC} = 0.5$.
- AURAC: used for selective answering. Given a rejection threshold $\tau$, reject answers with overly high entropy. AURAC measures remaining accuracy across thresholds.

![Semantic entropy outperforms leading baselines and naive entropy](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/20250604220010.png)

## 8. Distributional Self-Certainty

Reference: [Scalable Best-of-N Selection for Large Language Models via Self-Certainty](https://arxiv.org/abs/2502.18581).

### 8.1 Motivation

- In reasoning tasks, best-of-N sampling is a common method for improving LLM output accuracy.
- Mainstream methods use reward models, such as ORMs and PRMs, to score and select candidates. However:
  - Training cost is high.
  - They are sensitive to training distribution shifts.
  - They can be exploited by reward hacking.
  - They do not generalize well to open-ended generation tasks.

> [!note] Note: Sampling vs search
> 注意区分这里的 sampling 策略和 beam search, top-p 等搜索方法. 前者属于 output-level reranking/selection, 是对 decoding 之后的样本进行挑选, 是一种后处理技术. 后者是 token-level sequence generation 中的选择策略.

作者提出一种基于分布的 self-certainty 计算框架.

### 8.2 Methodology

#### 8.2.1 Self-Certainty

模型每一步 token 输出都参照一个分布 $p_i = p(\cdot | x, y_{\lt i})$ 进行. 作者通过这种输出分布构建模型输出 certainty 的衡量框架:

$$
\text{Self-Certainty} = F\left(f_1(p_1), f_2(p_2), ..., f_n(p_n)\right).
$$

- $f_i(p_i)$ is the distributional confidence score at step $i$, such as KL or entropy.
- $F$ is an aggregation function, such as mean.

Concretely:

$$
\text{Self-certainty} = -\frac{1}{nV} \sum_{i=1}^{n} \sum_{j=1}^{V} \log \left( V \cdot p(j \mid x, y_{\lt i}) \right).
$$

Or:

$$
\text{Self-certainty (CE)} = -\frac{1}{nV} \sum_{i=1}^{n} \sum_{j=1}^{V} \log p(j \mid x, y_{\lt i}).
$$

在每个时间步 $i$ 上, 遍历所有可能 token $j$, 即词汇表 $\mathcal{V}$ 中每个 token, 计算其概率分布 $p(j \mid x, y_{\lt i})$ 的对数并求平均.

![Negative perplexity and self-certainty differ on reasoning tasks](https://raw.githubusercontent.com/By-Xin/Blog-figs/main/20250611144724.png)

上图是一个 QA 数学推理问题的例子. LLM 一共生成两个样本: 第一次第一步就出错, 没有得到正确答案; 第二次正确进行了推理求解.

- 如果采用 negative perplexity:

$$
\text{PPL} = \exp\left(-\frac{1}{n} \sum_{i=1}^n \log p(y_i | x, y_{\lt i})\right),
$$

其本质是这个句子采样出的似然值. 它只对模型实际采样出来的 token 的概率做平均. 如果前面出错, 但后面每一步都采样到了高概率 token, 总体分数仍可能很高. 从结果来看, negative perplexity 没能很好地区分两次 sampling 结果.

- 如果采用 self-certainty:

$$
\text{Self-Certainty} = -\frac{1}{nV} \sum_{i=1}^n \sum_{j=1}^V \log(V \cdot p(j | x, y_{\lt i})),
$$

则可以很好地区分两次结果. 这是因为如果某一步模型分布很发散, 即不 confident, 即使采样到了高概率 token, 也会被惩罚. 且由于语言模型自回归特性, 一旦前面生成出错 token, 后续输出往往也变得相对更不 confident.

#### 8.2.2 Self-Certainty with Borda Voting

尽管 self-certainty 比常规平均 log probability 或 perplexity 更能区分对错, 但它本身仍存在被局部高置信样本欺骗的风险. 传统 majority voting 又不考虑生成样本间置信度差异, 因此容易受到频率失衡或等票问题影响. 因此这里提出 **Self-Certainty + Borda Voting**.

Workflow:

1. **Self-Certainty calculation and ranking.** 对同一个输入 $x$, 使用 LLM 生成 $N$ 个平行候选输出 $y_1, y_2, \ldots, y_N$, 并计算每个候选输出的 self-certainty 值 $C(y_i)$. 根据该值对候选输出排序, 对应于 $y_i$ 记为 $r_i$. 其中 $r_i \in \{1,2,\ldots,N\}$, $r_i=1$ 表示 self-certainty 最大的候选输出.
2. **Vote weight calculation.** 对于每个候选输出 $y_i$ 与对应排序 $r_i$, 计算投票权重:

$$
v(r_i) = (N - r_i + 1)^p.
$$

其中 $p$ 是超参数, 控制投票权重衰减程度. 当 $p=0$ 时, 所有候选输出投票权重相同, 相当于 majority voting; 当 $p\to\infty$ 时, 只有 self-certainty 最大的候选输出有权重.

3. **Borda Voting.** 将所有输出根据 final answer 分组, 同一个答案的所有候选输出投票权重相加:

$$
V(y) = \sum_{i: y_i \in \mathcal{Y}} v(r_i).
$$

4. **Select best answer.**

$$
y^* = \arg\max_{y \in \mathcal{Y}} V(y).
$$

## Related Notes

- [Deep Reasoning for LLMs](./Deep-Reasoning-for-LLMs.md)
- [Context Engineering](./Context-Engineering.md)
- [Probability Theory](../../ProbabilityTheory/)
- [Statistical Inference](../../StatisticalInference/)
