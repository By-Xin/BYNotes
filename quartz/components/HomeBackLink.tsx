import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const HomeBackLink: QuartzComponent = ({ fileData }: QuartzComponentProps) => {
  if (fileData.slug !== "index") {
    return null
  }

  return (
    <a
      class="home-back-link"
      href="https://by-xin.github.io/"
      aria-label="Back to personal homepage"
    >
      <span aria-hidden="true">←</span>
      <span>Home</span>
    </a>
  )
}

HomeBackLink.css = `
.home-back-link {
  align-items: center;
  border: 1px solid var(--lightgray);
  border-radius: 6px;
  color: var(--secondary);
  display: inline-flex;
  font-family: var(--headerFont);
  font-size: 0.86rem;
  font-weight: 700;
  gap: 0.28rem;
  line-height: 1.1;
  padding: 0.42rem 0.58rem;
  text-decoration: none;
  white-space: nowrap;
}

.home-back-link:hover {
  border-color: var(--secondary);
  color: var(--tertiary);
}
`

export default (() => HomeBackLink) satisfies QuartzComponentConstructor
