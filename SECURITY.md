# Security Policy

- Report vulnerabilities by opening a private security advisory on GitHub.
- Do not include secrets in issues or PRs.
- Webhook payloads should include `X-Signature` HMAC with `WEBHOOK_SECRET`.
- Set `ALLOW_LOCAL_LOGIN=false` in production and configure OIDC (`OAUTH_*`).
- Run behind TLS; limit CORS via `ALLOWED_CORS_ORIGINS`.
- Rotate `JWT_SECRET` regularly and scope roles minimally.
