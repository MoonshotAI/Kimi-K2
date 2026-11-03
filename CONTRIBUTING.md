# Contributing

Thanks for your interest in improving this repository!

## Ground Rules

- This repo documents Kimi K2 usage. Keep changes factual and consistent with the [tech report](tech_report.pdf) and the [tech blog](https://moonshotai.github.io/Kimi-K2/).
- Do not commit API keys, internal endpoints, or credentials — use placeholders such as `xxx` and `<YOUR_MODEL_DIR>`.
- All prose is in English; keep the tone consistent with existing docs.

## How to Contribute

1. Fork the repository and create a branch from `main`.
2. Make your changes:
   - Fix typos and broken links directly.
   - For new examples: add them under `docs/` and link them from the README.
   - For deployment changes: state the engine name and version you tested with.
3. Verify:
   - Code examples are syntactically valid Python and consistent with the OpenAI API.
   - Markdown passes `markdownlint` (`MD013` line length is disabled; see `.markdownlint.json`).
   - Links resolve (CI runs a link checker on every PR).
4. Open a pull request using the PR template.

## What We Won't Accept

- Benchmark numbers not present in the tech report or official blog.
- Promotional content or unrelated project links.
