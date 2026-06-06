# ICT Trading Rules — OpenClaw AI Trading Agent

This document specifies the **Inner Circle Trader (ICT) Smart Money Concepts** rules implemented in the OpenClaw agent. These rules transform discretionary institutional trading logic into deterministic, auditable decision criteria.

---

## 1. Fair Value Gap (FVG) — Rules

### Definition
A **Fair Value Gap** is a three-candle pattern where the high of the first candle and the low of the third candle do not overlap, creating an imbalance that the market tends to revisit.

### Detection Rules
- **Bullish FVG:** `candle[0].high < candle[2].low`
- **Bearish FVG:** `candle[0].low > candle[2].high`
- **Minimum gap size:** 0.5% of price
- **Maximum age:** 14 days (then invalidated)
- **Volume confirmation:** Required (1.2x 20-day average)

### Validity Criteria
- ✅ Unmitigated (price has not yet returned to fill the gap)
- ✅ Aligned with higher-timeframe bias
- ✅ Within higher-timeframe discount array (for longs) or premium array (for shorts)

---

## 2. Order Block (OB) — Rules

### Definition
An **Order Block** is the **last opposing candle** before a strong directional move, representing institutional entry or exit zones.

### Detection Rules
- **Bullish OB:** Last bearish candle before a strong bullish move
- **Bearish OB:** Last bullish candle before a strong bearish move
- **Minimum displacement:** 1.0 x ATR
- **Minimum volume:** 1.5x 20-day average
- **Confirmation:** FVG must be created after the OB

### Validity Criteria
- ✅ Displacement confirmed (ATR > 1.0)
- ✅ Volume profile (OB candle has high volume)
- ✅ Unmitigated (price has not yet returned to OB zone)

---

## 3. Liquidity Sweep — Rules

### Definition
A **Liquidity Sweep** (or Liquidity Grab) is a temporary price excursion beyond a key level, designed to trigger retail stop losses before the true directional move.

### Detection Rules
- **Key levels:** Previous day high/low, swing highs/lows, equal highs/lows
- **Minimum sweep depth:** 0.3% beyond the level
- **Reversal confirmation:** 3 candles after the sweep
- **Volume:** Decreasing volume on the sweep, increasing on reversal

### Validity Criteria
- ✅ Sweep reaches beyond liquidity level
- ✅ Reversal confirmed within 3 candles
- ✅ HTF bias aligns with reversal direction

---

## 4. Confluence Rules (FVG + OB)

The most high-probability setups combine **FVG + OB alignment**:

### Long Setup
1. Higher-timeframe bias: **Bullish**
2. Price in HTF **discount array** (0.5 - 0.79 of range)
3. **Bullish FVG** detected (unmitigated)
4. **Unmitigated bullish OB** identified within or near the FVG
5. Risk:Reward ratio ≥ 2.0
6. Session: London or NY overlap
7. No major news in next 30 minutes

### Short Setup
1. Higher-timeframe bias: **Bearish**
2. Price in HTF **premium array** (0.79 - 1.0 of range)
3. **Bearish FVG** detected (unmitigated)
4. **Unmitigated bearish OB** identified within or near the FVG
5. Risk:Reward ratio ≥ 2.0
6. Session: London or NY overlap
7. No major news in next 30 minutes

---

## 5. Entry Rules

### Entry Trigger
- Price reaches FVG midpoint (50% level)
- Confirmation candle closes in expected direction
- Volume confirms the move (1.2x 20-day average)

### Position Sizing
- **Method:** Fractional Kelly Criterion (1/4 Kelly)
- **Formula:** `position_size = (kelly_fraction × edge / odds) × portfolio`
- **Cap:** 10% of portfolio per position
- **Total cap:** 30% portfolio exposure

---

## 6. Exit Rules

### Stop Loss
- **Type:** ATR-based
- **ATR period:** 14
- **ATR multiplier:** 1.5
- **Placement:** Below OB low (for long) / Above OB high (for short)

### Take Profit (3 levels)
- **TP1:** 1.0R (close 33% of position)
- **TP2:** 2.0R (close 33% of position)
- **TP3:** 3.0R (close 34% of position, runner)

### Stop Management
- Move stop to breakeven after TP1 hit
- Trail stop using 1.0 ATR after TP2 hit

---

## 7. Session Filters

### Preferred Sessions
- **London:** 08:00-12:00 UTC
- **New York:** 13:00-17:00 UTC
- **London/NY Overlap:** 13:00-17:00 UTC (best liquidity)

### Avoid Sessions
- **Asia (low volume):** 00:00-08:00 UTC
- **Sunday open:** Limited setups
- **Friday close:** Close all positions before 20:00 UTC

---

## 8. News & Event Filters

### No-Trade Windows
- 30 minutes before major economic releases
- 30 minutes after major economic releases
- FOMC, ECB, BOJ meetings
- CPI, NFP, GDP releases
- Crypto-specific: Exchange maintenance, regulatory announcements

---

## 9. Risk Management Rules

### Position Limits
- **Max position size:** 10% of portfolio
- **Max total exposure:** 30% of portfolio
- **Max open positions:** 3 simultaneously

### Loss Limits
- **Daily loss limit:** 2% of portfolio → Pause trading
- **Weekly loss limit:** 5% of portfolio → Reduce position size 50%
- **Monthly loss limit:** 10% of portfolio → Stop trading for rest of month

### Drawdown Protection
- **Auto-pause trigger:** 8% drawdown from peak
- **Reactivation:** Manual review required

---

## 10. Audit & Logging

### Every Trade Must Log
- **Signal ID** (from JSON)
- **Entry/exit prices** and timestamps
- **Position size** and risk taken
- **Reasoning chain** (which rules passed/failed)
- **P&L** (realised and unrealised)
- **HTF context** at time of trade
- **Session** and market conditions

### Retention
- All trade logs: **7 years** (per SFC requirement)
- Decision logs: **7 years**
- Performance metrics: **Permanent**

---

*Rules aligned with ICT methodology + HK VASP regulatory requirements*
