import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/ask.scss"
// @ts-ignore
import script from "./scripts/ask.inline"
import { classNames } from "../util/lang"

export interface AskOptions {
  endpoint: string
}

const defaultOptions: AskOptions = {
  endpoint: process.env.QA_BACKEND_URL || "http://localhost:7860/api/qa",
}

export default ((userOpts?: Partial<AskOptions>) => {
  const Ask: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
    const opts = { ...defaultOptions, ...userOpts }

    return (
      <div class={classNames(displayClass, "ask")} data-endpoint={opts.endpoint}>
        <button class="ask-button" aria-label="Ask BYNotes">
          <svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <title>Ask BYNotes</title>
            <path d="M5 5.75A2.75 2.75 0 0 1 7.75 3h8.5A2.75 2.75 0 0 1 19 5.75v5.5A2.75 2.75 0 0 1 16.25 14H11l-4.2 4.2A1.05 1.05 0 0 1 5 17.46V14.1A2.75 2.75 0 0 1 2.5 11.36V5.75H5Zm2.75-1.25A1.25 1.25 0 0 0 6.5 5.75v12.11l3.66-3.66c.2-.2.47-.31.75-.31h5.34a1.25 1.25 0 0 0 1.25-1.25V5.75a1.25 1.25 0 0 0-1.25-1.25h-8.5ZM8 7.4h8v1.4H8V7.4Zm0 3h5.9v1.4H8v-1.4Z" />
          </svg>
          <p>Ask</p>
        </button>
        <div class="ask-container" role="dialog" aria-modal="true" aria-label="Ask BYNotes">
          <div class="ask-space">
            <form class="ask-form">
              <input
                autocomplete="off"
                class="ask-input"
                name="question"
                type="text"
                aria-label="Question"
                placeholder="Ask BYNotes..."
                maxlength={600}
              />
              <button class="ask-submit" type="submit" aria-label="Submit question">
                <svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <title>Submit</title>
                  <path d="M3.42 20.19 21.4 12 3.42 3.81 3 10.17 14.7 12 3 13.83l.42 6.36Z" />
                </svg>
              </button>
            </form>
            <div class="ask-layout" aria-live="polite">
              <div class="ask-status"></div>
              <div class="ask-answer"></div>
              <div class="ask-sources"></div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  Ask.afterDOMLoaded = script
  Ask.css = style

  return Ask
}) satisfies QuartzComponentConstructor<Partial<AskOptions> | undefined>
