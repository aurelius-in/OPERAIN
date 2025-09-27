<p align="center">
  <img src="operain.png" alt="OPERAIN wordmark" width="45%">
</p>

# OPERAIN — Investor Brief

**One front door from site walk to signed release.**  
OPERAIN is a seven-step suite that turns a site survey into running, audit-ready operations: **Plan → Procure and Provision → Prove → Run → Comply → Operate → Improve.**  
The suite implements **Step 2 (Procure and Provision)** and **Step 7 (Improve/CAPA and Retrain)** natively, and **orchestrates** five existing apps (BayWalk, PerceptionLab, EdgeSight-QA, RAINLane, DriftHawk) via links, APIs, and webhooks.

---

## 1) Executive summary
- **Problem:** Physical operations (factories, warehouses, retail, hospitals, data centers) leak value through slow planning, scattered buying, guess-based model choices, ad-hoc QA, risky deployments, and audit scramble.  
- **Solution:** OPERAIN unifies the lifecycle—planning, purchasing, evaluation, runtime QA, SOP answers, governed releases, and continuous improvement—with an **evidence locker** for instant audits.  
- **Why now:** Vision AI and edge computing are mainstream; enterprises need **operationalization**, not pilots.  
- **Business model:** Subscription (per site, line, or cluster) + implementation services when needed.  
- **Proof:** Each component already exists as a working app; OPERAIN is the orchestrator and glue that compounds value.

---

## 2) Product at a glance

| Step | Delivered by | Core value |
|---|---|---|
| 1. Plan | BayWalk (external) | From walk-through to camera layout, BOM, power and network plan, tasks |
| 2. Procure and Provision | **OPERAIN** | PO board, device vault, provisioning wizard, camera discovery |
| 3. Prove | PerceptionLab (external) | Head-to-head model reports (accuracy, latency), PDFs |
| 4. Run | EdgeSight-QA (external) | Real-time pass/fail, snapshots, write-back to plant systems |
| 5. Comply | RAINLane (external) | SOP answers with citations; green and yellow lanes |
| 6. Operate | DriftHawk (external) | GitOps, policy gates, signed releases and rollbacks |
| 7. Improve | **OPERAIN** | Incident → CAPA → re-test → promote; all evidence linked |

**Evidence Locker:** central index of reports, receipts, snapshots, approvals.

---

## 3) ICP and buyer
- **Primary industries:** Pharma and medical devices, food and beverage/CPG, logistics and 3PL, large retail ops, electronics/auto assembly, data centers, hospitals.  
- **Economic buyer:** VP Operations, VP Quality, Head of Manufacturing IT/OT, Plant or Facility Manager.  
- **Daily users:** Ops and Quality managers, process/manufacturing engineers, platform and SRE, line supervisors, auditors.

---

## 4) Value and ROI (monthly, per site or line)

| App/Step | Typical impact (conservative) |
|---|---|
| BayWalk (Plan) | \$2k–\$7k labor and overbuy avoided |
| **Procure and Provision (OPERAIN)** | \$5k–\$20k fewer delays and setup errors |
| PerceptionLab (Prove) | \$10k–\$40k better model choice; faster evals |
| EdgeSight-QA (Run) | \$60k–\$250k per line via scrap/rework reduction (0.5–2%) |
| RAINLane (Comply) | \$17k–\$50k faster changeovers and fewer policy mistakes |
| DriftHawk (Operate) | \$10k–\$40k fewer failed deploys/outages |
| **Improve (OPERAIN)** | \$10k–\$60k faster CAPA, steady accuracy gains |

> Rule of thumb: busy lines cost \$3k–\$10k/hr when down; a 0.5–2% defect delta on \$5–\$15M monthly output is material.

**Illustrative ROI (single regulated line):** ~\$160k+/mo value vs. suite price \$25k–\$60k → **3–6× monthly ROI**.

---

## 5) Pricing (subscription)

| SKU | Price guidance |
|---|---|
| BayWalk | \$1k–\$3k per site |
| PerceptionLab | \$2k–\$5k per site |
| EdgeSight-QA | \$8k–\$20k per line |
| RAINLane | \$3k–\$6k per site |
| DriftHawk | \$5k–\$12k per cluster |
| **OPERAIN Step 2** | \$2k–\$6k per site *(suite-only)* |
| **OPERAIN Step 7** | \$3k–\$8k per site *(suite-only)* |
| **OPERAIN Suite** | \$25k–\$60k per site (covers 1–2 lines) |

Volume discounts for multi-site or multi-line deployments (10–25%).

---

## 6) Go-to-market
- **Land:** PerceptionLab + EdgeSight-QA for immediate scrap reduction and proof.  
- **Expand:** Add RAINLane and DriftHawk for compliance and governed releases.  
- **Standardize:** Adopt OPERAIN suite to stitch procurement and continuous improvement, consolidate evidence, and scale.

---

## 7) User stories (abridged)

- **Pharma Quality Manager:** choose Model B (+14% accuracy) in PerceptionLab; deploy via DriftHawk with signatures; RAINLane guides changeover; Improve closes glare-related incidents.  
- **3PL Ops Director:** plan pack-station cameras; Procure and Provision devices; EdgeSight-QA marks pass/fail with snapshots; Improve routes misses into CAPA.  
- **Retail Platform Lead:** policy gates and signed images cut failed releases; rollback in seconds when canary trips.

---

## 8) Technology and integrations (plain language)
- **Hub and steps:** OPERAIN provides the UI hub, Step 2 and Step 7, and an evidence locker.  
- **External apps:** BayWalk, PerceptionLab, EdgeSight-QA, RAINLane, DriftHawk remain separate services; OPERAIN opens them and exchanges events via health checks, APIs, and webhooks.  
- **Stack:** React/TypeScript front end; FastAPI back end; Postgres; optional Redis; Docker; GitHub Actions.  
- **Ops connectors:** Ignition, MQTT, OPC-UA (via EdgeSight-QA); OpenShift/Kubernetes; GitOps; policy-as-code and signed supply chain.

---

## 9) Defensibility
- **Workflow ownership:** OPERAIN sits at the control point (procurement and improvement) where value compounds.  
- **Evidence by default:** signed releases, reports, pass/fail snapshots, and SOP citations tied to batches/SKUs.  
- **Switching cost:** once procurement, runtime QA, and CAPA loop are unified, replacing one point tool preserves the hub.

---

## 10) Risks and mitigations

| Risk | Mitigation |
|---|---|
| Integration friction | Thin adapters, documented webhooks, env-based endpoints |
| Air-gapped sites | Offline-safe ops, signed artifacts, file-based sync |
| Change management | Role-based UI, small wins first (one line, one SKU) |
| Model drift | Improve loop enforces re-test before promote |

---

## 11) Roadmap (next 2–3 quarters)
- Model registry UI (promote, compare, retire).  
- Digital-twin camera coverage simulator.  
- Auto-generated audit pack ZIP by batch or SKU.  
- Fleet health (camera uptime, edge temps, queue depth).  
- Cost and ROI board.

---

## 12) Metrics we track
- Time from plan to first run.  
- Scrap/rework delta and false reject rate.  
- Changeover time and SOP query resolution.  
- Release failure rate and rollback time.  
- Incident recurrence rate and time to CAPA close.  
- Evidence completeness (reports, receipts, snapshots per batch).

---

## 13) Diagrams (GitHub-friendly Mermaid)

**Lifecycle (vertical)**  
```mermaid
flowchart TB
  A["Plan (BayWalk)"] --> B["Procure and Provision (OPERAIN)"]
  B --> C["Prove (PerceptionLab)"]
  C --> D["Run (EdgeSight-QA)"]
  D --> E["Comply (RAINLane)"]
  E --> F["Operate (DriftHawk)"]
  F --> G["Improve (OPERAIN)"]
  G --> C
