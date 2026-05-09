# 3個月速成 PolyU MSc 自學計劃
## PolyU MSc in Economics (Applied Economics / Digital Economics)
## Weekend 階段 — 12 週完成

---

## 📋 PROGRAM OVERVIEW

**目標：** 完成後擁有完整 GitHub Portfolio + Research Paper + OpenClaw AI Trading Agent + Python ICT Dashboard，投身 HK Web3 行業

**時間：** 12 個週末（每週末 12–15 小時）

---

## 📚 12-WEEK STUDY PLAN — 官方 PolyU 科目

| Weekend | Phase | Subject | Main Resources | Task | Milestone |
|---------|-------|---------|----------------|------|-----------|
| 1–2 | Foundation | **AF5637** Microeconomics 微觀經濟學 | MIT OCW 14.01SC | 看4–5 Unit + 筆記 + Problem Set | Supply/Demand → Game Theory 所有習題 |
| 3–4 | Foundation | **AF5638** Macroeconomics 宏觀經濟學 | MIT OCW 14.02 | 看4–5 Unit + 畫AD-AS圖 + 香港GDP案例 | 掌握 GDP、Inflation、Monetary/Fiscal Policy |
| 5 | International + Managerial | **AF5642** International Economics + **AF5645** (Part 1) 國際經濟 + 管理經濟與數字轉型 | MIT OCW 14.54 + Coursera Digital Transformation (audit) | Trade model + AI對企業 case study | 寫1頁「香港數字轉型」報告 |
| 6–7 | Digital Core | **AF5645** (Part 2) + **AF5644** Advanced Topics in Digital Economics 管理經濟與數字轉型 + 數字經濟學進階 | 西南財經大學《數字經濟學》MOOC + Coursera Economics of AI | 每週末2–3章（平台經濟、數據價值化） | 完成quiz + 香港Digital Economy case study |
| 8 | Ethics + Digital Core | **AF5T21** Academic Integrity and Ethics in Business + **AF5644** 完結 商業道德與學術誠信 + 數字經濟學進階 | Coursera Business Ethics + MOOC | Ethics + Digital Economics 總結 | 寫500字 reflection + 拿 certificate |
| 9 | Core Elective 1 | **COMP5511** Artificial Intelligence Concepts 人工智能概念 | Coursera AI For Everyone – Andrew Ng | 完成4 module + AI應用討論 | 建1個mini AI use-case mindmap |
| 10 | Core Elective 2 | **AF5640** Metaverse Economics and Ecosystems 元宇宙經濟與生態 | Brookings Metaverse papers + Cathy Hackl YouTube | 讀3–4篇論文 + 商業模式研究 | 畫1個Metaverse Ecosystem mindmap |
| 11 | Free Elective | **AF5641** Econometrics for Data Analysis 計量經濟學數據分析 | MIT OCW Econometrics + Coursera | Regression + Google Colab Python練習 | 完成1個regression model（AI對就業影響） |
| 12 | Capstone | **AF5944** Research Project in Digital Economics 數字經濟學研究項目 | ICT Lectures + OpenClaw.ai + CoinGecko API | Paper + GitHub + OpenClaw Agent + Python Dashboard | 8–12頁 Research Paper + 完整 GitHub Portfolio |

---

## 🎯 FINAL DELIVERABLES

1. **Research Paper** (8–12 頁)
2. **GitHub Portfolio** 包含：
   - OpenClaw AI Trading Agent
   - Python ICT Dashboard
   - Data analysis notebooks
3. **Python Analysis** — Regression model + visualization

---

## 📝 WEEK 12 CAPSTONE — PAPER TEMPLATE + EXAMPLES

### Paper 題目（中英雙語）

**英文：** Applying Inner Circle Trader (ICT) Smart Money Concepts with OpenClaw AI Trading Agent to Hong Kong's Digital Economy and Web3 Markets: Bridging Traditional Finance, Digital Asset Strategies and Autonomous Execution

**中文：** ICT Smart Money Concepts 結合 OpenClaw AI Trading Agent 於香港數字經濟及 Web3 市場的應用 — 從傳統金融、數字資產交易策略到自主執行

### 大綱結構（8–12 頁 Word）

1. **Introduction** (1 頁)
2. **Literature Review** (2 頁)
3. **Theoretical Framework: ICT Smart Money Concepts + OpenClaw Agent Architecture** (2 頁)
4. **Analysis: ICT + OpenClaw in Hong Kong Crypto & Web3** (3–4 頁)
5. **Case Study & Python Empirical Analysis + OpenClaw Deployment** (2 頁)
6. **Conclusion & Policy Recommendations** (1 頁)
7. **References & Appendix**

---

### 📖 INTRODUCTION EXAMPLE

**英文：**
The rapid growth of Hong Kong's Web3 ecosystem, supported by the government's 2023–2026+ policy initiatives, has created new market structures in digital assets. This research applies Inner Circle Trader (ICT) Smart Money Concepts — originally taught in the 2016 Premiere Mentorship and updated in the 2026 Smart Money Lectures — together with the OpenClaw open-source AI agent framework to analyse how institutional "Smart Money" manipulates liquidity and how autonomous agents can execute ICT-based strategies in real time. By integrating PolyU's Digital Economics curriculum (AF5644, AF5640, AF5645), this paper demonstrates how ICT models + OpenClaw agents can enhance understanding and execution of digital transformation in finance.

**中文：**
香港Web3生態在政府2023–2026+政策支持下快速成長，創造了新的數字資產市場結構。本研究應用 Inner Circle Trader (ICT) Smart Money Concepts（源自2016 Premiere Mentorship並於2026最新講座更新）結合 OpenClaw 開源AI代理框架，分析機構「Smart Money」如何操縱流動性，以及自主代理如何即時執行ICT策略。結合 PolyU 數字經濟學課程（AF5644、AF5640、AF5645），本文展示 ICT 模型 + OpenClaw 代理如何提升對金融數字轉型的理解與執行。

---

### 📖 ANALYSIS EXAMPLE PARAGRAPH

**英文：**
According to ICT Lecture Month 1 (2016) and 2026 updates, Smart Money creates Order Blocks and Fair Value Gaps to engineer liquidity. In Hong Kong's crypto market, similar patterns appear in BTC-USD and ETH-USD during the 2024–2026 bull run on HashKey and OSL exchanges. By deploying an OpenClaw AI Trading Agent that consumes real-time ICT signals (via Python-generated Order Block / FVG detection), the agent can autonomously monitor liquidity grabs and execute paper trades, demonstrating a practical bridge between theoretical Digital Economics and executable Web3 strategies.

---

### 📚 REFERENCES FORMAT (APA / Harvard — PolyU 常用)

---

## 💻 PYTHON CODE EXERCISES

### 安裝指令
```bash
pip install yfinance pandas matplotlib plotly
```

### 練習 1：下載香港相關 Crypto 數據 + 簡單 Order Block 檢測

```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 下載 BTC-USD (香港Web3主要資產) + ETH-USD
data = yf.download(['BTC-USD', 'ETH-USD'], period='1y', interval='1d')['Close']
btc = data['BTC-USD'].dropna()

# 簡單 Order Block 檢測（Swing Low = Potential Bullish OB）
def find_order_blocks(price_series, window=5):
    ob = []
    for i in range(window, len(price_series)-window):
        if price_series.iloc[i] == price_series.iloc[i-window:i+window].min():  # Swing Low
            ob.append((price_series.index[i], price_series.iloc[i]))
    return ob

obs = find_order_blocks(btc)
print("Detected Potential Bullish Order Blocks (ICT):", obs[:5])

plt.figure(figsize=(12,6))
btc.plot(title='BTC-USD with Potential ICT Order Blocks (Hong Kong Web3 Context)')
for date, level in obs[:5]:
    plt.axhline(y=level, color='red', linestyle='--', alpha=0.7)
plt.legend()
plt.show()
```

---

### 練習 2：Fair Value Gap (FVG) 檢測（ICT 核心）

```python
def detect_fvg(df):
    fvg = []
    for i in range(1, len(df)-1):
        if df['High'].iloc[i-1] < df['Low'].iloc[i+1]:  # Gap Up
            fvg.append((df.index[i], df['High'].iloc[i-1], df['Low'].iloc[i+1], 'Bullish FVG'))
    return pd.DataFrame(fvg, columns=['Date', 'Top', 'Bottom', 'Type'])

btc_df = yf.download('BTC-USD', period='6mo')
fvg_df = detect_fvg(btc_df)
print("ICT Fair Value Gaps detected:\n", fvg_df.head())
```

---

### 練習 3：完整 ICT + 香港數據 Dashboard（Plotly） + 輸出 JSON 給 OpenClaw Agent

```python
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import json

# 下載 BTC-USD
btc = yf.download('BTC-USD', period='6mo')

# Order Block 檢測
def find_order_blocks(price_series, window=5):
    ob = []
    for i in range(window, len(price_series)-window):
        if price_series.iloc[i] == price_series.iloc[i-window:i+window].min():
            ob.append({'date': str(price_series.index[i]), 'level': float(price_series.iloc[i])})
    return ob[:5]

# FVG 檢測
def detect_fvg(df):
    fvg = []
    for i in range(1, len(df)-1):
        if df['High'].iloc[i-1] < df['Low'].iloc[i+1]:
            fvg.append({
                'date': str(df.index[i]),
                'top': float(df['High'].iloc[i-1]),
                'bottom': float(df['Low'].iloc[i+1]),
                'type': 'Bullish FVG'
            })
    return pd.DataFrame(fvg).head(5)

obs = find_order_blocks(btc['Close'])
fvg_df = detect_fvg(btc)

# 生成 signals.json 供 OpenClaw Agent
signals = {'order_blocks': obs, 'fvgs': fvg_df.to_dict('records')}
with open('signals.json', 'w') as f:
    json.dump(signals, f, indent=2)
print("signals.json generated for OpenClaw Agent!")

# 繪製 Dashboard
fig = go.Figure()
fig.add_trace(go.Scatter(x=btc.index, y=btc['Close'], name='BTC-USD', line=dict(color='blue')))
for ob in obs:
    fig.add_hline(y=ob['level'], line=dict(color='red', dash='dot'), annotation_text="OB")
fig.show()
```

---

## 🤖 OPENCLAW AI TRADING AGENT DEPLOYMENT (HK Web3 專用)

### Step 1: 安裝 OpenClaw
1. 前往 https://openclaw.ai → 下載 self-hosted 版本（GitHub openclaw/openclaw）
2. 安裝並啟動 gateway daemon（本地或 cloud VM）

### Step 2: 建立 Trading Skills

**Skill 1：** Fetch HK Web3 data (CoinGecko API / yfinance)

**Skill 2：** Run Python ICT script → generate Order Block / FVG signals

**Skill 3：** Execute paper-trade on HashKey/OSL demo API（或 Binance testnet）

### Step 3: 自然語言指令代理

> 「每天掃描 BTC-USD 和 ETH-USD 的 ICT Order Blocks 和 FVG，如果出現 liquidity grab 且 PolyU Digital Economics 指標正面，則自動執行 0.1% 倉位」

### Step 4: 部署後截圖
- agent dashboard
- 交易 log

放進 GitHub repo！

---

## 🏆 FINAL成果

| 成果 | 說明 |
|------|------|
| GitHub Portfolio | 所有週末作業 + Python ICT Dashboard + OpenClaw AI Trading Agent |
| Research Paper | 8–12頁（可直接投稿或投遞 HK Web3 公司）|
| OpenClaw AI Trading Agent | 可即時跑 ICT 策略於香港加密貨幣市場 |
| Python ICT Dashboard | 視覺化 + 自動化信號生成 |

---

## 📅 WEEKEND CRON SCHEDULE

| Cron | 時間 | 用途 |
|------|------|------|
| Fri 20:00 HKT | 12:00 UTC | 週末學習啟動提醒 |
| Sat 09:00 HKT | 01:00 UTC | 週末學習提醒 |
| Sun 10:00 HKT | 02:00 UTC | 進度檢查 + 下週預習 |

---

*Last updated: 2026-05-09*