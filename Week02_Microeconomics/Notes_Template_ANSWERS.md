# AF5637 Microeconomics — Game Theory 手寫筆記模板（答案版）

> **對照手寫版** — 用嚟對照自己手寫嘅筆記
> **姓名： __________________________  日期： __________________________**

---

## 核心概念

**1. Game Theory 研究什麼？**

研究策略互動（strategic interaction），即決策者之間互相影響的決策情況。

**2. Prisoner's Dilemma 的經典結果：**

即使合作對雙方最好，但理性自利下雙方都會選擇背叛，導致雙輸均衡。

**3. Nash Equilibrium 定義：**

每個玩家都選擇對自己最好的策略，假設對手也這樣做，沒有人想單方面改變策略。

**4. Dominant Strategy 定義：**

無論對手選擇什麼，該策略對自己都是最好的。

**5. Repeated Game 為什麼可能出現合作？**

在重複博弈中，玩家重視未來回報，可能透過 Tit-for-Tat 等策略維持合作。

**6. Payoff Matrix 是什麼？**

用表格顯示每個玩家在不同策略組合下的收益（payoff）。

---

## Prisoner's Dilemma Payoff Matrix

|       | 合作        | 背叛        |
|-------|------------|------------|
| **合作** | (  3,  3  ) | (  0,  5  ) |
| **背叛** | (  5,  0  ) | (  1,  1  ) |

> 解讀：
> - (合作, 合作) → 雙贏 (3, 3)
> - (合作, 背叛) → 對手贏 (0, 5)
> - (背叛, 合作) → 自己贏 (5, 0)
> - (背叛, 背叛) → 雙輸 (1, 1)
>
> **Nash Equilibrium = (背叛, 背叛)**

---

## 香港寡頭市場案例分析

### 香港地產商（New World / CK Asset / Henderson）

| Item | 分析 |
|------|------|
| 市場結構 | **寡頭市場** |
| 策略互動類型 | 價格博弈（Pricing Game） |
| Nash Equilibrium 結果 | 高價均衡（互相跟價） |
| 你的分析 | 雖然合作（共同減慢推盤）對大家更好，但理性下傾向高價出售，導致樓價長期高企。 |

---

### 香港銀行（HSBC / Hang Seng / Bank of China）

| Item | 分析 |
|------|------|
| 市場結構 | **寡頭市場** |
| 策略互動類型 | 利率博弈 |
| Dominant Strategy | 跟隨減息 |
| 你的分析 | 大家都減息搶客 → 整體利潤下降，類似 Prisoner's Dilemma。 |

---

### 電訊商（CMHK / 3HK / Smartone）

| Item | 分析 |
|------|------|
| 市場結構 | **寡頭市場** |
| 策略互動類型 | 價格戰 + Repeated Game |
| Repeated Game 策略 | Tit-for-Tat（你減我跟，你加我跟） |
| 你的分析 | 短期可能減價搶客，但長期傾向回復相對穩定價格。 |

---

## 📊 進階 Game Theory 概念

| 概念 | 應用 |
|------|------|
| **Cartel (卡特爾)** | 寡頭壟斷聯合定價（如 OPEC）|
| **Price Leadership** | 主導者定價，其他跟隨 |
| **Entry Deterrence** | 阻止新對手進入市場 |
| **Tacit Collusion** | 默契合作（不公開協議）|

---

## 🏢 香港市場實際案例

- **地產：** 領展（Link REIT）+ 領展收購策略
- **銀行：** 滙豐（HSBC）利率政策
- **電訊：** 5G 頻譜拍賣 + 共用網絡
- **航空：** 國泰 + HK Express 票價博弈
- **外賣平台：** Foodpanda / Deliveroo 補貼戰

---

## 📚 MIT OCW Resources

- **Game Theory Lecture:** https://ocw.mit.edu/courses/14-12/
- **HK Oligopoly Case Study:** https://www.gov.hk/

---

*Reference: 3個月速成 PolyU MSc 自學計劃*
