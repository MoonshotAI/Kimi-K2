# Security Policy

## Supported Versions

This repository contains documentation and usage examples for Kimi K2.
Security updates are applied to the `main` branch only.

## Reporting a Vulnerability

Please do **not** open a public issue for security vulnerabilities.

Report vulnerabilities by emailing [support@moonshot.cn](mailto:support@moonshot.cn) with the subject line `SECURITY:`.
Include a description of the issue, affected files/versions, and steps to reproduce.

You can expect an acknowledgment within 5 business days.

## Scope Notes

- The Modified MIT License requires prominent "Kimi K2" attribution for commercial products/services with more than 100 million MAU or more than 20 million USD monthly revenue — review [LICENSE](LICENSE) before commercial use.
- Deployment examples in [docs/deploy_guidance.md](docs/deploy_guidance.md) are **examples**, not production-hardened configurations. Before exposing a serving endpoint publicly:
  - Put the endpoint behind authentication and TLS (e.g., a reverse proxy) — the examples bind unauthenticated ports.
  - Restrict `--network host` containers and passwordless SSH setup to trusted, isolated hosts.
  - Never commit real API keys, endpoints, or model credentials into this repository.
