# BYNotes QA API

This is the first backend foundation for BYNotes knowledge-base QA. It is built
to run separately from the Quartz GitHub Pages frontend.

## What It Does

- Loads the Quartz-generated `public/static/contentIndex.json`.
- Retrieves relevant notes for a user question.
- Applies basic CORS, request validation, abuse filtering, and IP limits.
- Returns source snippets in retrieval-only mode.
- Optionally calls the OpenAI Responses API when explicitly enabled.

The first mode is intentionally retrieval-only so the backend can be deployed
and tested without incurring LLM costs.

## Local Run

Build the Quartz content index first:

```bash
npm run build:local
```

Run a smoke search:

```bash
npm run qa:smoke
```

Start the API:

```bash
npm run qa:serve
```

Start the local static site and QA API together:

```bash
npm run serve:local
```

Then open `http://localhost:8080`.

Health check:

```bash
curl http://localhost:7860/health
```

Ask a question:

```bash
curl -X POST http://localhost:7860/api/qa \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"What is the central limit theorem?\"}"
```

## Optional LLM Mode

LLM generation is disabled by default. Enable it only on a backend host, never
in browser code.

PowerShell example:

```powershell
$env:QA_ENABLE_LLM="1"
$env:OPENAI_API_KEY="..."
$env:OPENAI_MODEL="gpt-4.1-mini"
npm run qa:serve
```

The server uses `POST https://api.openai.com/v1/responses`.

## Environment Variables

| Variable                           | Default                            | Purpose                                  |
| ---------------------------------- | ---------------------------------- | ---------------------------------------- |
| `PORT`                             | `7860`                             | HTTP port                                |
| `QA_CONTENT_INDEX`                 | `public/static/contentIndex.json`  | Content index path                       |
| `QA_PUBLIC_BASE_URL`               | `https://by-xin.github.io/BYNotes` | Source URL base                          |
| `QA_ALLOWED_ORIGINS`               | GitHub Pages and localhost origins | Browser CORS allowlist                   |
| `QA_LIMIT_PER_MINUTE`              | `10`                               | Per-IP minute limit                      |
| `QA_LIMIT_PER_DAY`                 | `50`                               | Per-IP daily limit                       |
| `QA_MAX_QUESTION_CHARS`            | `600`                              | Maximum question length                  |
| `QA_TOP_K`                         | `5`                                | Retrieved source count                   |
| `QA_MIN_SCORE`                     | `3`                                | Minimum retrieval score before answering |
| `QA_CONTEXT_CHARS`                 | `900`                              | Snippet size per source                  |
| `QA_ENABLE_LLM`                    | off                                | Set to `1` to call OpenAI                |
| `OPENAI_API_KEY`                   | unset                              | OpenAI API key, backend only             |
| `OPENAI_MODEL` / `QA_OPENAI_MODEL` | `gpt-4.1-mini`                     | OpenAI model name                        |
| `QA_MAX_OUTPUT_TOKENS`             | `700`                              | LLM output cap                           |
| `QA_BACKEND_URL`                   | `http://localhost:7860/api/qa`     | Frontend build-time Ask UI endpoint      |

## Deployment Notes

For a Hugging Face Docker Space or another API host:

1. Build or copy this repository so `public/static/contentIndex.json` exists.
2. Run `node qa-api/server.mjs`.
3. Set `QA_ALLOWED_ORIGINS=https://by-xin.github.io`.
4. Store provider API keys as backend secrets.
5. Keep `QA_ENABLE_LLM` off until retrieval-only responses look reasonable.

For production public access, add a bot check such as Cloudflare Turnstile in
front of `/api/qa`.
