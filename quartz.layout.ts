import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

const explorerGroups = [
  {
    title: "STAT FOUNDATIONS AND MORE",
    slug: "StatFoundationsMore",
    children: [
      "ProbabilityTheory",
      "ComputationalStatistics",
      "StatisticalInference",
      "StochasticProcess",
    ],
  },
  {
    title: "OPTIMIZATION",
    slug: "Optimization",
    children: ["ConvexOptimization", "OnlineLearning", "BilevelOptimization"],
  },
  {
    title: "MACHINE LEARNING AND AI",
    slug: "MachineLearningAI",
    children: [
      "StatisticalLearningAlgorithms",
      "UnderstandingMachineLearning",
      "DeepLearning",
      "NLPAndLLMs",
    ],
  },
  {
    title: "PAPER READING",
    slug: "PaperReadingGroup",
    children: ["OptimizationReadings"],
  },
  {
    title: "ODDS & ENDS",
    slug: "OddsEnds",
    children: ["LearningRoadmaps"],
  },
]

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [
    // Giscus comments (GitHub Discussions on By-Xin/BYNotes). Runtime requests
    // to giscus.app are a deliberate, notes-only exception to the no-third-party
    // policy; readers need a GitHub login and mainland access may be flaky.
    // Rendered on real note pages only — not on the home, folder/topic index,
    // tag, or 404 pages.
    Component.ConditionalRender({
      component: Component.Comments({
        provider: "giscus",
        options: {
          repo: "By-Xin/BYNotes",
          repoId: "R_kgDORP_CQQ",
          category: "Announcements",
          categoryId: "DIC_kwDORP_CQc4DAv1F",
          mapping: "pathname",
          strict: true,
          reactionsEnabled: true,
          inputPosition: "bottom",
          themeUrl: "https://giscus.app/themes",
          lightTheme: "light",
          darkTheme: "dark",
          lang: "zh-CN",
        },
      }),
      condition: (page) => {
        const slug = page.fileData.slug ?? ""
        return (
          slug !== "index" &&
          slug !== "404" &&
          !slug.endsWith("/index") &&
          !slug.startsWith("tags/")
        )
      },
    }),
  ],
  footer: Component.Footer({
    links: {
      Homepage: "https://by-xin.github.io",
      GitHub: "https://github.com/By-Xin/BYNotes",
      RSS: "https://by-xin.github.io/BYNotes/index.xml",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.Flex({
      components: [
        { Component: Component.PageTitle(), grow: true, justify: "start" },
        { Component: Component.HomeBackLink(), shrink: false },
      ],
      gap: "0.8rem",
    }),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      groups: explorerGroups,
    }),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      groups: explorerGroups,
    }),
  ],
  right: [],
}
