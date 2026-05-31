import { Element, Root } from "hast"
import { QuartzTransformerPlugin } from "../types"
import { visit } from "unist-util-visit"

type NotebookKind = "in" | "out" | "error"

const notebookMetaRegex = /(?:^|\s)nb-(in|out|error)(?:=([^\s]+))?(?:\s|$)/

function findCodeElement(node: Element): Element | undefined {
  if (node.tagName === "code") {
    return node
  }

  for (const child of node.children) {
    if (child.type === "element") {
      const match = findCodeElement(child)
      if (match) {
        return match
      }
    }
  }

  return undefined
}

function getNotebookMeta(
  node: Element,
): { kind: NotebookKind; executionCount: string } | undefined {
  const code = findCodeElement(node)
  const meta = code?.data?.meta
  if (typeof meta !== "string") {
    return undefined
  }

  const match = meta.match(notebookMetaRegex)
  if (!match) {
    return undefined
  }

  return {
    kind: match[1] as NotebookKind,
    executionCount: match[2] ?? "",
  }
}

function promptLabel(kind: NotebookKind, executionCount: string) {
  const count = executionCount.trim()
  const bracketedCount = count.length > 0 ? count : " "

  if (kind === "in") {
    return `In [${bracketedCount}]`
  }

  if (kind === "error") {
    return `Error [${bracketedCount}]`
  }

  return `Out [${bracketedCount}]`
}

export const NotebookCells: QuartzTransformerPlugin = () => {
  return {
    name: "NotebookCells",
    htmlPlugins() {
      return [
        () => {
          return (tree: Root) => {
            visit(tree, "element", (node, index, parent) => {
              if (
                index === undefined ||
                parent === undefined ||
                (parent.type !== "root" && parent.type !== "element") ||
                node.properties?.["data-notebook-cell"] !== undefined
              ) {
                return
              }

              if (node.tagName !== "figure" && node.tagName !== "pre") {
                return
              }

              if (
                node.tagName === "pre" &&
                parent.type === "element" &&
                parent.tagName === "figure"
              ) {
                return
              }

              const notebookMeta = getNotebookMeta(node)
              if (!notebookMeta) {
                return
              }

              const roleClass =
                notebookMeta.kind === "in"
                  ? "notebook-input"
                  : notebookMeta.kind === "error"
                    ? "notebook-error"
                    : "notebook-output"

              const wrapper: Element = {
                type: "element",
                tagName: "div",
                properties: {
                  className: ["notebook-cell", roleClass],
                  "data-notebook-cell": "",
                  "data-notebook-kind": notebookMeta.kind,
                },
                children: [
                  {
                    type: "element",
                    tagName: "div",
                    properties: {
                      className: ["notebook-prompt"],
                      ariaHidden: "true",
                    },
                    children: [
                      {
                        type: "text",
                        value: promptLabel(notebookMeta.kind, notebookMeta.executionCount),
                      },
                    ],
                  },
                  {
                    type: "element",
                    tagName: "div",
                    properties: {
                      className: ["notebook-body"],
                    },
                    children: [node],
                  },
                ],
              }

              parent.children[index] = wrapper
            })
          }
        },
      ]
    },
  }
}
