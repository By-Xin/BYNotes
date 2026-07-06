---
title: "Generalized Linear Models"
aliases:
  - "Generalized_Linear_Models"
  - "Generalized Linear Models"
  - "GLM"
  - "广义线性模型"
  - "StatisticalLearningAlgorithms/Linear.Generalized-Linear-Models"
course: "Statistical Learning Algorithms"
type: "topic-note"
status: "draft"
tags:
  - course/statistical-learning-algorithms
  - topic/linear-models
  - topic/glm
---

> [!quote] References
> - Lecture: Advanced Categorical Data Analysis

## 1. Model Selection and Fitting Binary Data

### 1.1 Overview

- 评价一个模型的 goodness of fit 有两种常用指标:
  - Deviance.
  - Pearson's chi-square.
- 上述两种统计量都服从或近似服从 $\chi^2$ 分布.
- 用 Drop-in-Deviance 来比较 nested models 的拟合效果.
- 用 R 中的 `anova()` 函数进行 Deviance Test.
- 范例: Titanic 数据, 用 R 进行数据拟合、预测、检验与可视化.

### 1.2 Deviance and Pearson's Chi-Square

#### 1.2.1 Deviance

对于一个含有 $n$ 个观测的数据集, 可拟合的模型可以从 *NULL Model* 到 *Saturated Model*. NULL Model 对全部 $Y$ 只用 $\mu$ 进行刻画; Saturated Model 对每一个观测都有一个参数, 即 perfect fit.

参考似然比检验的思想, 定义 deviance 为一个目标模型与饱和模型的似然比.

**Definition (Deviance).**

$$
D^*(y,\hat\mu) = -2 \log \frac{L (y,\hat\mu)}{L (y,y)}  = 2\log \ell(y;y) - 2\log \ell(\hat\mu;y) \ge 0 \to \chi^2(n-d).
$$

其中 $\ell(y;y)$ 是饱和模型的对数似然, $\ell(\hat\mu;y)$ 是目标模型的对数似然. $n$ 是观测数, $d$ 是目标模型的参数数.

Deviance 可以理解为目标模型的拟合效果与饱和模型的拟合效果的差异. 因此 deviance 越大, 拟合差异越大, 拟合效果越差.

可以证明, 在 OLS 下, deviance 即为 RSS. 因此在整体理解上可以当作 RSS 的推广. 显然我们希望 deviance 越小越好.

> [!note] Note: Deviance conventions
> 不同模型有不同分布, 对应不同似然函数, 因此也对应不同 deviance. 其中 Bernoulli 单次 0-1 事件的 deviance 函数不适用, 其没有办法反映模型的拟合效果. 其余分布的详细 deviance 函数可以参考课件 Lecture 4, p. 8.

#### 1.2.2 Pearson $\chi^2$

Pearson's Chi-Square 是另一种用于检验拟合效果的统计量.

**Definition (Pearson's Chi-Square).**

$$
\chi^2 = \sum_{i=1}^n w_i \frac{(y_i - \hat\mu_i)^2}{\text{Var}(\hat\mu_i)} \sim \chi^2(n-d).
$$

其中 $w_i$ 是权重, 通常取为 $1$. $\text{Var}(\hat\mu_i)$ 是 $\hat\mu_i$ 的方差.

#### 1.2.3 Drop-in-Deviance for Nested Models

在比较两个 nested models 时, 可以使用 Drop-in-Deviance 来比较两个模型的拟合效果.

**Definition (Nested Models).** 称模型 $M_1$ 是模型 $M_2$ 的 nested model, 如果 $M_1$ 可以通过令 $M_2$ 的部分参数为 $0$ 得到.

**Definition (Drop-in-Deviance).** 给定两个模型 $M_0$ nested in $M_1$, 则 Drop-in-Deviance 定义为:

$$
D_{M_0}-D_{M_1} \sim \chi^2(d_1-d_0),
$$

其中 $d_1$ 是 $M_1$ 的参数数, $d_0$ 是 $M_0$ 的参数数.

事实上, Drop-in-Deviance 的本质是检验一系列参数 $\beta_i = \cdots = \beta_j = 0$ 是否成立. 这也是为什么 Drop-in-Deviance 只能用于 nested models 的比较.

> [!note] Note: Nested model quiz
> 考虑两个模型 $M_1: \text{logit}(p) = \beta_0 + \beta_1 x_1$ 和 $M_2: \text{probit}(p) = \beta_0 + \beta_1 x_1 + \beta_2 x_2^2$. 则 $M_1$ 不是 $M_2$ 的 nested model. 尽管可以令 $\beta_2 = 0$ 从而使 RHS 成立, 但 LHS 的 link function 不同, 因此两者不是 nested models, 亦不能使用 Drop-in-Deviance 来比较.

另外注意: 尽管 deviance 本身对于 Bernoulli 分布不适用, 但是 Drop-in-Deviance, 即两个模型的 deviance 之差, 是适用的. 因此在比较两个模型的拟合效果时, 可以使用 Drop-in-Deviance.

### 1.3 Deviance Test in R

**Single Deviance Test.**

```r
pchisq(fm$deviance, fm$df.residual, lower.tail = FALSE)
```

对于那些可以使用 deviance 进行检验的模型, 假设已经拟合了一个模型 `fm`, 则可以使用 `pchisq(fm$deviance, fm$df.residual, lower.tail=FALSE)` 进行检验. 其中 `fm$deviance` 是模型的 deviance, `fm$df.residual` 是模型的自由度.

这个检验用来对比 `fm` 与一个饱和模型的拟合效果. 因此, 如果 $P<0.05$, 则说明模型的拟合效果与饱和模型有显著差异, 即模型不是一个 adequate model. 如果 $P>0.05$, 则认为模型已经拟合充分, 即 do not reject the hypothesis that current model provides an adequate fit. 但是无法说明这个模型就是最优的, 只能说明这个模型和饱和模型的拟合效果没有显著差异, 是可以接受的.

**Drop-in-Deviance Test for Nested Models Comparison.**

```r
anova(MODELs, test = "Chisq")
```

在 R 中, Drop-in-Deviance 可以通过 `anova(MODELs, test='Chisq')` 进行检验. 其中 `MODELs` 是一个包含了 nested models 的模型列表, `test='Chisq'` 用来输出检验的 p-value.

若 `MODELs` 只有一个模型, 则程序会从 NULL model 开始, 逐步增加变量, 按照模型列表的顺序, 与上一个模型进行 Drop-in-Deviance 检验. 若 `MODELs` 有多个模型, 则程序会直接进行两两模型的 Drop-in-Deviance 检验.

若某个模型对应的 $P<0.05$, 则说明该模型的拟合效果与上一个模型有显著差异, 即这个模型是一个更好的模型, 这个模型的新增变量显著不为 $0$, 是对模型产生显著影响的, 因此应该保留.

例如:

```r
> anova(fm1, test="Chisq")

Analysis of Deviance Table
Model: binomial, link: logit
Response: Survived
Terms added sequentially (first to last)
Df Deviance Resid. Df Resid. Dev Pr(>Chi)
NULL 755 1025.57
Sex 1 228.929 754 796.64 < 2.2e-16
Age 1 1.058 753 795.59 0.3036
Sex:Age 1 25.030 752 770.56 5.645e-07
```

表示: 从 NULL Model 开始, 其原始 deviance 为 $1025.57$, df 为 $755$. 在此基础上引入 `Sex` 后, deviance 减少为 $796.64$, df 为 $754$. 由 $P<2.2e-16$ 可以看出, 引入 `Sex` 后的模型显著优于 NULL Model, 因此 `Sex` 是一个显著的变量. 以此类推.

> [!note] Note: Deviance test ordering
> 1. Deviance test 顺序是按照模型列表的顺序进行的, 因此在模型列表中的顺序很重要. 有可能在给定变量 $X_1$ 的基础上, 引入变量 $X_2$ 会显著; 但反之在给定变量 $X_2$ 的基础上, 引入变量 $X_1$ 会不显著.
> 2. 要满足 hierarchical principle, 即在引入更高阶的变量时, 对应的低阶变量不能被删除.
>
> 原文此处引用了一个本地 `image.png`, 但源目录中没有该图片文件, 因此发布版不展示这个缺失图片.

## 2. Binomial Data

### 2.1 Overview

- Grouped data 与 ungrouped data.
- Binomial 模型的拟合过程与系数解读.
- Odds, odds ratio, relative risk 与 risk difference 的含义与计算.
- 除了 logit link 外, 其他 link function 的含义与应用.
- 残差的种类与计算.

### 2.2 Grouped Data and Ungrouped Data

对于同样一组数据, 其可以以两种形式出现: grouped data 与 ungrouped data.

对于 grouped data, 每一行相当于一个类别的集合, 例如:

$$
\begin{array}{|c|c|c|}
\hline
\text{Age} & \text{Frequency} & \text{Survived} \\
\hline
0-10 & 100 & 80 \\
10-20 & 200 & 150 \\
\hline
\end{array}
$$

对于 ungrouped data, 每一行相当于一个观测, 即一个独立的个体:

$$
\begin{array}{|c|c|}
\hline
\text{Age} & \text{Survived} \\
\hline
5 & 1 \\
15 & 0 \\
20 & 1 \\
\hline
\end{array}
$$

尽管 grouped data 可以由 ungrouped data 得到, 但两者的建模方式是不同的:

- 在 GLM 建模中, 建模的基本单位都是行, 即一个观测. 对于 grouped data, 往往认为其服从一个 Binomial 分布, 隐含一组内所有个体是同质的, 概率相同. 对于 ungrouped data, 其针对每个个体是一个单独的 Bernoulli 分布, 隐含每个个体都会有一个独立概率. 这可能包含更多信息, 但也增加模型复杂度, 或许带来更多噪音.
- 对于 ungrouped data, 随着样本量增加, 数据的观测数也会增加, 因此没法给出其关于 deviance 的渐进性质. 但是对于 grouped data, 其行数与组数有关而与样本量无关, 因此能够给出关于 deviance 的渐进性质. 在这个意义上, grouped data 有时候更加方便.

### 2.3 Binomial Model Fitting and Interpretation

本小节以 Skin Cancer 数据集为例, 介绍如何对拟合的 Binomial 模型进行解读, 尤其是在 R 环境下.

Skin Cancer 数据集包含 15 个观测, 包含变量 `Cases` (患病数), `Town` (城镇名), `Age` (年龄段) 与 `Population` (该地区的总人口). 目标是用 `Age` 与 `Town` 来预测皮肤癌发病率. 这里假设 $Y_i \sim \text{Binomial}(n_i, p_i)$, 其中 $n_i$ 是该地区的总人口, $p_i$ 是发病率.

在 R 中导入数据后, 可以通过 `str()` 查看数据结构. 尤其注意 `Factor` 类型变量, 其第一个水平是基准水平.

```r
> str(skin)

'data.frame': 15 obs. of 4 variables:
$ Cases : int 1 16 30 71 102 130 133 40 4 38 ...
$ Town : Factor w/ 2 levels "0","1": 1 1 1 1 1 1 1 1 2 2 ...
$ Age : Factor w/ 8 levels "15-24","25-34",..: 1 2 3 4 5 6 7 8 1 2 ...
$ Population: int 172675 123065 96216 92051 72159 54722 32185 8328 181343 146207 ...
```

对于 Binomial 模型, 可以用 `glm(formula = cbind(Cases, Population-Cases) ~ Town + Age, family = binomial, data = skin)` 进行拟合. 其中 `cbind(Cases, Population-Cases)` 表示每个地区的发病数与未发病数, `family = binomial` 指定模型的分布为 Binomial 分布.

注意, `formula` 中变量的顺序将影响后续 Deviance Test 的顺序.

模型最终拟合结果如下:

```r
> summary(fm)

Call:
glm(formula=y.Bin~ Age + Town, family=binomial, data=skin)
Deviance Residuals:
Min 1Q Median 3Q Max
-1.2830 -0.3355 0.0000 0.3927 1.0820
Coefficients:
Estimate Std. Error z value Pr(>|z|)
(Intercept) -11.69364 0.44923 -26.030 < 2e-16
Age25-34 2.62915 0.46747 5.624 1.86e-08
Age35-44 3.84627 0.45467 8.459 < 2e-16
Age45-54 4.59538 0.45104 10.188 < 2e-16
Age55-64 5.08901 0.45031 11.301 < 2e-16
Age65-74 5.65031 0.44976 12.563 < 2e-16
Age75-84 6.20887 0.45756 13.570 < 2e-16
Age85+ 6.18346 0.45783 13.506 < 2e-16
Town1 0.85492 0.05969 14.322 < 2e-16
Null deviance: 2330.4637 on 14 degrees of freedom
Residual deviance: 5.1509 on 6 degrees of freedom
AIC: 110.1
Number of Fisher Scoring iterations: 4
```

注意这里的自由度:

- `Null deviance` 的自由度为 $df_{\text{Null}} = n-1_{(\text{intercept})} = 15-1 = 14$.
- `Residual deviance` 的自由度为 $df_{\text{Residual}} = n-p-1_{(\text{intercept})} = 15-8-1 = 6$.

模型的数学表达为:

$$
\text{logit}(\pi_i) = \log \frac{\pi_i}{1-\pi_i} = \mathrm{x}^\top \beta.
$$

其中 $Y_i$ 是皮肤癌的发病情况, $\pi_i$ 是发病率, $\mathrm{x}$ 是模型中的变量, $\beta_0,\ldots,\beta_k$ 是模型系数.

**Interpretation (Intercept $\beta_0$).** The odds of $Y=1$ when all predictors $\mathrm{x}$ are baseline is $\exp(\beta_0)$. 在本例中, 当 `Age=15-24` 且 `Town=0` 时, 皮肤癌的发病 odds 是 $\exp(-11.69364)$.

**Interpretation (Slope $\beta_i$).** Given all other predictors are fixed, $\delta$-unit increase in $X_i$ will result in $\exp(\beta_i \delta)$ times increase in the odds of $Y=1$:

$$
\begin{aligned}
\frac{\text{odds}(Y=1|\mathrm{x}_j = A+\delta) }{\text{odds}(Y=1|\mathrm{x}_j = A)}
&= \exp(\beta_i \delta), \\
\Rightarrow \text{odds}(\mathrm{x}_j = A+\delta)
&= \exp(\beta_i \delta) \cdot \text{odds}(\mathrm{x}_j = A).
\end{aligned}
$$

在本例中 `Town1: 0.85492`: 对于同样年龄段, 在 `Town=1` 地区的人, 皮肤癌发病 odds 是 `Town=0` 地区的人的 $\exp(0.85492)$ 倍.

在本例中 `Age25-34: 2.62915`: 对于同样地区, 在年龄段 `25-34` 的人, 皮肤癌发病 odds 是 `15-24` 的人的 $\exp(2.62915)$ 倍.

**Interpretation (Interaction Terms).** 在本例中, 通过 `anova(fm, fm1, test = "Chisq")` 的检验发现引入交互项 `Age:Town` 并不显著, 这可以解释为:

- Effect of `Town` is homogeneous across all `Age` groups.
- Effect of `Age` is homogeneous across all `Town` groups.

### 2.4 Odds Ratio and Related Metrics

- **Odds.** 假设某事件发生的概率为 $p$, 则其 odds 为 $\frac{p}{1-p}$. 可以理解为事件成功的概率是失败的 $\frac{p}{1-p}$ 倍. 若一个事件成功概率很低, 则 $\text{odds}= \frac{p}{1-p} \approx p$.
- **Odds Ratio.** 两个事件的 odds 之比:

  $$
  \text{OR} = \frac{\pi_1/(1-\pi_1)}{\pi_2/(1-\pi_2)} = \frac{\pi_1}{\pi_2} \cdot \frac{1-\pi_2}{1-\pi_1}.
  $$

  可以理解为两个事件成功的概率之比.

  $$
  \begin{array}{c|c|c}
  &  Y=1 (\text{Success}) & Y=0 (\text{Failure}) \\
  \hline
  X=1 (\text{Condition} 1) & \pi_1 & 1 - \pi_1 \\
  X=0 (\text{Condition} 2) & \pi_2 & 1 - \pi_2
  \end{array}
  $$

  若 $\text{OR} = 1$, 即 $\log \text{OR} = 0$, 则两个事件的 odds 相等, 即两个事件的成功概率相等. 或可以认为 $X$ 与 $Y$ 相互独立.

- **Relative Risk.** $\text{RR} = \frac{\pi_1}{\pi_2}$. 可以理解为两个事件成功的概率之比. 当 $X$ 与 $Y$ 相互独立时, $\text{RR} = 1$.
- **Risk Difference.** $\text{RD} = \pi_1 - \pi_2$. 可以理解为两个事件成功的概率之差. 当 $X$ 与 $Y$ 相互独立时, $\text{RD} = 0$.

在 GLM 中, 一般选择的 `logit` link function 对应于 odds. 其他 link function 也会对应于不同指标.

- `log` link function 对应于 relative risk:

  $$
  \log \pi_i = \mathrm{x}^\top \beta \Rightarrow \pi_i = \exp(\mathrm{x}^\top \beta)\in (0, \infty).
  $$

  这暗含一个问题: 这个模型并没有直接约束概率 $\pi$ 在 $[0,1]$ 之间, 因此可能产生不合理结果.

- `identity` link function 对应于 risk difference:

  $$
  \pi_i = \mathrm{x}^\top.
  $$

  `identity` link 削弱了模型约束条件, 因此拟合过程中可能产生一系列问题. 即使是 `identity` link, 其与 `lm()` 也并不等价. 因为 `lm()` 基于 $Y$ 服从正态分布的假设, 而 `glm(link = "identity")` 基于 $Y$ 服从二项分布的假设.

> [!note] Note: Metric interpretation
> 在描述上, 上述指标没有太大区别. 在实际运用中, 控制住其他变量不变, 用对应的关系指标进行替换即可.

### 2.5 Residual Analysis

首先回顾, 在传统 OLS 中, 残差被定义为 $e_i = y_i - \hat{y}_i$. 其中有一个较强假设为 $e_i \sim N(0, \sigma^2 I)$, 即残差是同方差的. 但是在 GLM 中, 由于假设 $Y_i \sim \text{Binomial}(n_i, p_i)$, 因此每个观测的方差不同: $\text{Var}(Y_i) = n_i p_i (1-p_i)$. 因此残差定义也会有所不同.

> [!note] Note: Residuals and observations
> 残差是和每个观测一一对应的, 有多少个样本就有多少项残差. 相当于每个真实观测值和预测值之间的差异. 因此残差是用来评价模型拟合效果的重要指标.

考虑 GLM 模型 $Y_i \sim \text{Binomial}(m_i, \pi_i)$. 则正常残差 (raw residual) 定义为 $y_i - \hat{\mu}_i = y_i - m_i \hat{\pi}_i$. 但考虑到上述方差问题, 对 raw residual 进行改进, 得到下面四种 GLM 中常用的残差定义:

- **Pearson Residual.**

  $$
  r_{P_i} = \frac{y_i - m_i \hat{\pi}_i}{\sqrt{m_i \hat{\pi}_i (1-\hat{\pi}_i)}}.
  $$

  进一步可知, 一系列 Pearson residuals 的平方和服从 $\chi^2$ 分布:

  $$
  \sum_{i=1}^n r_{P_i}^2 \sim \chi^2(n-p).
  $$

- **Deviance Residual.** 用于检验模型的拟合效果, 与 Pearson residual 类似, 但是其对于过度离群值的惩罚更大:

  $$
  r_{D_i} = \text{sign}(y_i - m_i \hat{\pi}_i) \sqrt{2 \left[ y_i \log \left(\frac{y_i}{m_i \hat{\pi}_i}\right) + (m_i - y_i) \log \left(\frac{m_i - y_i}{m_i - m_i \hat{\pi}_i}\right) \right]}.
  $$

- **Standard Pearson Residual.**

  $$
  r_{SP_i} = \frac{r_{P_i}}{\sqrt{1-h_{ii}}},
  $$

  where $h_{ii}$ is the leverage value.

- **Standard Deviance Residual.** 在 GLM 中最常用:

  $$
  r_{SD_i} = \frac{r_{D_i}}{\sqrt{1-h_{ii}}}.
  $$

  近似服从标准正态分布: $r_{SD_i} \sim N(0, 1)$.

  一般而言, 若模型的拟合是合适的, 则应有 $-2 \leq r_{SD_i} \leq 2$. 否则, 模型拟合效果可能存在问题. 在 R 中, 可以通过 `boot::glm.diag(fm)$rd` 获取.

通常可以刻画如下三种残差关系图:

- **Residual vs Fitted.** 用于检验残差是否随着拟合值增加而增加, 从而检验模型是否存在异方差性.
- **Residual vs Explanatory Variable.** 用于检验残差是否随着解释变量增加而增加, 从而检验模型是否存在非线性.
- **Residual vs index.** 用于检验残差是否随着观测增加而增加, 从而检验模型是否存在自相关性.

对于这三种残差图, 希望看到残差随机分布, 且没有明显趋势, 并且尽量处于 $-2 \leq r_{SD_i} \leq 2$ 的范围内.

> [!note] Note: GLM residual plot interpretation
> 与 OLS 相比, GLM 的残差图解读不仅要看残差的位置, 还要看类别的分布.

#### 2.5.1 Partial Residual Plot

在正常的残差分析外, 若模型中含有连续解释变量, 则还可以通过 Partial Residual Plot 来检验模型拟合效果, 讨论其是否需要进行一些变换, 如对数变换或 Box-Cox 变换.

具体而言, 对于某个连续型解释变量 $X_j$, 其 partial residual 的定义为在正常的某种残差基础上加回该变量的影响.

**Definition (Partial Residual).**

$$
r_{\partial j} = \text{Working Residual} + \hat{\beta}_j X_j.
$$

Partial Residual Plot 的纵坐标是 partial residual, 横坐标是对应的解释变量. 这个图的分布趋势指示这个解释变量是否需要进行变换. 若其分布是线性的, 则说明模型拟合效果较好, 可以直接以线性形式加入模型. 若其分布是非线性的, 例如呈现出对数分布, 则说明该变量可能需要变换.

## 3. Binary GLM Applications: Bioassay and Epidemiology

### 3.1 Overview

本节介绍 GLM 在 Bioassay (生物测定) 与 Epidemiology (流行病学) 中的应用, 并以这两个应用场景为背景介绍一些统计技巧.

### 3.2 Bioassay

Bioassay 是一种用于测定生物活性的方法. 通俗而言, 实验者会对生物体施加一定浓度的药物, 然后观察生物体的反应, 如死亡率等. 通过这种方法, 可以得到药物的剂量-反应曲线, 从而得到药物的有效剂量 (ED) 等信息.

在处理 Bioassay 数据时, 有一个重要概念: **Tolerance Distribution**. 这里假定某个生物体对药物的承受上限 $U$ 是一个随机变量, 其分布为 $F(u)$. 对于某个给定剂量 $d_i$, 若 $d_i > U$, 则生物体会死亡. 因此, 死亡率 $\pi_i = \mathbb{P}(U<d_i) = F_X(x)$.

当假定 $U$ 服从特定分布时, 能得到 probit link 或 logit link 的 GLM 模型.

**Case (Normal tolerance distribution).** 若 $U\sim\mathcal{N}(\mu, \sigma^2)$:

- 死亡率 $\pi_i = \mathbb{P}(U<d_i) = \Phi\left(\frac{d_i-\mu}{\sigma}\right)$, 其中 $\Phi$ 是标准正态分布的分布函数.
- 对应 GLM:

  $$
  \text{probit}(\pi_i) = \Phi^{-1}(\pi_i) =\frac{d_i}{\sigma} - \frac{\mu}{\sigma} = \beta_0 + \beta_1 d_i.
  $$

**Case (Logistic tolerance distribution).** 若 $U\sim\text{Logistic}(\mu, \sigma)$:

- Logistic 分布的 pdf 为:

  $$
  f(u) = \frac{\exp\left(\frac{u-\mu}{\sigma}\right)}{\sigma \left(1+\exp\left(\frac{u-\mu}{\sigma}\right)\right)^2},
  $$

  其中 $\mu\in\mathbb{R}, \sigma>0$. 且有 $\mathbb{E}(U) = \mu$, $\text{Var}(U) = \frac{\pi^2}{3}\sigma^2$.

- 死亡率:

  $$
  \pi_i = \mathbb{P}(U<d_i) = \frac{\exp\left(\frac{d_i-\mu}{\sigma}\right)}{1+\exp\left(\frac{d_i-\mu}{\sigma}\right)}.
  $$

- 对应 GLM:

  $$
  \text{logit}(\pi_i) = \log\left(\frac{\pi_i}{1-\pi_i}\right) = \frac{d_i}{\sigma} - \frac{\mu}{\sigma} = \beta_0 + \beta_1 d_i.
  $$

综上, 在 Bioassay 中, Probit Link 是最常见的一种模型. 其分析的核心在于剂量与生物体 response 之间的关系.

#### 3.2.1 Beetles Dataset Workflow

Beetles 数据集包含 $n=8$ 个观测, 包含变量 `dose` (剂量), `death` (死亡数), `total` (总数). 目标是用 `dose` 预测死亡率. 假设 $Y_i \sim \text{Binomial}(m_i, \pi_i)$, 其中 $m_i$ 是总数, $\pi_i$ 是死亡率.

详细拟合流程结果见课件 Lecture 6, p. 7. 这里摘录主要步骤作为流程参考.

- 首先利用 logit link 拟合一个一次的无交互项模型:

  ```r
  fm1 <- glm(cbind(death, total-death) ~ dose, family = binomial(link = "logit"), data = beetles)
  ```

- 通过 `summary(fm1)` 可以得到模型拟合结果. 其 `Deviance = 11.23, df = 6`. 通过 `pchisq(11.23, 6, lower.tail = FALSE)` 可以得到 $P=0.08 > 0.05$, 因此这个模型是 adequate.
- 通过残差检验以及 `Dose` 的 Partial Residual Plot, 发现残差图具有二次型趋势, partial residual plot 也具有二次型趋势. 因此认为 `Dose` 需要引入更高阶项.
- 记引入直到 2 阶、3 阶的模型为 `fm2`, `fm3`. 通过 `pchiq()` 分别检验各自拟合是否 adequate. 结果展示这两个模型都是 adequate.
- 通过 `anova(fm1, fm2, fm3, test = "Chisq")` 进行 Drop-in-Deviance 检验. 发现二次项显著, 但三次项不显著. 因此认为直到二次项的 `fm2` 是一个最优模型.
- 经过残差检验, 发现残差图基本都是随机分布, 且没有明显趋势. Partial Residual Plot 也基本线性. 因此认为模型拟合效果较好.

> [!note] Note: Interpreting quadratic terms
> 在含有二次型的模型中, 例如 Beetles 数据中的最终模型 `y.Bin ~ Dose + I(Dose^2)`, 由于二次项存在, 无法再像之前那样按照类似边际效应的方式解释模型系数. 因此在这种模型的解读中, 更多考虑给定具体 `Dose` 取值下的死亡率或 odds, 而不讨论其边际效应.

#### 3.2.2 Lethal Dose

在 Bioassay 中, 一个重要指标是 Lethal Dose (LD), 即对应于某个死亡率的剂量. 若给定剂量与死亡率的关系为 $\pi_i = F(d_i)$, 则 $LD_X$ 即为使得 $\pi_i = X$ 的剂量. 通常关注 $LD_{50}$, 即使得死亡率为 50% 的剂量.

**Point estimation.** 以二次型为例, 假设模型为

$$
\zeta = \log\frac{\pi_i}{1-\pi_i} = \beta_0 + \beta_1 d_i + \beta_2 d_i^2.
$$

则有:

$$
\log\frac{0.5}{1-0.5} = \hat \beta_0 + \hat\beta_1 LD_{50} +\hat \beta_2 LD_{50}^2,
$$

从而可以解出 $LD_{50}$. 对于有多个根的情况, 在求解完后需要验证其是否落在剂量取值范围内.

更一般地应使用数值方法求解. 例如在 R 中, 可以通过 `uniroot()` 求解. 不论何种方法, 本质上都是在求解一个以模型系数为未知数的方程组. 当模型拟合完成后, 其各概率的 LD 值就已经确定, 即 $LD_X = h(\hat\beta)$.

**Interval estimation.** 区间估计的一般形式为:

$$
LD_X \in [h(\hat\beta) \pm z_{\alpha/2} \text{SE}(h(\hat\beta))].
$$

重点在于计算 $h(\hat\beta)$ 的标准误差. 一种统计学做法是 Delta Method.

- 假设 $\beta$ 是一维随机变量, 其均值为 $\mu$, 方差为 $\sigma^2$. 则对于可微函数 $g(\beta)$:

  $$
  \text{Var}(g(\beta)) \approx \left(\frac{\partial g}{\partial \beta}\right)^2 \text{Var}(\beta).
  $$

  若在大样本等情况下有近似正态分布, 则有:

  $$
  g(\hat \beta) \sim N(g(\mu), (g'(\mu))^2 \sigma^2).
  $$

- 若 $\beta\in\mathbb{R}^p$, 则有:

  $$
  \text{Var}(g(\beta)) \approx \nabla g(\beta)^\top \text{Var}(\beta) \nabla g(\beta),
  $$

  其中 $\nabla g(\beta) = \left(\frac{\partial g}{\partial \beta_1}, \cdots, \frac{\partial g}{\partial \beta_p}\right)^\top$.

  其大样本下的近似分布为:

  $$
  g(\hat \beta) \sim N(g(\mu), \nabla g(\mu) \text{Var}(\beta) \nabla g(\mu)^\top).
  $$

### 3.3 Epidemiology

Epidemiology 是研究人群中疾病发生因素等问题的学科. 主要有两种研究方法: **Cohort Study** 与 **Case-Control Study**.

#### 3.3.1 Cohort Study

- **Cohort Study** 是一种前瞻性的研究方法. 在研究开始时, 研究者选择一组无所研究疾病的人群, 并对其进行长期追踪. 在足够时间后, 统计研究人群中疾病的发生情况, 并与一些因素进行关联分析.
- Cohort Study 由于在研究开始时研究者并不知道疾病发生情况, 因此其研究结果比较可靠. **Cohort Study 可以用来估计某种因素暴露下的疾病发生率.**
- 但其研究周期长、成本高. 如果一些疾病非常罕见, 则可能需要很长时间才能得到足够数据.

在 Cohort Study 中, 通常会有三种基本变量:

- **Exposure Variable.** 暴露变量, 即研究者感兴趣的变量, 如吸烟、饮食习惯等.
- **Outcome Variable.** 结果变量, 即研究者感兴趣的结果, 如疾病发生情况.
- **Countervailing Variable.** 这类变量既与暴露变量相关, 如年龄、性别、社会地位等, 也与结果变量相关, 如年龄可能会影响疾病发生. 但本身不是暴露变量的结果, 因此不能作为中介变量. 同时由于其与结果也有因果关系, 因此不应该被忽略.

**Example (Framingham data).** Framingham data 是一个经典的 Cohort Study 数据集. 其包含一些变量, 如 `age`, `sex`, `chol`, `CHD`. 目标是用 `age`, `sex`, `chol` 来预测 `CHD` 的发生情况.

拟合细节省略, 详见课件 Lecture 6, p. 30. 这里强调两个重点方法: 利用 AIC 进行变量选择, 以及对交互项的模型解读.

**AIC for Model Selection.**

- AIC 是一种模型选择准则. 其定义为 $\text{AIC} = -2\log L + 2p$, 其中 $L$ 是似然函数的最大值, $p$ 是模型参数个数. **我们倾向于选择 AIC 最小的模型.**
- 在 R 中, 可以通过 `stepAIC()` 进行模型逐步选择.
  - `direction = "forward"` 表示从 Null Model 开始, 逐步添加变量.
  - `direction = "backward"` 表示从 Full Model 开始, 逐步删除变量.
  - `direction = "both"` 表示前向与后向结合, 在每一步都会考虑添加或删除变量.
- `stepAIC()` 的结果可能受到初始模型影响. 因此使用时应多次尝试不同初始模型, 并选择几个最终模型中 AIC 最小的那个.
- 对于参数变量较多的模型, 可以通过 `stepAIC()` 进行基本变量选择. 但由于 AIC 依然倾向于选择参数较多的模型, 因此在 AIC 选择后, 还可以通过 `drop1()` 等函数进行进一步变量选择, 或使用 `add1()`, `anova()`.

**Interpretation of Interaction Terms.** 在本例中, 最终选择的模型为 `CHD ~ sex + age + chol + age:chol + sex:age`. 其对应的系数为:

```r
> coef(fm)
(Intercept)     sexmale     age50-62 chol>250
-4.55797135 1.36270131 1.99405104 1.54451751
chol190-219 chol220-249 age50-62:chol>250 age50-62:chol190-219
0.05637924 0.92448432 -0.87779164 0.22973705
age50-62:chol220-249 sexmale:age50-62
-0.55866803 -0.57195686
```

注意到在这个模型中, 有两个交互项: `age:chol` 与 `sex:age`. 这说明 `CHD` 和 `chol` 的关联对于不同年龄段是不同的, 但这种关联对于不同性别是基本相同的, 因为 `sex:chol` 并不显著.

在解释含有交互项的模型时, 要说全所有变量类别, 并且注意交互项“且”的关系. 例如:

- `chol>250: 1.469` 表示: 对于两个性别相同的个体, 对于胆固醇水平大于 250 的个体, 其发生心脏疾病的 odds 是胆固醇水平小于 250 的个体的 $e^{1.469}$ 倍, 如果这两个个体的年龄在 30-49 岁之间.
- `age50-62:chol>250: -0.877` 表示: 对于两个性别相同的个体, 对于胆固醇水平大于 250 的个体, 其发生心脏疾病的 odds 是胆固醇水平小于 250 的个体的 $e^{-0.877 + 1.469}$ 倍, 如果这两个个体的年龄在 50-62 岁之间.

#### 3.3.2 Case-Control Study

**Case-Control Study** 是一种回顾性的研究方法. 在研究开始时, 研究者会在已经发生疾病的人群中抽取一部分样本 (case), 并在没有发生疾病的人群中抽取一部分样本 (control). 然后对这两部分样本进行比较.

- 在抽样时, 是否暴露于某种因素不应该影响研究者的选择. 因此抽样时应该采用随机方法.
- 由于 Case-Control Study 是回顾性的, 因此其结果可能受到一些偏差影响. 但由于研究周期短、成本低, 因此在一些情况下适用.
- Case-Control Study 的抽样存在偏差. 其研究对象中发生疾病的群体比例往往远高于整个人群中的比例. 因此 **Case-Control Study 不可以用来估计疾病发生率**.
  - Case-Control 可以估计: 在给定发病的情况下, 某种因素的暴露率.
  - Case-Control 不可以估计: 在给定暴露的情况下, 某种疾病的发生率.

由于上述原因, 疾病发病的 odds 不可以直接估计. 其具体数学推导见课件 Lecture 7, p. 10.

Case-Control Study 的可行研究对象为 odds ratio (OR) 或 relative risk (RR).

- **OR.**

  $$
  OR = \frac{odds_{\text{exposed}}}{odds_{\text{unexposed}}} = \frac{p_0(x_1) / (1-p_0(x_1))}{p_0(x_0) / (1-p_0(x_0))}.
  $$

  其中 $p_0(X)$ 表示在观测到的样本中, 暴露于 $X$ 的个体患病的概率.

- **RR.**

  $$
  RR = OR \frac{1 - p(x_1)}{1 - p(x_0)}.
  $$

  其中 $p(X)$ 表示在整个人群中, 暴露于 $X$ 的个体患病的概率. 若该疾病发生率很低, 则有 $RR \approx OR$.

**Example (Cervical Cancer data).** 假设只考虑是否患病与 `age` (<= 或 > 15 岁) 之间的关系. 给定最终拟合模型为:

```r
> (fm <- glm(cbind(cases, controls) ~ age, dat, family="binomial"))
Call: glm(formula = cbind(cases, controls) ~ age, family = "binomial",
data = dat)
Coefficients:
(Intercept) age<=15
-2.156 1.383
Degrees of Freedom: 1 Total (i.e. Null); 0 Residual
Null Deviance: 15.39
Residual Deviance: 2.864e-14 AIC: 13.19
```

其中 `age<=15` 的系数为 `1.383`. 这说明: 在 `age<=15` 的个体中, 患病的 odds 是在 `age>15` 的个体中患病的 $e^{1.383}$ 倍. 虽然这里说的是患病 odds, 但其本质上是在比较 odds ratio, 因此这里的解释是合理的.

如果可以认为疾病发生率很低, 则有

$$
RR \approx OR = e^{1.383} = 3.98.
$$

这说明: 在 `age<=15` 的个体中, 患病的相对风险是在 `age>15` 的个体中患病的 $3.98$ 倍.

补充: 在本例中, $\hat\beta_j$ 相当于是 log odds ratio. 因此在解释时常通过取指数来得到 odds ratio. 这是点估计的解释. 对于区间估计, 若想求解一个 odds ratio 的区间估计, 则可以先求 log odds ratio, 即 $\hat\beta_j$, 的置信区间 $CI$, 然后再通过对区间两端取指数来得到 odds ratio 的区间估计:

$$
CI_{OR} = [e^{CI_{\hat\beta_j}}].
$$

## Related Notes

- [Linear Models for Classification](../Classification/Linear-Models-for-Classification.md)
- [Naive Bayes Classifier](../Classification/Naive-Bayes-Classifier.md)
- [Statistical Inference](../../StatisticalInference/)
