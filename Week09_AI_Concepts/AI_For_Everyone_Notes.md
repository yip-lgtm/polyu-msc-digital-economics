# AI_For_Everyone_Notes.md

> **Coursera "AI For Everyone" by Andrew Ng**
> **PolyU COMP5511 | Week 9 | 2026年6月**

---

## Module 1: What is AI?

### 1.1 核心概念

**AI（Artificial Intelligence）：** 由機器展示嘅智能行為

**AI 嘅子集：**
- **Machine Learning（機器學習）：** 從數據中學習規律
- **Deep Learning（深度學習）：** 多層神經網絡
- **Data Science（數據科學）：** 從數據中提取洞見
- **Generative AI（生成式 AI）：** 創造新內容（文字、圖像、音樂）

### 1.2 AI vs ML vs DL

| 項目 | AI | Machine Learning | Deep Learning |
|------|----|-------------------|---------------|
| 定義 | 智能行為嘅總稱 | 從數據中學習 | 多層神經網絡 |
| 例子 | 專家系統、推薦 | 線性回歸、決策樹 | CNN、RNN、Transformer |
| 數據需求 | 不一定 | 中等 | 大量 |
| 計算力 | 低 | 中 | 高（GPU/TPU）|

### 1.3 監督式 vs 非監督式 vs 強化學習

- **Supervised（監督式）：** 有標籤數據 → 預測結果
  - 例子：垃圾郵件分類
- **Unsupervised（非監督式）：** 無標籤數據 → 發現模式
  - 例子：客戶分群
- **Reinforcement（強化學習）：** 試錯學習 → 最大化獎勵
  - 例子：AlphaGo、自動駕駛

### 1.4 AI 嘅現實應用

| 領域 | 應用 |
|------|------|
| **金融** | 信用評分、欺詐檢測、Algorithmic Trading |
| **醫療** | 影像診斷、藥物研發 |
| **零售** | 推薦系統、動態定價 |
| **製造** | 預測性維護、品質控制 |
| **交通** | 自駕車、路線優化 |
| **教育** | 個人化學習、自動評分 |

### 1.5 AI 嘅限制

- **數據飢餓：** 需要大量數據
- **偏見問題：** 訓練數據嘅偏見會被放大
- **可解釋性差：** 難以理解 AI 點做決定
- **邊界情況：** 未見過嘅場景可能出錯
- **計算成本：** 訓練大模型好貴

---

## Module 2: Building AI Projects

### 2.1 AI 項目流程（5 步）

```
Scoping → Data → Modeling → Deployment → Maintenance
   ↓         ↓         ↓            ↓             ↓
 界定範圍  收集數據  訓練模型    上線監控     持續更新
```

**Step 1: Scoping（界定範圍）**
- 解決咩問題？
- 呢個問題用 AI 啱唔啱？
- 預期 ROI 係幾多？
- 有咩替代方案？

**Step 2: Data（數據）**
- 邊度攞數據？
- 數據質量如何？
- 標註方法？
- 私隱同合規？

**Step 3: Modeling（建模）**
- 揀選算法
- 特徵工程
- 訓練 + 驗證 + 測試
- 調參

**Step 4: Deployment（部署）**
- 上線
- A/B Testing
- 監控表現
- 處理異常

**Step 5: Maintenance（維護）**
- 處理 model drift
- 持續更新數據
- 重新訓練

### 2.2 AI vs 傳統軟件

| 項目 | 傳統軟件 | AI |
|------|----------|-----|
| 邏輯 | 人工編寫 | 從數據學習 |
| 改進 | 改代碼 | 改數據 + 重新訓練 |
| 可解釋 | 高 | 低 |
| 邊界情況 | 明確 | 模糊 |

### 2.3 AI 項目常見失敗原因

1. **目標唔清晰：** 老闆想用 AI 但唔知做咩
2. **數據質量差：** 數據少、雜亂、有偏見
3. **期望過高：** 期望 AI 做所有嘢
4. **部署失敗：** PoC 成功但上線失敗
5. **維護不足：** Model drift 無人理

---

## Module 3: Building AI in Your Company

### 3.1 AI 轉型策略

**Pilot Project（試點項目）原則：**
- 由小規模開始
- 快速失敗、快速學習
- 揀有清晰 ROI 嘅項目
- 累積成功案例

**Build vs Buy 決策：**
- **Build：** 核心競爭力 + 有數據 + 有 talent
- **Buy：** 通用功能 + 唔係核心 + 想快

**香港企業 AI 應用現況：**

| 行業 | 應用 | 成熟度 |
|------|------|--------|
| **銀行** | AML、欺詐檢測、信用評分 | 高 |
| **保險** | 理賠自動化、精算 | 中 |
| **零售** | 推薦、動態定價 | 中 |
| **物流** | 路線優化、預測 | 中 |
| **政府** | 智慧城市、交通 | 低-中 |
| **醫療** | 影像、診斷 | 低-中 |

### 3.2 AI 項目嘅 5 個角色

| 角色 | 責任 |
|------|------|
| **Domain Expert** | 理解問題 + 提供洞見 |
| **Data Engineer** | 收集 + 處理 + 儲存數據 |
| **ML Engineer** | 訓練 + 部署 + 維護模型 |
| **ML Researcher** | 研究新算法 |
| **AI Product Manager** | 統籌 + 訂立優先級 |

### 3.3 AI 採用嘅障礙

- **數據孤島：** 部門之間唔共享數據
- **人才短缺：** 數據科學家 + ML 工程師難請
- **私隱顧慮：** PDPO + GDPR 限制
- **監管不明：** 尤其係金融 + 醫療
- **文化阻力：** 員工怕被 AI 取代

### 3.4 香港 AI 政策

- 2017 年《香港智慧城市藍圖》
- 2022 年《創新及科技發展藍圖》
- 創新及科技基金（ITF）：HK$200 億
- 數碼港 AI/Web3 Hub
- InnoHK 創新香港研發平台

---

## Module 4: AI and Society

### 4.1 AI 嘅社會影響

**正面：**
- 生產力提升
- 新工作機會
- 醫療突破
- 教育個人化

**負面：**
- 就業取代
- 私隱侵犯
- 算法偏見
- 數字鴻溝

### 4.2 AI 倫理 5 大原則

1. **Fairness（公平）：** 不歧視弱勢群體
2. **Transparency（透明）：** 決策可解釋
3. **Privacy（私隱）：** 保護用戶數據
4. **Accountability（問責）：** 明確責任
5. **Safety（安全）：** 不傷害人

### 4.3 與 Week 8 Ethics 連結

| Week 8 概念 | Week 9 應用 |
|--------------|------------|
| 數據倫理 | AI 訓練數據 |
| 算法倫理 | AI 模型偏見 |
| 平台責任 | AI 應用責任 |
| Web3 倫理 | AI + Crypto |

### 4.4 AI 對香港 Web3 嘅影響

| 應用 | 描述 |
|------|------|
| **Algorithmic Trading** | ICT Smart Money + AI |
| **AI Trading Agent** | OpenClaw + Python |
| **AML/KYC** | 自動化合規 |
| **Robo-advisor** | Web3 投資建議 |
| **Smart Contract Audit** | AI 漏洞檢測 |
| **DAO Governance** | AI 輔助決策 |

### 4.5 AI + Web3 整合案例

- **Numerai：** 數據科學家 + 對沖基金 + 區塊鏈
- **SingularityNET：** 去中心化 AI 服務市場
- **Ocean Protocol：** 數據 tokenization
- **Render Network：** GPU 渲染去中心化
- **Fetch.ai：** AI 代理經濟

### 4.6 EU AI Act vs 香港

| 風險級別 | EU AI Act | 香港（暫無統一法規）|
|----------|-----------|---------------------|
| 不可接受 | 禁止（社會評分、實時人臉識別）| — |
| 高風險 | 嚴格要求（招聘、貸款、執法、醫療）| — |
| 有限風險 | 披露要求（ChatBot）| — |
| 極低風險 | 無要求（垃圾郵件過濾）| — |
| 罰則 | €35M 或 7% 營業額 | 暫無 |

---

## Capstone Paper 連結（AF5944）

AI 概念為 Capstone Paper 提供基礎：

1. **AI + Trading：** OpenClaw AI Trading Agent 嘅技術基礎
2. **AI 倫理：** Trading Agent 嘅透明度 + 公平性
3. **AI + Web3：** 香港 Web3 市場嘅 AI 應用案例
4. **AI 政策：** 香港 vs EU 嘅 AI 監管對比
5. **AI 採用障礙：** 香港 Web3 公司面對嘅挑戰

---

## 必記關鍵詞

- AI / ML / DL
- Supervised / Unsupervised / Reinforcement
- Scoping / Data / Modeling / Deployment / Maintenance
- Algorithmic Bias / Fairness
- Explainable AI (XAI)
- AML / KYC
- Generative AI / LLM
- EU AI Act
- DAO + AI
- ICT Smart Money + AI

---

## 📚 Resources

- Coursera AI For Everyone: https://www.coursera.org/learn/ai-for-everyone
- Andrew Ng: https://www.andrewng.org/
- DeepLearning.AI: https://www.deeplearning.ai/
- HK AI Lab: https://www.hkailab.com/
- OpenClaw.ai: https://openclaw.ai

---

*Reference: 3個月速成 PolyU MSc 自學計劃 — Week 9 COMP5511*
