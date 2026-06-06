# ICT Trading Rules

This document defines the trading rules used by the **OpenClaw AI Trading Agent**. The rules are based on **Inner Circle Trader (ICT) Smart Money Concepts**, with additional filters designed for clarity, risk control, and suitability in regulated trading environments such as **Hong Kong's VASP framework**.

---

## 1. Overview

The agent follows a **confluence-based approach**. A trade signal is only considered valid when multiple ICT concepts align. The primary objective is to identify **high-probability institutional order flow zones** rather than chasing every market move.

### Core Philosophy

- **Trade in the direction of institutional order flow** (Smart Money).
- **Wait for clear liquidity engineering** and market structure confirmation.
- **Prioritise confluence over frequency.**

---

## 2. Core ICT Concepts Used

| Concept | Definition | Role in the Agent |
|---------|------------|-------------------|
| **Order Block (OB)** | The last opposing candle before a strong impulsive move | Key entry zone |
| **Fair Value Gap (FVG)** | Imbalance created during rapid price movement that price tends to revisit | Entry trigger / confirmation |
| **Liquidity Grab** | Temporary price movement to sweep stop losses or induce retail participation | Confirmation of institutional intent |
| **Discount / Premium Array** | Price trading below (discount) or above (premium) the equilibrium | Bias filter |
| **Market Structure** | Break of Structure (BOS) and Change of Character (CHOCH) | Higher-timeframe direction |

---

## 3. Entry Rules (Confluence Required)

A valid long setup must meet **at least 3 of the following 5 conditions**:

1. **Bullish Order Block** present and unmitigated (price has not returned to fill the block).
2. **Bullish Fair Value Gap (FVG)** formed, and price is trading within or just above the FVG.
3. **Price is trading in a discount array** relative to the higher-timeframe equilibrium.
4. **A Liquidity Grab** (equal highs or stop hunt below recent lows) has recently occurred.
5. **Higher-timeframe market structure is bullish** (Break of Structure to the upside).

A valid short setup follows the **inverse** of the above conditions.

### Additional Filters

- Only consider setups that align with the **higher-timeframe (4H / Daily) bias**.
- Avoid trading during major news events or low liquidity periods (e.g., weekends for certain assets).
- **Minimum confluence score of 3/5** is required before the agent considers execution.

---

## 4. Risk Management Rules

| Rule | Description | Default Setting |
|------|-------------|-----------------|
| **Position Sizing** | Risk no more than 0.5%–1% of account per trade (Fractional Kelly 1/4) | 0.75% (1/4 Kelly) |
| **Stop Loss Placement** | Below the Order Block (long) / Above the Order Block (short) | 1–1.5× ATR |
| **Take Profit** | Minimum 1:2 Risk-Reward ratio | 1:2.5 |
| **Maximum Daily Loss** | Stop trading for the day if daily loss exceeds 2% | 2% |
| **Maximum Weekly Loss** | Reduce position size 50% if weekly loss exceeds 5% | 5% |
| **Maximum Monthly Loss** | Stop trading for rest of month if monthly loss exceeds 10% | 10% |
| **Maximum Open Positions** | Limit concurrent open positions | 2-3 |
| **Auto-pause Drawdown** | Pause trading if drawdown from peak exceeds 8% | 8% |

---

## 5. Exit & Trade Management Rules

### Partial Profit Taking

- **50% close** at **1:1.5 Risk-Reward** → Move stop loss to breakeven.

### Full Exit (3 TP Levels)

- **TP1:** 1.0R → Close 33% of position
- **TP2:** 2.0R → Close 33% of position, trail stop using 1.0 ATR
- **TP3:** 3.0R → Close 34% (runner) or trail with 1.5 ATR

### Alternative Full Exit

- Close remaining position at **1:2.5 Risk-Reward** or when price reaches the opposing Order Block / FVG.

### Invalidation

- Exit immediately if price **closes strongly beyond the Order Block in the opposite direction** (indicating mitigation or failed setup).

### Time-based Exit

- If a trade remains open for **more than 48 hours** without reaching target or invalidation, reassess and consider manual exit.

---

## 6. Session Filters

### Preferred Sessions (Higher Liquidity)

- **London:** 08:00-12:00 UTC
- **New York:** 13:00-17:00 UTC
- **London/NY Overlap:** 13:00-17:00 UTC (best liquidity)

### Avoid Sessions

- **Asia (low volume):** 00:00-08:00 UTC
- **Sunday open:** Limited setups
- **Friday close:** Close all positions before 20:00 UTC

---

## 7. News & Event Filters

### No-Trade Windows

- **30 minutes** before major economic releases
- **30 minutes** after major economic releases
- FOMC, ECB, BOJ meetings
- CPI, NFP, GDP releases
- Crypto-specific: Exchange maintenance, regulatory announcements

---

## 8. Compliance & Audit

### Audit Trail Requirements

- **Every decision** logged with timestamp + reasoning chain
- **Trade records** preserved for 7 years (per SFC requirement)
- **LIME/SHAP explainability** for trade rationale
- **PDPO compliance:** No PII collected

### Deterministic & Auditable

- All rules are designed to be **deterministic and auditable**
- Suitable for **SFC VASP regulatory inspection**
- Modularity allows **independent testing** of each component (Perception, Reasoning, Action)

---

## 9. Notes & Future Improvements

### Current Design (Paper Trading)

- Current rules are intentionally conservative to suit paper trading and regulatory compliance.
- All rules are designed to be deterministic and auditable.

### Future Versions Will Include

- **Dynamic position sizing** based on signal strength
- **Multi-timeframe confirmation** scoring (4H + Daily + Weekly)
- **Session-based filters** (e.g., London / New York kill zones)
- **Sentiment analysis** integration (Twitter/X, news APIs)
- **On-chain data integration** for Web3-native assets
- **Reinforcement learning** for adaptive parameter tuning

---

## 10. Quick Reference Card

```
ENTRY (Long)          EXIT
─────────             ─────────
✓ Bullish OB          TP1: 1R → 33%
✓ Bullish FVG         TP2: 2R → 33%
✓ Discount array      TP3: 3R → 34%
✓ Liquidity grab      SL: Below OB (1.5 ATR)
✓ HTF Bullish         Time: Max 48h
                      Invalid: Close below OB

RISK MANAGEMENT
─────────
• Position: 0.75% (1/4 Kelly)
• Daily: -2% → Stop
• Weekly: -5% → Reduce
• Monthly: -10% → Stop
• Drawdown: -8% → Auto-pause
• Max Positions: 2-3
```

---

*Rules aligned with ICT methodology + HK VASP regulatory requirements*

**Version:** 2.1.0 | **Last Updated:** 2026-06-06 | **Author:** Saba Yip
