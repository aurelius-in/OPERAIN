# OPERAIN Integration Notes

This document catalogs public integration points for five external applications. Do not copy code or internal logic; use only documented/public interfaces.

## BayWalk (Plan)
- Base URL env: `BAYWALK_BASE_URL`
- Auth: TBD (assume none or OIDC per deployment)
- Health: `GET /health` → expect `{ "status": "ok" }` or 200
- Deep links: if undocumented, open base URL
- Webhooks: `event=bom.ready { project_id, items:[{ sku, qty, description, alt_sku, eta, monthly_cost }] }`
- Outbound calls: none required
- Errors to surface: 401/403 auth, 5xx

## PerceptionLab (Prove)
- Base URL env: `PERCEPTIONLAB_BASE_URL`
- Auth: TBD
- Health: `GET /health` → `{ "status": "ok" }`
- Deep links: reports/projects if available; else base URL
- Webhooks: `event=eval.completed { report_url, map, iou, idf1, latency_ms }`
- Outbound calls: `POST /api/evals { clip_url|incident_ref } → { report_url, metrics }`
- Errors: 400 malformed, 401/403, 5xx; timeouts 10s, retry with backoff

## EdgeSight-QA (Run)
- Base URL env: `EDGESIGHT_BASE_URL`
- Auth: TBD
- Health: `GET /health`
- Deep links: dashboards if available; else base URL
- Webhooks: `event=fail.detected { incident_id, image_url, log_url, sku, timestamp }`
- Outbound calls: none required

## RAINLane (Comply)
- Base URL env: `RAINLANE_BASE_URL`
- Auth: TBD
- Health: `GET /health`
- Webhooks: `event=answer.yellow { question, doc_ref, confidence, timestamp }`
- Outbound calls: none required

## DriftHawk (Operate)
- Base URL env: `DRIFTHAWK_BASE_URL`
- Auth: TBD
- Health: `GET /health`
- Webhooks: `event=release.signed { release_id, signed_receipt_url }`
- Outbound calls: `POST /api/releases { project_id, model_version_id, plan } → { release_id, signed_receipt_url }`

Notes: Replace placeholders with official docs as available. Verify any webhook signatures if documented using `WEBHOOK_SECRET`.

