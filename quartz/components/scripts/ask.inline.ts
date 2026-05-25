import { registerEscapeHandler, removeAllChildren } from "./util"

type QASource = {
  title: string
  url: string
  score?: number
  snippet?: string
}

type QAResponse = {
  answer?: string
  mode?: string
  model?: string
  sources?: QASource[]
  error?: string
}

const maxVisibleSources = 5

function textEl<K extends keyof HTMLElementTagNameMap>(tag: K, className: string, text: string) {
  const el = document.createElement(tag)
  el.className = className
  el.textContent = text
  return el
}

function renderAnswer(container: HTMLElement, answer: string) {
  removeAllChildren(container)
  const paragraphs = answer
    .split(/\n{2,}/)
    .map((part) => part.trim())
    .filter(Boolean)

  for (const paragraph of paragraphs.length ? paragraphs : [answer]) {
    container.appendChild(textEl("p", "ask-answer-paragraph", paragraph))
  }
}

function renderSources(container: HTMLElement, sources: QASource[]) {
  removeAllChildren(container)
  if (!sources.length) return

  container.appendChild(textEl("h3", "ask-sources-title", "Sources"))
  const list = document.createElement("ol")
  list.className = "ask-source-list"

  for (const source of sources.slice(0, maxVisibleSources)) {
    const item = document.createElement("li")
    const link = document.createElement("a")
    link.href = source.url
    link.textContent = source.title
    link.target = "_blank"
    link.rel = "noreferrer"
    item.appendChild(link)

    if (source.snippet) {
      item.appendChild(textEl("p", "ask-source-snippet", source.snippet))
    }

    list.appendChild(item)
  }

  container.appendChild(list)
}

function setStatus(statusEl: HTMLElement, message: string, tone: "idle" | "error" = "idle") {
  statusEl.textContent = message
  statusEl.dataset.tone = tone
}

function setupAsk(askElement: Element) {
  if (typeof window.addCleanup !== "function") return
  if (!(askElement instanceof HTMLElement)) return
  if (askElement.dataset.askInitialized === "true") return
  askElement.dataset.askInitialized = "true"

  const endpoint = (askElement as HTMLElement).dataset.endpoint
  const button = askElement.querySelector(".ask-button") as HTMLButtonElement | null
  const container = askElement.querySelector(".ask-container") as HTMLElement | null
  const input = askElement.querySelector(".ask-input") as HTMLInputElement | null
  const form = askElement.querySelector(".ask-form") as HTMLFormElement | null
  const submit = askElement.querySelector(".ask-submit") as HTMLButtonElement | null
  const layout = askElement.querySelector(".ask-layout") as HTMLElement | null
  const status = askElement.querySelector(".ask-status") as HTMLElement | null
  const answer = askElement.querySelector(".ask-answer") as HTMLElement | null
  const sources = askElement.querySelector(".ask-sources") as HTMLElement | null

  if (!endpoint || !button || !container || !input || !form || !submit || !layout || !status) {
    return
  }

  if (!answer || !sources) return

  const qaEndpoint = endpoint
  const askButton = button
  const askContainer = container
  const askInput = input
  const askForm = form
  const askSubmit = submit
  const askLayout = layout
  const askStatus = status
  const askAnswer = answer
  const askSources = sources

  function openAsk() {
    askContainer.classList.add("active")
    askInput.focus()
  }

  function closeAsk() {
    askContainer.classList.remove("active")
    askButton.focus()
  }

  async function submitQuestion(event: Event) {
    event.preventDefault()
    const question = askInput.value.trim()
    if (!question) {
      setStatus(askStatus, "Question required.", "error")
      return
    }

    askSubmit.disabled = true
    askInput.disabled = true
    askLayout.classList.add("display-results")
    setStatus(askStatus, "Searching BYNotes...")
    removeAllChildren(askAnswer)
    removeAllChildren(askSources)

    try {
      const response = await fetch(qaEndpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      })
      const data = (await response.json()) as QAResponse

      if (!response.ok) {
        throw new Error(data.error || `Request failed with ${response.status}`)
      }

      setStatus(askStatus, data.mode === "llm" ? "Answer" : "Retrieved context")
      renderAnswer(askAnswer, data.answer || "No answer returned.")
      renderSources(askSources, data.sources || [])
    } catch (error) {
      setStatus(
        askStatus,
        error instanceof Error ? error.message : "QA backend unavailable.",
        "error",
      )
    } finally {
      askSubmit.disabled = false
      askInput.disabled = false
      askInput.focus()
    }
  }

  askButton.addEventListener("click", openAsk)
  askForm.addEventListener("submit", submitQuestion)
  registerEscapeHandler(askContainer, closeAsk)

  window.addCleanup(() => askButton.removeEventListener("click", openAsk))
  window.addCleanup(() => askForm.removeEventListener("submit", submitQuestion))
}

function setupAllAsk() {
  if (typeof window.addCleanup !== "function") return

  for (const askElement of document.getElementsByClassName("ask")) {
    setupAsk(askElement)
  }
}

function setupAllAskWhenReady(attempt = 0) {
  if (typeof window.addCleanup === "function") {
    setupAllAsk()
    return
  }

  if (attempt < 20) {
    window.setTimeout(() => setupAllAskWhenReady(attempt + 1), 25)
  }
}

setupAllAskWhenReady()
document.addEventListener("nav", setupAllAsk)
