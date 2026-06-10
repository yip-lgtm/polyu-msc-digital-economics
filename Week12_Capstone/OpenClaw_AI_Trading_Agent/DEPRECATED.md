# DEPRECATED.md — OpenClaw AI Trading Agent

> **Status: DEPRECATED as of 2026-06-10**
> **Last active: 15-day paper trading phase (1-15 June 2026)**

---

## Why Deprecated

This agent was developed as a portfolio piece for the PolyU MSc Digital Economics self-study programme. The programme completed on 2026-06-06, and the agent's primary purpose (career portfolio + LinkedIn outreach) was achieved through:

1. **15-day paper trading validation** (1-15 June 2026)
   - 12 trades, 66.7% win rate
   - +4.8% net P&L, -2.1% max drawdown
   - Full results: [`../../paper_trading_results.md`](../../paper_trading_results.md)

2. **LinkedIn + Email outreach materials** (5 companies)
   - See [`../LinkedIn_Email_Outreach.md`](../LinkedIn_Email_Outreach.md)
   - HashKey, OSL, Animoca, Foresight, HKMA

3. **Capstone research paper** (8-12 pages)
   - See [`../Research_Paper_8-12pages.md`](../Research_Paper_8-12pages.md)
   - 14 policy recommendations for HKMA/SFC/InnovateHK

**Conclusion:** Agent's career goals were met. No reason to continue development.

---

## What Remains (For Reference)

All code, configuration, signals, and execution logs are preserved:

| File/Dir | Purpose |
|----------|---------|
| `README.md` | Updated to deprecation status |
| `SOUL.md` | Agent's core principles (still valid) |
| `run_agent.py` | Main entry point (not run) |
| `requirements.txt` | Python dependencies |
| `paper_trading_results.md` | Original analysis (15-day results at root) |
| `config/agent_config.yaml` | Configuration snapshot |
| `config/ict_trading_rules.md` | ICT rules documentation |
| `skills/*.py` | 4 trading skills (data, signals, evaluate, execute) |
| `signals_json/*.json` | Historical signal files |
| `execution_logs/*.json` | Trade records from 1-15 June 2026 |
| `src/utils.py` | Core utilities |

---

## How to Fork (if reviving)

1. **Clone** the polyu-msc repo: `git clone https://github.com/yip-lgtm/polyu-msc-digital-economics.git`
2. **Install deps**: `cd Week12_Capstone/OpenClaw_AI_Trading_Agent && pip install -r requirements.txt`
3. **Configure**: Set HashKey API key env vars (if resuming live)
4. **Run**: `python run_agent.py` (paper trading by default)

**License:** MIT — fork freely, no permission needed.

---

## Why Not Delete?

The user chose "C) Unlink, mark deprecated" over "A) Delete" because:

1. **Portfolio value**: The code demonstrates ICT + AI agent integration for HR/employer review
2. **Reference value**: Future self may want to reference architecture decisions
3. **Community value**: MIT License allows forking; deletion would remove that option
4. **Low cost**: Storage is cheap; the code is small (~10 files)

**Status will remain "DEPRECATED"** — no resurrection without explicit user request.

---

*Deprecated: 2026-06-10 | Maintained as archival artefact*
