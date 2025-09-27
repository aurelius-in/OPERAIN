# Deeplink Rules

If a tool documents deep links, use them; otherwise open the base URL.

- BayWalk: base or `/projects/:id` if official link exists.
- PerceptionLab: base or `/reports/:id` for eval reports.
- EdgeSight-QA: base or `/dashboards/:project` if available.
- RAINLane: base.
- DriftHawk: base or `/releases/:id` for signed releases.

Fallback: always open `BASE_URL` in a new tab.
