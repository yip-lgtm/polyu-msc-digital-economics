# Regression Results Interpretation — AI 對就業影響模型

> **PolyU AF5641 Econometrics | Week 11 | 2026年6月**
> **對應 Notebook: `AI_Employment_Regression_Model.ipynb`**

---

## 1. 模型設定

### 1.1 研究問題

**The Impact of AI Adoption on Workforce Changes in Companies**

> 探討公司層級嘅 AI 採用程度、自動化率、公司規模如何影響員工數變化。

### 1.2 假設

| 假設 | 描述 | 預期係數符號 |
|------|------|--------------|
| **H1** | AI 採用程度 ↑ → 員工數變化 | +（擴張）/ -（取代）|
| **H2** | 自動化率 ↑ → 員工數變化 | -（取代效應）|
| **H3** | 公司規模大 → 員工數變化 | +（更多投資）|

### 1.3 模型公式

```
Workforce_Change = β₀ + β₁·AI_Adoption_Level_Medium 
                         + β₂·AI_Adoption_Level_High
                         + β₃·Automation_Rate 
                         + β₄·Company_Size 
                         + ε
```

### 1.4 變量定義

| 變量 | 類型 | 定義 |
|------|------|------|
| **Workforce_Change** | 連續 | 員工數變化百分比 |
| **AI_Adoption_Level_Medium** | 虛擬 | 1 = 中度採用 AI，0 = 低度 |
| **AI_Adoption_Level_High** | 虛擬 | 1 = 高度採用 AI，0 = 低度 |
| **Automation_Rate** | 連續 | 自動化率（%）|
| **Company_Size** | 連續 | 公司規模（員工數）|

---

## 2. 估計方法

### 2.1 OLS with HC3 Robust Standard Errors

```python
model = sm.OLS(y, X).fit(cov_type='HC3')
```

**點解用 HC3：**
- 修正異方差性（Heteroskedasticity）
- 對觀察值中嘅極端值更穩健
- 學術界 + 業界標準做法

### 2.2 OLS 假設

| 假設 | 檢測方法 | 預期結果 |
|------|----------|----------|
| 線性 | 殘差 vs 擬合值 | 隨機散佈 |
| 多重共線性 | VIF | VIF < 10 |
| 同方差性 | Breusch-Pagan | p > 0.05 |
| 自相關 | Durbin-Watson | DW ≈ 2 |
| 常態性 | Q-Q Plot / JB | 接近對角線 |

---

## 3. 結果解讀範例（基於模擬數據）

### 3.1 估計結果

```
                            OLS Regression Results (HC3 Robust)
==============================================================================
Dep. Variable:        Workforce_Change   R-squared:                       0.785
Model:                                OLS   Adj. R-squared:                  0.768
Method:                     Least Squares   F-statistic:                     41.62
No. Observations:                      50   Prob (F-statistic):           1.23e-15
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -2.4508     0.823     -2.978      0.005      -4.107      -0.795
AI_Adoption_M   0.8120     0.234      3.470      0.001       0.343       1.281
AI_Adoption_H   1.5240     0.298      5.114      0.000       0.926       2.122
Automation_R   -0.0298     0.011     -2.709      0.010      -0.052      -0.008
Company_Size    0.0001     0.000      0.892      0.378      -0.000       0.000
==============================================================================
```

### 3.2 係數解釋

| 變量 | 係數 | 解釋 |
|------|------|------|
| **AI_Adoption_Level_Medium** | +0.812 | 對比低度採用 AI 嘅公司，中度採用嘅公司員工數平均增加 0.81% |
| **AI_Adoption_Level_High** | +1.524 | 高度採用 AI 嘅公司員工數平均增加 1.52%（顯著 p<0.001）|
| **Automation_Rate** | -0.030 | 自動化率每升 1%，員工數下降 0.03%（顯著 p<0.05）|
| **Company_Size** | +0.0001 | 公司規模影響唔顯著 |

### 3.3 假設檢定結果

| 假設 | 結果 | 結論 |
|------|------|------|
| **H1a** AI 中度採用 | +0.812 (p=0.001) | ✅ 統計顯著正向 |
| **H1b** AI 高度採用 | +1.524 (p<0.001) | ✅ 統計顯著正向 |
| **H2** 自動化率 | -0.030 (p=0.010) | ✅ 統計顯著負向 |
| **H3** 公司規模 | +0.0001 (p=0.378) | ❌ 統計唔顯著 |

---

## 4. 經濟意義

### 4.1 主要發現

1. **AI 採用對就業嘅淨效應為正**
   - 中度採用：+0.81%
   - 高度採用：+1.52%
   - 反映 AI 創造新職位 > 取代舊職位

2. **自動化率對就業有負面影響**
   - 每升 1% 自動化率 → -0.03% 員工
   - 反映取代效應

3. **公司規模影響唔顯著**
   - 大小公司都能受惠於 AI

### 4.2 政策建議

1. **支持 AI 採用：** 政府可提供補貼鼓勵企業採用 AI
2. **再培訓計劃：** 自動化率高嘅行業需配套再培訓
3. **無分大小：** 中小企也應採用 AI

### 4.3 與 Capstone Paper 連結

呢個模型為 Capstone Paper 提供：
- **方法論基礎：** OLS + HC3 Robust SE
- **實證證據：** AI 對經濟嘅影響
- **政策框架：** 支援 + 再培訓 + 普及

---

## 5. 模型診斷結果

### 5.1 VIF（多重共線性）

| 變量 | VIF | 判斷 |
|------|-----|------|
| const | 0.00 | — |
| AI_Adoption_Medium | 1.42 | ✅ 良好 |
| AI_Adoption_High | 1.55 | ✅ 良好 |
| Automation_Rate | 1.12 | ✅ 良好 |
| Company_Size | 1.08 | ✅ 良好 |

**結論：** 所有 VIF < 10，無多重共線性問題。

### 5.2 Breusch-Pagan（同方差性）

- LM 統計量 = 2.34
- p-value = 0.673
- **結論：** p > 0.05，接受同方差性假設 ✅

### 5.3 Durbin-Watson（自相關）

- DW = 1.97
- **結論：** 接近 2，無自相關 ✅

### 5.4 常態性

- Jarque-Bera p-value = 0.234
- Q-Q Plot 接近對角線
- **結論：** 殘差近似常態分佈 ✅

---

## 6. 報告寫作（Capstone Paper 章節模板）

### 6.1 章節結構

**Chapter 4: Empirical Analysis**

#### 4.1 Data
- 數據來源
- 樣本規模
- 變量定義

#### 4.2 Methodology
- OLS 模型
- Robust SE
- 診斷測試

#### 4.3 Results
- 描述性統計
- 相關性分析
- 迴歸結果

#### 4.4 Discussion
- 經濟意義
- 政策建議
- 限制

### 6.2 引用範例

> "Using OLS regression with HC3 robust standard errors, we find that AI adoption has a positive and statistically significant effect on workforce changes (β = 1.524, p < 0.001). Conversely, automation rate has a negative effect (β = -0.030, p = 0.010), suggesting that while AI creates new jobs, automation displaces existing ones. The model explains 78.5% of the variance (R² = 0.785)."

---

## 7. 可擴展方向（Capstone Paper 增強）

### 7.1 增加變量
- 行業固定效應
- 國家固定效應
- 時間趨勢
- 交互項（AI × 行業）

### 7.2 使用 Panel Data
- 公司層級多年度數據
- Fixed Effects / Random Effects
- 控制不可觀察嘅異質性

### 7.3 內生性處理
- Instrumental Variable (IV)
- Difference-in-Differences (DiD)
- Regression Discontinuity

### 7.4 ICT Smart Money 應用
- 將 AI 採用擴展到 Trading Agent
- 測試 ICT 信號 + AI 嘅互補效應
- 套用到加密貨幣市場

---

## 8. 必記關鍵詞

- OLS / HC3 Robust SE
- Workforce Change / AI Adoption
- Heteroskedasticity / Multicollinearity
- VIF / Breusch-Pagan / Durbin-Watson
- Causal Inference
- Fixed Effects / Panel Data
- Ceteris Paribus
- Coefficient Interpretation
- Statistical Significance
- Economic Significance

---

## 📚 Resources

- MIT OCW 14.32: https://ocw.mit.edu/courses/14-32-econometrics-spring-2007/
- Wooldridge Textbook
- statsmodels: https://www.statsmodels.org/
- Kaggle: https://www.kaggle.com/
- World Bank: https://data.worldbank.org/

---

*Reference: 3個月速成 PolyU MSc 自學計劃 — Week 11 AF5641 Econometrics*
