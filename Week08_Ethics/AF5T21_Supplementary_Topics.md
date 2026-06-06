# AF5T21 補充主題：ESG、AI 倫理、Web3 倫理（詳細版）

> **PolyU MSc | Week 8 | 2026年6月版**
> **姓名： __________________________  日期： __________________________**

---

## 1. ESG in Digital Economy（數字經濟中的 ESG）

### 1.1 三大支柱

#### E（Environmental 環境）
- **數據中心能耗：** 全球數據中心用電量佔全球 1-2%
- **AI 訓練的碳排放：** 訓練一個大型 AI 模型可產生數百噸 CO₂
- **電子廢棄物：** 硬件報廢 + 加密挖礦設備
- **綠色 Web3：** 碳中和區塊鏈（Algorand、Cardano）

#### S（Social 社會）
- **算法偏見對弱勢群體的影響：** 招聘 AI、貸款 AI、醫療 AI
- **平台工作者（外送員、司機）的勞動權益：** 缺乏社保、最低工資保障
- **數字鴻溝：** 老年人、貧困戶、偏遠地區缺乏數字接入
- **內容審查：** 假新聞、仇恨言論、深度偽造

#### G（Governance 管治）
- **數據治理：** 數據使用、透明性、安全性
- **算法透明度：** 黑盒 vs 白盒
- **平台反壟斷：** 自我優待、扼殺式收購
- **董事會對科技風險的監督：** AI 風險、網絡安全
- **ESG 報告：** 港交所要求上市公司披露

### 1.2 香港相關

- **港交所 ESG 報告：** 越來越嚴，2018 年起上市公司必須披露
- **Cyberport / 數碼港：** 評估 startup 嘅 ESG 表現
- **Web3 項目：** 需考慮「可持續發展」敘事（綠色比特幣 ESG 基金）
- **綠色金融：** 政府發行綠色債券，支持 ESG 項目

### 1.3 ESG vs CSR

| 項目 | CSR | ESG |
|------|-----|-----|
| **範圍** | 企業社會責任（廣）| 環境 + 社會 + 管治（可量化）|
| **披露** | 自願 | 強制（上市公司）|
| **評估** | 質性 | 量化 + 第三方評級 |
| **投資** | 影響力投資 | 機構投資者必看 |

---

## 2. AI Ethics（AI 倫理）

### 2.1 5 大議題

#### (1) Algorithmic Bias（算法偏見）
- AI 模型可能放大既有社會偏見
- **例子：** 招聘 AI 歧視女性、貸款 AI 歧視少數族裔、內容推薦 AI 助長假新聞
- **解決方法：** 多元化訓練數據 + 公平性審計 + 多學科團隊

#### (2) Transparency & Explainability（透明度 + 可解釋性）
- 黑箱算法嘅問題：「為什麼我被拒絕貸款？」
- **GDPR 規定：** 自動決策必須可解釋
- **解決方法：** Explainable AI (XAI) + Model Cards + Datasheets

#### (3) Accountability（問責）
- 當 AI 造成傷害時，責任歸屬？
- 開發者？部署者？使用者？監管機構？
- **案例：** Tesla Autopilot 事故、Uber 自駕車致命意外
- **解決方法：** 明確法律框架 + 保險機制

#### (4) Job Displacement（就業取代）
- AI 對就業結構嘅衝擊
- 預計 30-40% 工作可能被自動化
- **再培訓責任：** 政府 + 企業 + 個人
- **解決方法：** 終身學習 + UBI 討論

#### (5) Privacy（私隱）
- AI 訓練需要大量數據
- 與 PDPO / GDPR 可能衝突
- **解決方法：** Federated Learning + Differential Privacy

### 2.2 香港視角

- 政府推動 AI 應用（智慧城市、醫療 AI、金融 AI）
- 尚未有全面 AI 倫理框架
- 建議參考 **EU AI Act** 嘅風險分類思路
  - 不可接受風險：社會評分、實時人臉識別
  - 高風險：招聘、貸款、執法、醫療
  - 有限風險：ChatBot、生成內容
  - 極低風險：垃圾郵件過濾

### 2.3 EU AI Act vs 香港

| 項目 | EU AI Act | 香港 |
|------|-----------|------|
| **法律地位** | 已通過 | 暫無統一法規 |
| **風險分類** | 4 級 | 暫無 |
| **罰則** | 最高 €35M 或 7% 營業額 | 暫無 |
| **執行** | 歐盟 AI Office | 創新及科技局（ITIB）|

---

## 3. Web3 Ethics（Web3 倫理）

### 3.1 5 大議題

#### (1) Investor Protection（投資者保護）
- 散戶 vs 機構資訊不對等
- 高風險產品（加密貨幣波動性大）
- 騙案頻生（PlusToken、FTX 倒閉）
- **解決方法：** KYC + 適當性評估 + 投資者教育

#### (2) Market Manipulation（市場操縱）
- **Pump and Dump：** 人為推高價格後拋售
- **Wash Trading：** 自己買自己賣製造假成交量
- **Spoofing：** 製造假買單
- **解決方法：** On-chain 分析 + 監管科技 (RegTech)

#### (3) DAO Governance（去中心化自治組織治理）
- **一幣一票 vs 一人一票**
- 鯨魚（whale）操縱
- 治理攻擊（51% attack）
- **案例：** The DAO 2016 事件、Compound 提案被攻擊
- **解決方法：** 二次方投票 + 委託投票 + 時間鎖

#### (4) Smart Contract Risk（智能合約風險）
- 代碼漏洞導致資金被盜
- **案例：** The DAO 2016、Parity Wallet 2017、Poly Network 2021
- **解決方法：** 形式化驗證 + 漏洞賞金 + 保險

#### (5) Environmental Impact（環境影響）
- PoW（工作量證明）能耗高（比特幣）
- PoS（權益證明）較環保（以太坊 2.0）
- **解決方法：** 轉向 PoS + 碳中和

### 3.2 香港 Web3 監管框架

- **VASP 牌照**（2023 生效）
- **穩定幣條例**（2025 生效）
- **現貨 ETF**（2024 批准）
- **沙盒機制**（Fintech 試點）
- **零售投資者保護**（適當性評估 + 風險聲明）

### 3.3 Web3 倫理論證

| 立場 | 觀點 | 倫理框架 |
|------|------|----------|
| **支持** | 去中心化 = 個人賦權 | 美德倫理（自由、責任）|
| **反對** | 監管不足、騙案 | 正義論（保護弱勢）|
| **中立** | 平衡創新 + 監管 | 利益相關者理論 |

---

## 4. ESG + AI + Web3 整合

### 4.1 AI 對 ESG 嘅影響

- **E：** AI 優化能源效率、智能電網
- **S：** AI 預測社會風險、公平性審計
- **G：** AI 監察合規、檢測欺詐

### 4.2 Web3 對 ESG 嘅影響

- **E：** 碳信用 tokenization、綠色債券
- **S：** 去中心化金融包容性
- **G：** DAO 治理透明度

### 4.3 AI + Web3 整合案例

- **智能合約審計：** AI 自動檢測漏洞
- **去中心化 AI：** 數據 + 模型 + 治理去中心化
- **AI 預測市場：** 結合預測市場 + AI 模型

---

## 5. Capstone Paper 連結（AF5944）

呢啲補充主題同 Capstone Paper 高度相關：

1. **ICT Smart Money Concepts** — 演算法交易嘅 AI 倫理
2. **OpenClaw AI Trading Agent** — 透明度、問責、公平性
3. **Web3 市場** — 去中心化、DAO 治理、投資者保護
4. **ESG** — 綠色金融、可持續發展
5. **香港數字經濟** — 監管框架 + 國際競爭

---

## 必記關鍵詞

- ESG (E + S + G)
- Algorithmic Bias / Fairness
- Explainable AI (XAI)
- GDPR / EU AI Act
- DAO Governance
- Smart Contract Risk
- PoW vs PoS
- VASP / 穩定幣
- Carbon Neutral Blockchain
- Federated Learning
- Differential Privacy
- Investor Protection

---

## 📚 Resources

- 港交所 ESG: https://www.hkex.com.hk/
- EU AI Act: https://artificialintelligenceact.eu/
- PCPD: https://www.pcpd.org.hk/
- SFC: https://www.sfc.hk/
- HKMA e-HKD: https://www.hkma.gov.hk/
- 西南財經 ESG MOOC: https://www.icourse163.org/

---

*Reference: 3個月速成 PolyU MSc 自學計劃 — Week 8 AF5T21 補充主題*
