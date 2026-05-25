import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

const explorerGroups = [
  {
    title: "STAT Foundations and More ...",
    slug: "StatFoundationsMore",
    children: [
      "ProbabilityTheory",
      "ComputationalStatistics",
      "StatisticalInference",
      "StochasticProcess",
    ],
  },
  {
    title: "Optimization",
    slug: "Optimization",
    children: ["ConvexOptimization", "OnlineLearning"],
  },
  {
    title: "Machine Learning and AI",
    slug: "MachineLearningAI",
    children: ["StatisticalLearningAlgorithms", "DeepLearning", "NLPAndLLMs"],
  },
]

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
      "Discord Community": "https://discord.gg/cRFFHYye7t",
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
    Component.PageTitle(),
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
