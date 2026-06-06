# OpenClaw 3-Module Architecture — Detailed Specification

**Version:** 2.1.0
**Last Updated:** 2026-06-06

---

## 1. Perception Module

### Purpose
Ingest real-time market data and transform into structured ICT signals.

### Input
- **Price data:** OHLCV from HashKey WebSocket (1m, 5m, 15m, 1h, 4h, 1d)
- **Volume data:** Real-time trade volume
- **Order book data:** Level 2 order book snapshots
- **On-chain data:** Whale wallet movements (BTC, ETH)
- **Sentiment data:** Twitter/X, news APIs

### Processing
1. **Data normalisation** across exchanges
2. **ICT pattern detection:**
   - Fair Value Gap (FVG)
   - Order Block (OB)
   - Liquidity Sweep
   - Market Structure (HH, HL, LH, LL)
3. **Higher-timeframe context** (HTF discount/premium)
4. **JSON serialisation** for downstream consumption

### Output (JSON Schema)
```json
{
  "signal_id": "fvg_2026_06_06_btc_15m",
  "type": "FVG",
  "direction": "bullish",
  "trading_pair": "BTC-USD",
  "timeframe": "15m",
  "high": 68500.50,
  "low": 68200.00,
  "midpoint": 68350.25,
  "volume_confirmation": true,
  "htf_context": "discount",
  "timestamp": "2026-06-06T15:30:00Z"
}
```

### Source
**Python ICT Dashboard V2** (separate process)
- File: `../Python_ICT_Dashboard_V2.py`
- Output: `signals_json/`

---

## 2. Reasoning Module

### Purpose
Evaluate incoming signals against predefined rules, risk parameters, and market context.

### Input
- ICT signal from Perception Module
- Current portfolio state
- Market context (HTF bias, session, news)
- Risk parameters (max position, max drawdown)

### Processing (Rule-based + ML)
1. **Signal validation:**
   - FVG valid only if unmitigated
   - OB valid only if not swept
   - Liquidity sweep confirmed by reversal pattern

2. **Confluence check:**
   - FVG + OB alignment
   - HTF discount/premium alignment
   - Session timing (London/NY overlap)

3. **Risk-reward calculation:**
   - Entry: FVG midpoint
   - Stop Loss: Below OB low (for long) / Above OB high (for short)
   - Take Profit: 2R, 3R, 4R levels

4. **Position sizing:**
   - Kelly Criterion (fractional, 1/4 Kelly)
   - Volatility adjustment (ATR-based)

5. **Decision output:** VALID / INVALID + reasoning

### Output (JSON Schema)
```json
{
  "signal_id": "fvg_2026_06_06_btc_15m",
  "decision": "VALID",
  "direction": "long",
  "entry_price": 68350.25,
  "stop_loss": 68100.00,
  "take_profit": [68500.00, 68700.00, 68900.00],
  "risk_reward_ratio": 2.5,
  "position_size_usd": 5000,
  "reasoning": [
    "Bullish FVG in discount array",
    "Confluence with unmitigated OB",
    "London session overlap",
    "R:R = 2.5:1"
  ]
}
```

---

## 3. Action Module

### Purpose
Execute validated trades with proper risk management and logging.

### Input
- Validated trade decision from Reasoning Module

### Processing
1. **Pre-execution checks:**
   - Account balance sufficient
   - Position size within limits
   - Total exposure within limits
   - Daily/weekly/monthly loss limits not breached

2. **Order execution:**
   - Order type: Limit at entry price
   - Time-in-force: GTC (Good Till Cancelled)
   - Contingent orders: Stop loss + Take profit

3. **Position management:**
   - Partial close at 1R, 2R (33% each)
   - Trailing stop on remaining 34%
   - Move stop to breakeven at 2R

4. **Logging:**
   - Trade execution timestamp
   - Entry/exit prices
   - P&L (realised and unrealised)
   - Reasoning chain (for explainability)
   - Audit trail (perception → reasoning → action)

### Output
- **Executed trade** in `execution_logs/`
- **Updated portfolio state** in memory
- **Performance metrics** updated in Prometheus

---

## 4. Feedback Loop

### Continuous Improvement
1. **Daily review:** Win rate, Sharpe, drawdown
2. **Weekly calibration:** Adjust Kelly fraction, position size limits
3. **Monthly model retraining:** LSTM on new data
4. **Quarterly strategy review:** Add/remove ICT components

### Explainability
- **LIME/SHAP:** Trade-level explanations
- **Decision log:** Full reasoning chain for every trade
- **Performance attribution:** ICT component contribution

---

## 5. Modularity Benefits

Each module can be:
- **Independently tested** (unit tests, integration tests)
- **Independently debugged** (clear interfaces)
- **Independently audited** (regulatory compliance)
- **Independently upgraded** (zero-downtime deployment)

This modularity is critical for:
- **SFC VASP compliance** — audit trail
- **PDPO compliance** — data minimisation
- **Operational resilience** — fault isolation
- **Continuous improvement** — A/B testing strategies

---

*Architecture aligned with HK VASP regulatory requirements + open-source best practices*
