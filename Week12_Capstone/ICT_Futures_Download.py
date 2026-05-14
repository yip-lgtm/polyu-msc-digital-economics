# ICT Futures Data Download Script
## Week 12 Capstone — OpenClaw AI Trading Agent

**Date:** 2026-05-14
**Purpose:** Download futures data for ICT analysis + OpenClaw Agent signals

---

## 📥 Download Script

```python
import yfinance as yf

# ICT Futures Symbols
symbols = [
    'MES=F',   # Micro E-mini S&P 500
    'MNQ=F',   # Micro E-mini Nasdaq
    'M2K=F',   # Micro E-mini Russell
    'M6E=F',   # Micro Euro
    'M6A=F',   # Micro Australian Dollar
    'MCL=F',   # Micro Crude Oil
    'SIL=F',   # Micro Silver
    'MGC=F',   # Micro Gold
]

# Download 60 days, 15-minute interval
for sym in symbols:
    tk = yf.Ticker(sym)
    df = tk.history(period='60d', interval='15m')
    filename = f"{sym.replace('=F', '')}.csv"
    df.to_csv(filename)
    print(f"Downloaded: {filename} ({len(df)} rows)")
```

---

## 📊 Data Dictionary

| Symbol | Name | Use Case |
|--------|------|----------|
| MES=F | Micro E-mini S&P 500 | US Equity direction |
| MNQ=F | Micro E-mini Nasdaq | Tech equity direction |
| M2K=F | Micro E-mini Russell | Small-cap direction |
| M6E=F | Micro Euro | EUR/USD direction |
| M6A=F | Micro Australian Dollar | AUD/USD direction |
| MCL=F | Micro Crude Oil | Commodity / risk sentiment |
| SIL=F | Micro Silver | Precious metals / inflation |
| MGC=F | Micro Gold | Safe haven / USD sentiment |

---

## 🎯 ICT Applications

1. **Order Block Detection** — Identify swing lows/highs
2. **Fair Value Gap (FVG)** — Detect 15m timeframe imbalances
3. **Liquidity Zones** — Map institutional order flow
4. **Smart Money Concept** — Track where institutions trade

---

## 🚀 Next Steps

1. Run script to download data
2. Apply ICT indicators (Order Blocks, FVGs)
3. Generate signals.json for OpenClaw Agent
4. Paper trade on Binance Testnet or HashKey Demo

---

*Week 12 Capstone — ICT + OpenClaw AI Trading Agent*