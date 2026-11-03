# Decision Theory — release review (2026-11-04)

User authorized minimal mathematical corrections and direct publication. The Obsidian original remains unchanged. PDF and HTML are generated from the same corrected edition.

## Content changes

| Source line | Correction                 | Reason                                                                                                                 |
| ----------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 354         | `transitivity-menu`        | 反设针对 {x,z}；此步应用 WARP 的两个菜单也包含 {x,z}。                                                                 |
| 550         | `utility-order-symbol`     | U 的值是实数，用 >；偏好符号用于 lottery。                                                                             |
| 774         | `expected-utility-example` | 按给定概率重新计算 sqrt 的期望；保留原例，不再把这个 FOSD 例子当成均值排序失效的反例。U 已是期望效用，删除多余外层 E。 |
| 788         | `fosd-cdf-direction`       | 生存函数更高对应 CDF 更低。                                                                                            |
| 1158        | `risk-aversion-direction`  | 更风险厌恶的决策者 1 接受的确定性替代集合更大，与 CE_1 <= CE_2 一致。                                                  |
| 1168        | `weak-concavity`           | 命题使用弱风险厌恶比较和 >=，必须允许线性的 phi（相同风险态度）。                                                      |
| 1223        | `cara-sign-and-domain`     | 由 exp(-a CE)=E exp(-a Z) 解出，负号必要；对数表达式只适用于 a>0。                                                     |
| 1250        | `crra-quantifier`          | CRRA 固定风险参数 gamma，对所有正财富 z 要求系数恒定。                                                                 |
| 1178        | `typo-wuyi`                | 明显错字。                                                                                                             |
| 1178        | `typo-shitu`               | 明显错字。                                                                                                             |
| 1234        | `typo-yanwu`               | 明显错字。                                                                                                             |
| 1499        | `typo-regularity`          | 英文拼写。                                                                                                             |
| 415         | `axiom-equivalence-label`  | 本命题的证明逐项证明 WARP 与 alpha+beta 等价；原第 (2) 项重复效用表示。                                                |
| 432         | `counterexample-direction` | 正文反例满足 alpha+beta 却不满足 WARP，标题的蕴含方向反了。                                                            |
| 1308        | `rum-smaller-menu`         | 本段已把菜单缩为 B，0.9 和 0.1 对应 B 上的选择概率。                                                                   |
| 504         | `lottery-normalization`    | 示例概率和为 1.1；保留前两个数，将末项改为剩余概率 0.3。                                                               |

Exact before/after strings and expected occurrence counts are versioned in [the correction ledger](../../scripts/latex-notes/decision-theory-corrections.json). Template-only changes (counter labels and fixed date) are separate from these content corrections.

## Verification

- Original main.tex SHA-256: `b587980e8fde0642cf3baaa9779d510280fead2bbc927f1919b8e89be495b547`.
- Corrected edition SHA-256: `fae60c82d8ac5326cd33808d5d31a36e3fbccdf13798d8cb9b15fdddd5ef786b`.
- 1186 rendered expressions, zero KaTeX errors; 55 content blocks, 19 proofs, 16 footnotes, two tables, three SVG diagrams.
- Source structure/prose checks and seven PDF/web label comparisons pass.
- Eight parser tests and four correction tests pass; the latter check arithmetic, CARA certainty equivalence, implication direction, and refusal of stale/ambiguous correction contexts.
- Entire 136-page Markdown input builds; home Recent Updates retains exactly three entries; topic index, Quick Guide and Economics sidebar group are wired.
- Desktop and 375px clipping checks pass, excluding the deliberately hidden KaTeX MathML accessibility layer. The pre-existing mobile top-bar width issue is outside this note change.
- Corrected PDF pages were visually compared with the HTML. PDF remains 25 pages, with no overfull boxes or undefined references.
- Production CI and live HTTP checks are performed after pushing the release commit.

## Scope and limitations

- This is a rendering/publication pass with narrowly authorized corrections, not a complete mathematical audit. Incomplete original arguments are not expanded.
- Lemma 2.1.1 uses p_i/q_i and alpha_i in ways that mix lottery components and mixture weights; resolving the intended statement would require a larger rewrite, so it is retained for author review.
- The source’s informal GARP “no cycle” explanation should be read alongside its formal axiom; a fuller distinction between weak cycles and strict revealed preference is outside this small correction pass.
- Mathematical glyphs use KaTeX on the web; the documented mathds-to-mathbb glyph substitution remains.
- Full tsc includes an existing archived backup with missing imports. Active-source checks exclude that backup; production CI is the release build gate.

## Rebuild

Use the manifest in `scripts/latex-notes/decision-theory.json`; its `corrections` field applies the reviewed ledger before generating either edition. If the author edits the original, explicitly review/rebase the ledger rather than bypass its source hash check.
