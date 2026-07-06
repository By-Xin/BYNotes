# Content audit 2026-07-06 — open items

Produced by the opus/sonnet review fleet + Fable adjudication. 147 verified
corrections and 75 cross-links were applied in the accompanying commits.
The items below were NOT applied (reviewer confidence was not certain, or the
proposed fix was not a drop-in replacement) and await owner judgment.

## Unapplied findings

- **ConvexOptimization/5.Gradient-Descent.md** [notation/medium/likely]
  - quote: `对于固定步长 $t\leq 1/L$, GD 方法有:`
  - issue: L is never defined in this note; the smoothness constant used throughout is M (m I <= Hessian <= M I, M-Smooth). This is an unexplained symbol switch (L should be M).
  - proposed: 对于固定步长 $t\leq 1/M$, GD 方法有:

- **ConvexOptimization/6.Subgradient.md** [notation/medium/likely]
  - quote: `上一个例子还可以进一步推广到 $n$ 个函数的最大值. 定义 $f(x) = \max_{i=1...n} f_i(x)$, 其中每个 $f_i: \mathbb{R}^n \to \mathbb{R}$`
  - issue: The symbol n is used for two different things at once: the number of functions in the max (i = 1...n) and the domain dimension (f_i: R^n -> R). This collides within one statement.
  - proposed: 上一个例子还可以进一步推广到 $m$ 个函数的最大值. 定义 $f(x) = \max_{i=1...m} f_i(x)$, 其中每个 $f_i: \mathbb{R}^n \to \mathbb{R}$

- **ConvexOptimization/6.Subgradient.md** [notation/low/likely]
  - quote: `定义 $f$ 在点 $x$ 关于方向 $d$ 的方向导数为:`
  - issue: The directional derivative is written $\partial f(x; d)$ (in the sentence just above and in the display), overloading the symbol $\partial$ which everywhere else in this note denotes the subdifferential $\partial f(x)$. Standard notation for the directional derivative is $f'(x; d)$.
  - proposed: 定义 $f$ 在点 $x$ 关于方向 $d$ 的方向导数 $f'(x; d)$ 为:

- **ConvexOptimization/9.Stochastic-Gradient-Descent.md** [notation/low/likely]
  - quote: `存在常数 $M > 0$ 使得 $\mathbb{E}[\|g_{i_k}(x_k)\|^2] \leq M^2<\infty$`
  - issue: 符号 M 在本篇内被复用为两个不同对象: 此处是随机次梯度二阶矩的上界常数 M(§3.1 收敛性分析全程沿用, 出现在所有 M^2 项与最优步长 R/(M√k) 中); 而在 §2.2 的 RMSProp/AdaDelta/Adam 中 M_k 又被用作梯度平方的指数移动平均累积量(如 M_{k+1}=ρM_k+(1-ρ)(g_k⊙g_k)). 同一符号在一篇笔记里指代两个无关的量, 易混淆.
  - proposed: 为二者之一改名以消歧, 例如将二阶矩上界常数改记为 G(如 E[‖g‖^2]≤G^2), 或将自适应算法中的累积量改记为 v_k / r_k, 使 M 在本篇只指代一个对象.

- **ConvexOptimization/8.Proximal-Gradient-Descent.md** [fact/low/unsure]
  - quote: `Beck 和 Teboulle 在 2008 年给出了 Nesterov 1983 算法的 Proximal Gradient 版本, 被称为 **FISTA**`
  - issue: FISTA 的正式发表年份通常记为 2009 年(Beck & Teboulle, "A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems", SIAM J. Imaging Sciences, 2(1), 2009). 此处写作 2008 年的年份存疑(该说法沿用了所引 CMU 讲义, 但按发表年应为 2009).
  - proposed: Beck 和 Teboulle 在 2009 年给出了 Nesterov 1983 算法的 Proximal Gradient 版本, 被称为 **FISTA**

- **ConvexOptimization/12.Optimality-Conditions-for-Constrained-Optimization.md** [typo/low/likely]
  - quote: `LCQ 和 LICQ 直接一般没有必然关联.`
  - issue: '直接' is misplaced and makes the sentence ungrammatical; the intended word is '之间' (between LCQ and LICQ there is generally no necessary relation).
  - proposed: LCQ 和 LICQ 之间一般没有必然关联.

- **ConvexOptimization/12.Optimality-Conditions-for-Constrained-Optimization.md** [notation/low/likely]
  - quote: `&& A\mathbf{x}^* = \mathbf{b} \quad \forall j\in \mathcal{E} \\`
  - issue: The primal-feasibility line writes the single vector equation A\mathbf{x}^* = \mathbf{b} but appends '\forall j\in\mathcal{E}', a stray index quantifier left over from the componentwise c_j(\mathbf{x}^*)=0 form; A\mathbf{x}=\mathbf{b} is not indexed by j here.
  - proposed: && A\mathbf{x}^* = \mathbf{b} \\

- **ConvexOptimization/13.Duality-Uses-and-Correspondents.md** [notation/medium/likely]
  - quote: `\max_\mu -f^*(A^\top \mu) - I^*_K(-\mu)`
  - issue: The primal problem here is \min_x f(x) s.t. x\in K, which contains no matrix A. A appears from nowhere (it should be the identity, i.e. z=x). The dual should use f^*(\mu), not f^*(A^\top\mu).
  - proposed: \max_\mu -f^*(\mu) - I^*_K(-\mu)

- **ConvexOptimization/13.Duality-Uses-and-Correspondents.md** [logic/low/unsure]
  - quote: `\sup_{\boldsymbol{\mu}}\left[-\mathbf{y}^\top \boldsymbol{\mu} - \frac{1}{2} \|\boldsymbol{\mu}\|_2^2 - \frac{`
  - issue: This substitutes -f^*(\mu). Even granting the note's own (incorrect) f^*(\mu)=y^\top\mu+1/2\|\mu\|^2-1/2\|y\|^2, then -f^* would give +1/2\|y\|^2, but the line shows -1/2\|y\|^2 — a sign inconsistent with line 403. (With the correct f^*=y^\top\mu+1/2\|\mu\|^2, there is no \|y\|^2 term here at all.)
  - proposed: \sup_{\boldsymbol{\mu}}\left[-\mathbf{y}^\top \boldsymbol{\mu} - \frac{1}{2} \|\boldsymbol{\mu}\|_2^2 - I_{\{\|X^\top\boldsymbol{\mu}\|_\infty \leq \lambda\}}\right]

- **ConvexOptimization/17.Quasi-Newton-Methods.md** [notation/low/likely]
  - quote: `\hat{H}_0^k = \gamma_k I, \quad \text{where } \quad \gamma_k`
  - issue: Notation inconsistency for the L-BFGS initial matrix. Here it is written \hat{H}_0^k, but the surrounding text (line 510 '来近似 $H^{k-m}$ 的值'), the two-loop pseudocode (line 577), and the optimization pseudocode (line 590) all denote the same object \hat{H}_0^{k-m}. Using the superscript k here mislab
  - proposed: \hat{H}_0^{k-m} = \gamma_k I, \quad \text{where } \quad \gamma_k

- **ConvexOptimization/17.Quasi-Newton-Methods.md** [logic/low/unsure]
  - quote: `首先重申记号.`
  - issue: The Global-Convergence-of-BFGS theorem (line 244) is stated for a general '二阶可微的目标函数' with a convex level set L and m I ⪯ ∇²f ⪯ M I on L, yet its conclusion (line 256) and the proof sketch (line 262 '由于 $f$ 是凸的, 因此该 stationary point 就是一个全局最优解') silently assume f is convex to promote a stationary poi
  - proposed: 首先重申记号. (建议在定理假设中明确 $f$ 为凸函数, 或将结论改为收敛到 stationary point.)

- **ConvexOptimization/19.Numerical-Linear-Algebra.md** [math/medium/unsure]
  - quote: `其最终的误差敏感性大约为 $\kappa(\mathbf{X}) + \|\mathbf{Y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 \cdot \kappa^2(\mathbf{X`
  - issue: In the standard least-squares perturbation result the term multiplying κ²(X) involves the residual to the first power (via tan θ = ‖r‖/‖Xβ‖), not the squared residual norm ‖Y−Xβ‖². The squared residual appears to be an error.
  - proposed: 其最终的误差敏感性大约为 $\kappa(\mathbf{X}) + \|\mathbf{Y} - \mathbf{X} \boldsymbol{\beta}\|_2 \cdot \kappa^2(\mathbf{X})$

- **ConvexOptimization/19.Numerical-Linear-Algebra.md** [math/low/unsure]
  - quote: `对于分解后的系统, 求解的复杂度约为 $\mathcal{O}(3n^2)$ flops.`
  - issue: Solving after LU is two triangular solves (Ly=Pb then Ux=y), each ≈ n² flops, for ≈2n² total — matching the Cholesky solve cost of O(2n²) stated later. The constant 3n² appears too large.
  - proposed: 对于分解后的系统, 求解的复杂度约为 $\mathcal{O}(2n^2)$ flops.

- **StatisticalInference/EstimationTheory/UMVUE.md** [notation/low/likely]
  - quote: `\hat{\theta}(\mathbf{X}) = \arg\min_{\theta} \text{MSE}(\hat{\theta}(\mathbf{X}))`
  - issue: The minimization index θ is the parameter being estimated, but the best estimator is obtained by minimizing over the choice of estimator (the function/decision rule), not over θ. Indexing argmin by θ while equating it to θ̂(X) is inconsistent.
  - proposed: \hat{\theta}(\mathbf{X}) = \arg\min_{\hat\theta} \text{MSE}(\hat{\theta}(\mathbf{X}))

- **StatisticalInference/InformationAndSufficiency/Neyman-Factorization-Theorem.md** [notation/low/likely]
  - quote: `}_{g(\sum \textbf{X},\mu) ~(\text{with } \sigma,n \text{ known})}`
  - issue: Bold X denotes the sample vector, but here the intended argument of g is the scalar statistic Σx_i (= S(X)). Using Σ**X** as a subscript label conflicts with S(X)=Σx_i used everywhere else in the same derivation.
  - proposed: }_{g(\sum x_i,\mu) ~(\text{with } \sigma,n \text{ known})}

- **StatisticalInference/Nonparametric/Kruskal-Wallis-Test.md** [notation/low/likely]
  - quote: `Assume there are $k$ independent population groups with sample sizes $n_1, n_2, n_3$. Given the null hypothesi`
  - issue: The test is stated for general k groups, but the sample sizes and the null hypothesis are written with only 3 explicit subscripts (n_1,n_2,n_3 and median_1..median_3), which is inconsistent with the k-group formulation used in the statistic (sum over j=1..k) and the table (rows 1..k).
  - proposed: Assume there are $k$ independent population groups with sample sizes $n_1, n_2, \ldots, n_k$. Given the null hypothesis $H_0: \text{median}_1 = \text{median}_2 = \cdots = \text{median}_k$

- **StatisticalLearningAlgorithms/Linear/Generalized-Linear-Models.md** [typo/medium/certain]
  - quote: `    \pi_i = \mathrm{x}^\top.`
  - issue: The identity-link equation is missing the coefficient vector β on the right-hand side; it should be π_i = x^T β (matching every other link equation in this section).
  - proposed:     \pi_i = \mathrm{x}^\top \beta.

- **StatisticalLearningAlgorithms/Linear/Generalized-Linear-Models.md** [notation/low/likely]
  - quote: `死亡率 $\pi_i = \mathbb{P}(U<d_i) = F_X(x)$.`
  - issue: The tolerance distribution was introduced as F(u) for the variable U at dose d_i, but this writes F_X(x) — a symbol switch to X/x that is never defined here. It should be F(d_i) (equivalently F_U(d_i)).
  - proposed: 死亡率 $\pi_i = \mathbb{P}(U<d_i) = F(d_i)$.

- **StatisticalLearningAlgorithms/Linear/Linear-Regression.md** [notation/low/likely]
  - quote: `其中 $j=1,2,\ldots,p$, 也就是同步更新所有的特征.`
  - issue: Feature count is denoted p here, but the hypothesis h(x)=Σ_{i=0}^n θ_i x_i indexes features up to n, and n is also used as the sample count in the cost function Σ_{i=1}^n. The same symbol n stands for both #features and #samples, and the feature dimension is called both n and p. This ambiguous overl
  - proposed: 其中 $j=0,1,\ldots,n$, 也就是同步更新所有的特征 (此处 $n$ 指特征维数, 与样本量记号需区分).

- **StatisticalLearningAlgorithms/Kernel/Kernel-Methods.md** [notation/low/unsure]
  - quote: `输入矩阵为:

$$
{\Phi} :=
\begin{bmatrix}
1 & \phi(\boldsymbol{x_1})^\top \\`
  - issue: The feature/design matrix Φ (capital Phi) collides with the feature map φ (lowercase phi) used in its own entries φ(x_i). Elsewhere Φ is also used in RKHS notes for the kernel map. Within this section the design matrix and the map are barely distinguished typographically; worth disambiguating (e.g. 
  - proposed: 输入矩阵为 (记为设计矩阵 $Z$, 以区别于特征映射 $\phi$):

$$
{Z} :=
\begin{bmatrix}
1 & \phi(\boldsymbol{x_1})^\top \\

- **StatisticalLearningAlgorithms/Kernel/Kernel-Methods.md** [notation/low/unsure]
  - quote: `\in \mathbb{R}^{N \times (D+1)}.`
  - issue: Input dimension was defined as d (x_i ∈ ℝ^d, φ: ℝ^d → ℋ) a few lines above, but the feature-space dimension is introduced here as capital D without definition. Minor unexplained symbol switch d→D.
  - proposed: \in \mathbb{R}^{N \times (D+1)}, \text{ 其中 } D = \dim\mathcal{H}.

- **StatisticalLearningAlgorithms/Classification/Naive-Bayes-Classifier.md** [notation/low/likely]
  - quote: `&= \frac{\prod_{i=1}^n p(x_i|y=1)p(y=1)}{\prod_{i=1}^n p(x_i|y=1)p(y=1)+\prod_{i=1}^n p(x_i|y=0)p(y=0)}.`
  - issue: The feature dimension is k throughout section 1 (features x_1,...,x_k; the Naive Bayes assumption product runs \prod_{i=1}^k). Here the posterior product is indexed to n, which is not defined in this model (n is introduced only later in the multinomial event model). Should be k for consistency.
  - proposed: &= \frac{\prod_{i=1}^k p(x_i|y=1)p(y=1)}{\prod_{i=1}^k p(x_i|y=1)p(y=1)+\prod_{i=1}^k p(x_i|y=0)p(y=0)}.

- **StatisticalLearningAlgorithms/Nonparametric/Regression-Splines.md** [notation/low/likely]
  - quote: `$K+4$ predictors, including the intercept: $X, X^2, X^3, h(X, \xi_1), h(X, \xi_2), \cdots, h(X, \xi_K), \beta_`
  - issue: The list of predictors ends with the coefficient symbol beta_0 rather than the intercept predictor. beta_0 is a coefficient, not a predictor; the intercept 'predictor' is the constant 1. Mixing a coefficient into the predictor list is a category error (the count K+4 is correct: 3 power terms + K bas
  - proposed: $K+4$ predictors, including the intercept: $1, X, X^2, X^3, h(X, \xi_1), h(X, \xi_2), \cdots, h(X, \xi_K)$

- **DeepLearning/5.Recurrent-Neural-Networks.md** [notation/medium/likely]
  - quote: `\text{Perplexity} = \frac{1}{T} \sum_{t=1}^T -\log \mathbb{P}(x_t | x_{t-1}, \ldots, x_1)`
  - issue: This average-negative-log-likelihood quantity is labeled 'Perplexity', but two paragraphs later the note says 'exponentiating this metric gives us perplexity' and defines a second, different-looking formula \text{Plxy} as the actual perplexity (= exp of this same sum). The two labels contradict each
  - proposed: \text{CrossEntropy} = \frac{1}{T} \sum_{t=1}^T -\log \mathbb{P}(x_t | x_{t-1}, \ldots, x_1)

- **DeepLearning/6.Modern-RNNs.md** [katex/low/likely]
  - quote: `\end{bmatrix}\\
\mathbf{O}_t = \mathbf{H}_t\mathbf{W}_{hq} + \mathbf{b}_q`
  - issue: A bare \\ line break is used outside any aligned/array/matrix environment in this display-math block (it appears right after \end{bmatrix}, not inside one). KaTeX only supports \\ inside environments like aligned or array; used bare in plain display math it is invalid syntax and will error or render
  - proposed: \end{bmatrix}
$$
$$
\mathbf{O}_t = \mathbf{H}_t\mathbf{W}_{hq} + \mathbf{b}_q

- **DeepLearning/5.Recurrent-Neural-Networks.md** [typo/low/unsure]
  - quote: `通过引入一个 hidden state $h_t$ 来概选定时间窗口的历史信息`
  - issue: Garbled phrase: '概选定' is not a coherent Chinese verb phrase. Compare the parallel phrasing two lines later ('维护这样一个 hidden state $h_t$ 来概括历史信息'), which uses the correct verb 概括 (summarize).
  - proposed: 通过引入一个 hidden state $h_t$ 来概括截止到当前时间步的历史信息

- **DeepLearning/5.Recurrent-Neural-Networks.md** [typo/low/unsure]
  - quote: `我们可以认为这个序列是独立的到的`
  - issue: Garbled phrase, not grammatical Chinese. Given the following clause ('但是对于序列中的每个元素往往是有关联的' — but elements are usually correlated), the intended meaning is likely that the sequence is 'independently sampled' as a whole unit, contrasted with within-sequence correlation.
  - proposed: 我们可以认为这个序列是独立采样得到的

- **DeepLearning/6.Modern-RNNs.md** [typo/low/unsure]
  - quote: `一般而言 $h\in(64,2056)$, $L\in(1,8)$.`
  - issue: 2056 is very likely a typo for 2048 (2^11), the standard round hidden-size value typically cited for this range; 2056 is not a conventional number in this context.
  - proposed: 一般而言 $h\in(64,2048)$, $L\in(1,8)$.

- **DeepLearning/7.Attention-and-Transformer.md** [notation/medium/likely]
  - quote: `\text{Softmax}\left(\frac{\mathbf{Q} \mathbf{K}^\top}{\sqrt{d_\mathrm k}}\right) \mathbf{V}`
  - issue: Section 4.1 explicitly defines d as the shared query/key feature dimension and uses it consistently (lines with q^T k_i / sqrt(d), and the immediately preceding boxed formula A = Softmax(QK^T/sqrt(d))). This formula (repeated at two places in the note) silently switches to d_k without ever defining 
  - proposed: \text{Softmax}\left(\frac{\mathbf{Q} \mathbf{K}^\top}{\sqrt{d}}\right) \mathbf{V}

- **DeepLearning/7.Attention-and-Transformer.md** [math/low/unsure]
  - quote: `得到 $\mathrm A^{(h)} \in \mathbb R^{n \times n}$. 最终将所有的 head 的输出拼接起来, 映射回原始的维度`
  - issue: A^{(h)} is defined here as the n×n attention-weight matrix (softmax(QK^T) for head h). But what actually gets concatenated across heads in multi-head attention is each head's post-value output (A^{(h)} V^{(h)}, of size roughly (d_model/h)×n), not the raw n×n attention-weight matrices themselves. Con
  - proposed: 得到 head 的输出 $\mathrm A^{(h)} \mathrm V^{(h)}$. 最终将所有 head 的输出拼接起来, 映射回原始的维度

- **DeepLearning/8.Transformer-and-Variants.md** [typo/medium/likely]
  - quote: `Linear Attention 就是广义 RNN 去掉了 Reflection $f_{A,t}$`
  - issue: 'Reflection' is used (here and 2 more times later, in the '更复杂的 Reflection' subsection) as the name for f_{A,t}, the hidden-state transition/gating function. The note itself explicitly describes f_{A,t} as playing the role of the LSTM forget gate (section 1.1, line 44) and as a decay/gating term (Re
  - proposed: Linear Attention 就是广义 RNN 去掉了 Recurrence $f_{A,t}$

- **NLPAndLLMs/Inference/Uncertainty-in-LLMs.md** [notation/medium/likely]
  - quote: `V(y) = \sum_{i: y_i \in \mathcal{Y}} v(r_i).`
  - issue: The summation condition 'y_i ∈ 𝒴' is nearly vacuous if 𝒴 is the set of all distinct candidate answers (as used two lines later in the argmax over 𝒴) — essentially every y_i satisfies this, so V(y) would not actually depend on the specific y being scored, defeating the stated purpose of grouping cand
  - proposed: V(y) = \sum_{i: y_i = y} v(r_i).

- **NLPAndLLMs/Inference/Uncertainty-in-LLMs.md** [math/low/unsure]
  - quote: `如果采用 negative perplexity:`
  - issue: The subsequent formula displayed is plain PPL = exp(-avg log p), i.e. standard (non-negated) perplexity, not its negation — despite the bullet and the image caption above both labeling this 'negative perplexity'. As written, PPL is small when confident (consistent with the earlier Perplexity subsect
  - proposed: 如果采用 perplexity (取负号以对齐 confidence 方向, negative perplexity):

- **NLPAndLLMs/Inference/Deep-Reasoning-for-LLMs.md** [typo/low/likely]
  - quote: `Long Chain of Thought" (LoT), 把之前传统 CoT 称为 "Short Chain of Thought" (SoT)`
  - issue: Both abbreviations drop the 'C' from the already-established 'CoT' abbreviation used throughout this note, producing non-standard/incorrect initialisms. 'Long Chain of Thought' should abbreviate to LCoT, and 'Short Chain of Thought' should abbreviate to SCoT — using 'SoT' is additionally confusing s
  - proposed: Long Chain of Thought" (LCoT), 把之前传统 CoT 称为 "Short Chain of Thought" (SCoT)

- **NLPAndLLMs/Inference/Context-Engineering.md** [notation/low/likely]
  - quote: `f_{\text{LM}}(x) = \mathbb{P}(x_{t+1}|x_t).`
  - issue: The sentence just before this formula introduces the input as x_t ('给定输入 $x_t$'), and the RHS of the formula itself conditions on x_t, but the function argument on the LHS uses an unsubscripted, never-separately-defined x instead of x_t. The same bare x recurs in the next paragraph ('当我们的输出 $f_{\tex
  - proposed: f_{\text{LM}}(x_t) = \mathbb{P}(x_{t+1}|x_t).

- **LearningRoadmaps/Stochastic-Programming-and-Bilevel-Optimization-Roadmap.md** [typo/medium/likely]
  - quote: `topics including recourse, SAA, scenario tree, nonparticipativity, value function, etc.`
  - issue: 'Nonparticipativity' is not a real term in stochastic programming. The standard concept relevant to this module (decisions cannot depend on future/unrevealed information) is 'nonanticipativity' — this looks like a mangled/misremembered version of that term.
  - proposed: topics including recourse, SAA, scenario tree, nonanticipativity, value function, etc.

- **LearningRoadmaps/Stochastic-Programming-and-Bilevel-Optimization-Roadmap.md** [fact/medium/unsure]
  - quote: `URL: [https://arxiv.org/abs/2604.14075](https://arxiv.org/abs/2604.14075)`
  - issue: This arXiv identifier and the accompanying optimization-online.org/wp-content/uploads/2026/04/ path both encode a very recent (April 2026) submission date for a paper by 'Şen, Hu, Kuhn'. Given the note's own preface states this whole roadmap was generated by ChatGPT, and this is the single most rece
  - proposed: Verify this arXiv ID and the paper's existence/authorship directly on arxiv.org before treating it as a citable source; replace or remove if it cannot be confirmed.

- **LearningRoadmaps/Stochastic-Programming-and-Bilevel-Optimization-Roadmap.md** [logic/low/unsure]
  - quote: `This roadmap generally is composed of the following 8 sections:`
  - issue: The 8-item thematic list does not fully cover the document's own content: Module 6 (KKT Reformulation, MPEC, and Implicit Function Ideas) is not represented by any of the 8 listed themes, and the list does not correspond 1:1 to the document's actual Module 0 through Module 9 (10 modules).
  - proposed: This roadmap generally is composed of the following themes (spanning Modules 0-9):

## Adjudication notes

- Two "high" findings on 01_DiscreteTimeMarkovChain (recurrence box) were REJECTED:
  under the note's own definition tau_i = number of returns (E[tau_i] = sum P_ii(n)),
  the boxed case analysis is correct; only the two 即-clauses in the prose were wrong
  and were fixed instead (see the corrections commit).
- The reviewer fix for the strong-convexity chord bound (2.Convexity-I) mismatched the
  chord parametrization; the applied fix uses theta*f(x) + (1-theta)*f(y).
- The Lipschitz definition completed in 14.Newton-Method uses the HESSIAN Lipschitz
  condition (matching the L in the quadratic-convergence theorem), not gradient Lipschitz.
- 31 of 105 proposed cross-links were skipped by guardrails (anchors inside math/code/
  headings, or overlong anchors); see git history of this file's commit for the script.
