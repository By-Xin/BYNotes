# Release review — Deterministic Operational Research (SJTU, 2026)

Date: 2026-11-06. Publication and minimal corrections explicitly authorized by
Baiying. This includes the later clarification: web typography only; keep
fonts inside environments, and keep PDF font size/line spacing unchanged.

## Source and fidelity

The complete 1,312-line original was reviewed. Its byte-identical snapshot is
[`original.md`](../../sources/deterministic-operational-research/original.md),
SHA-256 `8464144490b01b27dd3baebbf30d99c9a4aca9f9dc9d5bafc397b4e1c0156fb0`.
The Obsidian file remains byte-identical. Revised source and full exact changes:
[`revised.md`](../../sources/deterministic-operational-research/revised.md),
[`corrections.patch`](../../sources/deterministic-operational-research/corrections.patch),
[`corrections.json`](../../sources/deterministic-operational-research/corrections.json).

93 replacement operations correct quantifiers/assumptions, dimensions, algebra,
inequality directions, mistaken uniqueness claims, terminology and clear typos.
Several operations may address a single original line. No new section,
exposition, proof completion, reference or diagram was added to the lecture.
The changes below are the user's authorized revision pass, distinct from
representation-only conversion. Every exact before/after is in the linked ledger.

## Representation and template

- Clean, complete `main.tex`, using the Decision Theory XeLaTeX template.
- 98 semantic blocks: 37 definitions, 15 theorems, 12 propositions, 6 corollaries,
  1 lemma, 6 examples, 2 remarks, and 19 proof/sketch environments.
- All 1,409 remaining math expressions preserved in order; all 15 original
  QED markers retained at proof ends. Four sketches/proofs without an original
  QED use `proof*`; no end marker was invented.
- All 18 image occurrences preserved (17 unique original PNGs), now local;
  image checksums and dimensions recorded. No diagram redrawing.
- Sections retain source order. Duplicate 2.4 numbering repaired; block labels
  use subsection counters. References and the original commented-out reference
  table remain. Six quotes, 89 itemize and 8 enumerate environments retained.
- Template-only changes: title/byline/date, reference-counter repair, braces
  around comma-containing box titles, an unnumbered no-QED proof variant,
  omission of an unused bibliography resource, and a six-line minimum before
  splitting an example box. The last change prevents orphan example titles.
- PDF stays 11pt with the template's `linespread=1.3`; 44 pages. Source ZIP
  contains the 21 files used to compile it, checked byte-for-byte.

## Web typography for both articles

The opt-in `latex-note` profile applies to this article and Decision Theory.
Normal paragraphs use the site's sans-serif family (Source Sans Pro with
system sans-serif CJK fallback); statement bodies retain Termes/Kai, proofs
retain Termes/Song, and headings retain Pagella/Song. Body size is 17→16px on
desktop and 16→15px on mobile; fixed heading/edition text sizes also step down
1px. Paragraph line-height multipliers are reduced by exactly 15% (1.85→1.5725;
nested paragraphs 1.68→1.428). Font resizing additionally affects pixel height.
Other Markdown articles and site navigation retain their typography.
Decision Theory Markdown, source and PDF were not regenerated or edited.
Font subsets were regenerated from the union of both reviewed TeX sources.

## Validation

- 18 focused parser/correction/algebra tests pass.
- Markdown import preservation audit and independent TeX→HTML audit pass;
  595 prose chunks checked, 82 anchor links checked, no duplicate IDs or
  missing local images, zero KaTeX errors. No original `\label`/`\ref` pairs
  exist in this lecture; the zero label-match count is expected.
- Full-site build: 138 content files, 867 emitted files. The first `npx`
  invocation could not write the sandboxed npm cache; running the already
  installed `node quartz/bootstrap-cli.mjs` entrypoint completed successfully.
- PDF: reviewed the 44-page contact sheets and full-size representative pages,
  all original diagrams, and all four pages affected by the page-break repair.
  No text outside page bounds, missing glyphs, overfull boxes or unresolved
  references in the final TeX pass. Harmless inherited notices: biblatex's
  fallback backend, unavailable Fandol bold-italic shape substitution, and two
  source `\small` commands inside math mode. Source math styling was preserved.
- Browser: both articles checked at 1280px and 375px; no visible article content
  hidden/clipped (KaTeX's intentionally hidden accessibility MathML excluded).
  Confirmed sans-serif ordinary body and unchanged environment font families.
  Operational Research light/dark checked, proof open/close checked, wide
  display formula scrollLeft changed 0→40 via actual keyboard interaction.
  Decision Theory footnote jumps and return links checked. Standalone reading
  edition's native TOC navigation and PDF/source paths checked. Full-site mobile menu was collapsed
  for reading; existing off-screen site UI can contribute to root scrollWidth,
  but the article fits its viewport and its wide content has scroll containers.
- New topic index, homepage Quick Guide and OPTIMIZATION explorer entry are
  synchronized. Recent Updates contains exactly three entries.

## Scope limits retained

The original finite-dimensional separation proof is still a sketch invoking
relative-interior separation; it has not been expanded into a standalone proof.
The projection-distance proof's original scope is retained rather than adding
missing expository derivations. Informal geometric explanations remain in the
author's wording. Rendering/preservation tests do not certify every textbook
attribution or replace peer review.

## Revision index

Source lines refer to the original Markdown. See the exact ledger/diff above
for the complete before/after text of every operation.

| ID | Original line | Reason |
| --- | ---: | --- |
| OR-01 | 40 | 局部最优需要存在邻域半径 |
| OR-02 | 40 | 严格局部最优的比较范围也是邻域 |
| OR-03 | 40 | 孤立局部最优是邻域性质；strong 并非统一同义术语 |
| OR-04 | 138 | 两两不共线不足以推出多个向量线性无关 |
| OR-05 | 167 | SOC 右侧 c 与 x 维数必须一致 |
| OR-06 | 193 | 仿射原像的目标集合位于 R^m |
| OR-07 | 242 | 紧性不保证整个算法点列收敛 |
| OR-08 | 280 | 缺字 |
| OR-09 | 282 | 空集紧不能证明最优解存在 |
| OR-10 | 288 | 多余编辑符号 |
| OR-11 | 290 | 扩展实数下确界总存在，需要证有限性 |
| OR-12 | 291 | 量词对象误写 |
| OR-13 | 322 | 拼写 |
| OR-14 | 338 | 对应实际代数操作 |
| OR-15 | 340 | 投影唯一性证明遗漏共同最优距离平方 |
| OR-16 | 346 | 平方展开交叉项系数应为 1/2 |
| OR-17 | 347 | 配套使用正确内积上界得到严格小于最优距离平方 |
| OR-18 | 386 | 除以 t 前需消去常数项 |
| OR-19 | 414 | 法锥不限制权重和为 1 |
| OR-20 | 414 | 指向外部不是法向量的充分条件 |
| OR-21 | 429 | 支持平面不会切开凸集 |
| OR-22 | 486 | 极锥属于集合而非某个点 |
| OR-23 | 511 | 修复重复小节编号并顺延 |
| OR-24 | 553 | 修复重复小节编号并顺延 |
| OR-25 | 611 | 修复重复小节编号并顺延 |
| OR-26 | 643 | 修复重复小节编号并顺延 |
| OR-27 | 613 | 确保 prox 和 Moreau 的 argmin 存在且唯一的原稿缺失前提 |
| OR-28 | 619 | 指标函数凸性及投影光滑性所需前提 |
| OR-29 | 641 | 排除边界处指标函数不可微情况 |
| OR-30 | 650 | 垂足在边界才推出等式 |
| OR-31 | 670 | 拼写 |
| OR-32 | 672 | 拼写 |
| OR-33 | 695 | 拼写 |
| OR-34 | 682 | 错字 |
| OR-35 | 745 | 闭凸集的差不一定闭 |
| OR-36 | 759 | 常值结论只针对该集合 |
| OR-37 | 768 | 平行线段有多个最近点对，但差向量唯一 |
| OR-38 | 786 | 点集强分离的闭性条件，与下方证明一致 |
| OR-39 | 786 | 归一化保证非零极限；修正紧性措辞及错字 |
| OR-40 | 806 | 闭凸集是支持半空间交而非超平面交 |
| OR-41 | 829 | 闭凸集是支持半空间交而非超平面交 |
| OR-42 | 824 | 未取得的 support supremum 不产生相交支持平面 |
| OR-43 | 837 | 统一前文以 simplex 维数作下标的约定 |
| OR-44 | 883 | 使用标准 max 对偶变量取负后的等价 min 形式，与后文负证书一致 |
| OR-45 | 881 | 说明对偶变号，避免误称标准对偶 |
| OR-46 | 885 | 逻辑否定符误写 |
| OR-47 | 895 | 负证书证明不可行 |
| OR-48 | 909 | 状态价格一般不是总和为 1 的概率 |
| OR-49 | 907 | 明确本例采用的较窄套利概念，避免混同完整无套利定理 |
| OR-50 | 916 | 择一系统不是逻辑等价 |
| OR-51 | 917 | 择一系统不是逻辑等价 |
| OR-52 | 918 | 择一系统不是逻辑等价 |
| OR-53 | 918 | 齐次变体遗漏 RHS 为零，否则所述证书不成立 |
| OR-54 | 925 | 任意集合元素不足以证明给定 b 的归属性 |
| OR-55 | 930 | 任意外点的严格分离需闭性 |
| OR-56 | 971 | 修正择一系统 RHS，与后续证明一致 |
| OR-57 | 987 | 同步修正题设回指 |
| OR-58 | 1013 | 圆盘内部不是极点 |
| OR-59 | 1021 | 实数空间符号误写 |
| OR-60 | 1063 | basic solution 不要求可行，与后句一致 |
| OR-61 | 1063 | 拼写 |
| OR-62 | 1144 | 错字 |
| OR-63 | 1169 | 错字 |
| OR-64 | 1169 | 退化定义的对象需为基解 |
| OR-65 | 1202 | 正 slack 给正步长，并排除除零 |
| OR-66 | 1208 | 无直线只保证至少一侧受阻 |
| OR-67 | 1237 | 最优值不是最优点集合 |
| OR-68 | 1237 | 最优解集合非空来自最优解存在 |
| OR-69 | 1238 | 凸组合等值推导需要同时用两个最优性不等式 |
| OR-70 | 1250 | 应垂直于活跃法向量而非点 x |
| OR-71 | 1251 | 无界下降存在更优点，原句结论相反 |
| OR-72 | 1255 | 无直线只保证一侧受阻并修正错字 |
| OR-73 | 1258 | 索引 argmin 不是向量 |
| OR-74 | 1262 | 上文最优极点定理的前提 |
| OR-75 | 1269 | 衰退锥所列等价式需要非空 |
| OR-76 | 1278 | 非零性及 pointed 前提，避免零向量和仅至少 n-1 的歧义 |
| OR-77 | 1280 | 原点不是射线方向 |
| OR-78 | 1280 | 点是射线的生成方向 |
| OR-79 | 1284 | 无下界的最优值为负无穷，而不存在最优解 |
| OR-80 | 1286 | 无下界的最优值为负无穷，而不存在最优解 |
| OR-81 | 1288 | 无下界的最优值为负无穷，而不存在最优解 |
| OR-82 | 1289 | 无下界的最优值为负无穷，而不存在最优解 |
| OR-83 | 1295 | 无下界的最优值为负无穷，而不存在最优解 |
| OR-84 | 1290 | 拼写 |
| OR-85 | 1291 | 区分截面与锥的活跃约束 |
| OR-86 | 1310 | 含直线的多面体可能没有极点，保留一般 H/V 等价而修正极点限定 |
| OR-87 | 404 | 并非所有指向外部的向量都是法向量 |
| OR-88 | 412 | 内部点仍可用长向量指向外部，但没有非零法向量 |
| OR-89 | 470 | 切向极限不一定是可行方向 |
| OR-90 | 478 | 与下方圆盘切向例子一致 |
| OR-91 | 484 | 外部方向不足以刻画极锥 |
| OR-92 | 1306 | 一般多面体可能没有顶点 |
| OR-93 | 1310 | 一般 H/V 表示中的生成点不必是极点 |
