# LLM QA Roadmap

This note captures a staged plan for adding knowledge-base QA to BYNotes without
moving the Quartz site away from GitHub Pages.

## Current Decision

- Keep the public Quartz frontend on GitHub Pages.
- Run QA as a separate backend service, initially on Hugging Face Spaces,
  Render, Railway, Fly.io, or another small API host.
- Do not expose LLM provider keys to the browser.
- Do not require user registration for the first public version.
- Treat the QA API as a bounded knowledge-base endpoint, not a general chatbot.

## Target Architecture

```text
GitHub Pages / BYNotes frontend
  |
  | POST https://qa-backend.example/api/qa
  v
QA backend
  |-- CORS allowlist
  |-- optional Turnstile check
  |-- IP and global rate limits
  |-- question validation and abuse filters
  |-- BYNotes retrieval from contentIndex.json or a vector store
  |-- optional LLM generation
  v
answer + source notes
```

## Phase 1: Retrieval-Only API

Goal: expose a safe backend that can answer with relevant note sources before
spending money on LLM calls.

Implemented in this branch:

- `qa-api/server.mjs`
- `qa-api/README.md`
- `quartz/components/Ask.tsx`
- `scripts/serve_local.mjs`
- `npm run qa:serve`
- `npm run qa:smoke`
- `npm run build:local`
- `npm run serve:local`

Behavior:

- Reads `public/static/contentIndex.json`.
- Searches note titles, tags, and content with a simple lexical ranker.
- Rejects empty or oversized questions.
- Rejects common prompt-injection and secret-extraction attempts.
- Applies in-memory per-IP minute and daily limits.
- Applies CORS allowlist headers.
- Returns source titles, URLs, snippets, and scores.
- Can run in retrieval-only mode without any LLM key.

Verification:

```bash
npm run build:plain
npm run qa:smoke
npm run qa:serve
```

## Phase 2: Optional LLM Generation

Goal: generate concise answers only when retrieval finds relevant notes.

Controls:

- LLM is disabled unless `QA_ENABLE_LLM=1`.
- API key stays in backend environment variables.
- Model is configurable with `OPENAI_MODEL` or `QA_OPENAI_MODEL`.
- Output length is capped with `QA_MAX_OUTPUT_TOKENS`.
- The prompt tells the model to answer only from retrieved snippets.
- Retrieved notes are marked as data, not instructions.

Important gate:

```text
question -> retrieve -> low score? return no-answer without LLM
question -> retrieve -> good score? call LLM with top-k note snippets
```

## Phase 3: Frontend Ask UI

Goal: add a small ask box to the Quartz frontend while keeping normal search
unchanged.

Implemented scope:

- Add a compact `Ask` button near the existing search entry point.
- Submit to the build-time `QA_BACKEND_URL` endpoint.
- Show answer, sources, and a clear "not enough context" state.
- Avoid chat history in the first version.
- Keep the API URL configurable at build time.

## Phase 4: Public Abuse Controls

Goal: keep the feature public without forcing users to create accounts.

Recommended controls:

- Cloudflare Turnstile or equivalent bot check.
- Per-IP rate limit.
- Per-IP daily limit.
- Global daily budget.
- Max question length.
- Max answer tokens.
- Retrieval relevance gate.
- Request logging with privacy-aware redaction.

The first version can run without Turnstile, but it should be added before any
wide public launch.

## Phase 5: Better Retrieval

Goal: improve answer quality after the simple lexical API proves useful.

Options:

- Keep lexical search for small notes if it is good enough.
- Add chunking over `content/**/*.md`.
- Add embeddings and store vectors in SQLite with sqlite-vec, LanceDB, Chroma,
  Supabase pgvector, or a hosted vector service.
- Store source metadata: slug, title, heading, line range, tags, and URL.
- Keep lexical fallback for exact math terms and abbreviations.

## Phase 6: Deployment

Recommended first deployment:

```text
GitHub Pages: frontend
Hugging Face Docker Space or Render: qa-api
OpenAI/Gemini/Anthropic/etc.: external LLM provider
```

For Hugging Face Spaces:

- Use a Docker Space for the API.
- Store `OPENAI_API_KEY` in Space secrets.
- Set `QA_ALLOWED_ORIGINS=https://by-xin.github.io`.
- Set `QA_PUBLIC_BASE_URL=https://by-xin.github.io/BYNotes`.
- Start with retrieval-only mode, then enable `QA_ENABLE_LLM=1`.

## API Contract

Request:

```json
{
  "question": "What is the central limit theorem?"
}
```

Response:

```json
{
  "answer": "A short answer grounded in retrieved notes.",
  "mode": "retrieval-only",
  "sources": [
    {
      "title": "Central Limit Theorem",
      "url": "https://by-xin.github.io/BYNotes/ProbabilityTheory/Limit/Central-Limit-Theorem",
      "score": 42,
      "snippet": "..."
    }
  ]
}
```

## Open Questions

- Whether public QA should be free for everyone or guarded by a lightweight
  access code during early testing.
- Whether the first frontend should be a modal, a page, or an extension of the
  existing search overlay.
- Whether retrieval quality is sufficient with `contentIndex.json`, or whether
  source Markdown chunking should happen before frontend integration.
