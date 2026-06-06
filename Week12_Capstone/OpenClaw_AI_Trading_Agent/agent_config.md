# OpenClaw AI Trading Agent — Configuration

**Last Updated:** 2026-06-06
**Version:** 2.1.0
**Status:** Live on HashKey

---

## 1. Exchange Connection

```yaml
exchange:
  name: HashKey
  api_endpoint: https://api.hashkey.com
  websocket_endpoint: wss://ws.hashkey.com
  rate_limit: 10  # requests/second
  testnet: false
  trading_pairs:
    - BTC-USD
    - ETH-USD
    - SOL-USD
```

## 2. ICT Signal Configuration

```yaml
ict_signals:
  fair_value_gap:
    enabled: true
    min_gap_size: 0.5  # % of price
    max_age: 14  # days
    detection_timeframes: [15m, 1h, 4h]
  
  order_block:
    enabled: true
    min_volume: 1.5  # x average
    min_displacement: 1.0  # ATR multiplier
    confirmation_required: true
  
  liquidity_sweep:
    enabled: true
    min_sweep_depth: 0.3  # % beyond level
    reversal_confirmation: 3  # candles
```

## 3. Reasoning Module Rules

```yaml
reasoning:
  entry_conditions:
    - bullish_fvg AND unmitigated_bullish_ob
    - within_higher_tf_discount  # 0.5 - 0.79 of range
    - risk_reward_ratio: 2.0
    - market_session: london_or_ny
    
  exit_conditions:
    - stop_loss: 1.5_atr
    - take_profit_1: 1.0_risk  # at 1R
    - take_profit_2: 2.0_risk  # at 2R
    - take_profit_3: 3.0_risk  # at 3R (runner)
    
  filters:
    - min_volume: 1.2x_20d_avg
    - max_spread: 0.05%
    - no_news_event_within: 30min
```

## 4. Action Module — Risk Management

```yaml
risk_management:
  position_sizing:
    method: kelly_criterion
    fractional_kelly: 0.25  # 1/4 Kelly for safety
    max_position_size: 0.10  # 10% of portfolio
    max_total_exposure: 0.30  # 30% of portfolio
    
  drawdown_protection:
    max_daily_loss: 0.02  # 2%
    max_weekly_loss: 0.05  # 5%
    max_monthly_loss: 0.10  # 10%
    auto_pause_threshold: 0.08  # 8% drawdown
    
  stop_loss:
    type: atr_based
    atr_period: 14
    atr_multiplier: 1.5
    
  take_profit:
    type: risk_multiple
    targets: [1.0, 2.0, 3.0]
    partial_close: [0.33, 0.33, 0.34]
```

## 5. Monitoring & Logging

```yaml
monitoring:
  log_level: INFO
  log_destination: file  # execution_logs/
  metrics_destination: prometheus
  alert_thresholds:
    - daily_pnl: 0.05
    - win_rate_drop: 0.50
    - latency_high: 500  # ms
    
  dashboard:
    framework: plotly_dash
    refresh_rate: 5  # seconds
    url: http://localhost:8050
```

## 6. Compliance Configuration

```yaml
compliance:
  sfc_vasp:
    enabled: true
    audit_trail: true
    transaction_monitoring: true
    suspicious_activity_threshold: 0.10  # 10% portfolio
    
  pdpo:
    enabled: true
    data_retention: 7  # years
    pii_collected: false
    
  audit:
    decision_logs: 7_years
    trade_logs: 7_years
    performance_metrics: permanent
```

## 7. Model Parameters

```yaml
ml_models:
  lstm_price_prediction:
    enabled: true
    lookback: 60  # days
    features: [price, volume, rsi, macd, vwap]
    hidden_units: 64
    dropout: 0.2
    
  sentiment_analysis:
    enabled: true
    source: twitter_x
    model: distilbert-base-uncased
    update_frequency: 15min
```

---

## Environment Variables (.env, NOT in repo)

```bash
HASHKEY_API_KEY=your_key_here
HASHKEY_SECRET=your_secret_here
OPENCLAW_GATEWAY_URL=https://gateway.openclaw.ai
LOG_LEVEL=INFO
ENVIRONMENT=production
```

---

*Configuration last reviewed: 2026-06-06*
