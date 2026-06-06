# AF5641 — Econometrics for Data Analysis 手寫筆記模板

> **列印友好格式** — A4 / 12pt / 1.5 行距
> **姓名： __________________________  日期： __________________________**

---

## 1. Econometrics 基礎

**1. 定義：**

> Econometrics = Economic Theory + Mathematics + Statistics

- 用統計方法驗證經濟理論
- 從數據中估計經濟關係
- 預測 + 因果推斷

**2. 3 大步驟：**

1. **模型設定（Model Specification）：** Y = β₀ + β₁X + ε
2. **參數估計（Estimation）：** OLS / MLE / GMM
3. **假設檢定（Hypothesis Testing）：** t-test, F-test, p-value

**3. 主要軟件：**

- **Python：** statsmodels, scikit-learn, linearmodels
- **R：** lm, plm, fixest
- **Stata：** reg, xtreg, areg
- **EViews：** 金融時間序列
- **MATLAB：** 計量經濟學

---

## 2. OLS (Ordinary Least Squares) 線性回歸

**1. 簡單線性回歸：**

$$Y = \beta_0 + \beta_1 X + \varepsilon$$

- **Y：** 應變量（Dependent Variable）
- **X：** 自變量（Independent Variable）
- **β₀：** 截距（Intercept）
- **β₁：** 斜率（Slope）
- **ε：** 誤差項（Error Term）

**2. OLS 假設（Gauss-Markov）：**

1. 線性關係
2. 隨機抽樣
3. 無多重共線性
4. 同方差性（Homoscedasticity）
5. 無自相關（No Autocorrelation）
6. 誤差項常態分佈

**3. 多元回歸：**

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k + \varepsilon$$

- 控制多個變量
- 估計邊際效應
- ceteris paribus（其他不變）

**4. 重要指標：**

- **R²：** 解釋力（0-1）
- **Adjusted R²：** 調整後解釋力
- **F-statistic：** 整體顯著性
- **t-statistic：** 個別變量顯著性
- **p-value：** 顯著性概率
- **Standard Error：** 標準誤

---

## 3. OLS 估計步驟（Python）

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 加載數據
df = pd.read_csv('data.csv')

# 2. 設定 X 和 Y
X = df[['X1', 'X2', 'X3']]
y = df['Y']

# 3. 加常數項
X = sm.add_constant(X)

# 4. OLS 估計
model = sm.OLS(y, X).fit()

# 5. 結果摘要
print(model.summary())

# 6. 預測
predictions = model.predict(X)

# 7. 殘差分析
residuals = model.resid

# 8. 視覺化
plt.scatter(y, predictions)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()
```

---

## 4. 模型診斷（Diagnostic Tests）

**1. 多重共線性（Multicollinearity）：**

- VIF (Variance Inflation Factor) > 10 = 嚴重
- 解決：刪除變量 / 主成分分析 / 正則化

**2. 同方差性（Homoscedasticity）：**

- Breusch-Pagan Test
- White Test
- 解決：稳健標準誤 / 加權最小二乘

**3. 自相關（Autocorrelation）：**

- Durbin-Watson Test
- 解決：GLS / Newey-West

**4. 常態性（Normality）：**

- Jarque-Bera Test
- Q-Q Plot
- 解決：對數轉換 / Box-Cox

---

## 5. 推薦主題（Capstone Paper 方向）

### 主題 A：AI 對就業嘅影響

**自變量 X：**
- AI 投資額
- 自動化程度
- 行業 AI 滲透率

**應變量 Y：**
- 就業增長率
- 工資水平
- 失業率

**數據來源：**
- World Bank
- OECD
- IMF
- McKinsey Global Institute

### 主題 B：Digital Economy 對 GDP 嘅影響

**自變量 X：**
- 數字經濟佔 GDP 比率
- 互聯網普及率
- 金融科技發展指數

**應變量 Y：**
- 實質 GDP 增長
- 人均 GDP
- 全要素生產率

**數據來源：**
- 中國國家統計局
- Hong Kong Census
- World Bank Digital Adoption Index

### 主題 C：Web3 對金融包容性嘅影響

**自變量 X：**
- DeFi 用戶數
- 加密貨幣採用率
- VASP 牌照數

**應變量 Y：**
- 銀行帳戶滲透率
- 跨境支付成本
- 金融服務可得性

**數據來源：**
- World Bank Findex
- Chainalysis
- Statista

### 主題 D：ICT Smart Money 對加密貨幣回報嘅影響

**自變量 X：**
- Order Block 信號強度
- Fair Value Gap 大小
- Liquidity Sweep 頻率

**應變量 Y：**
- 月度回報率
- Sharpe Ratio
- 最大回撤

**數據來源：**
- yfinance
- Binance API
- CoinGecko

---

## 6. Python 模板：AI 對就業影響 Regression

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# ===== 1. 數據準備 =====
# 模擬數據（實際可從 World Bank / OECD 取得）
np.random.seed(42)
n = 50

data = {
    'Country': [f'Country_{i}' for i in range(1, n+1)],
    'AI_Investment_USD_B': np.random.uniform(0.1, 50, n),
    'Automation_Rate_Pct': np.random.uniform(10, 80, n),
    'Internet_Penetration_Pct': np.random.uniform(50, 99, n),
    'Education_Index': np.random.uniform(0.5, 0.95, n),
    'Employment_Growth_Pct': np.random.uniform(-2, 5, n),
}

df = pd.DataFrame(data)

# 模擬：AI 投資 ↑ 就業 ↑ (0.05 * AI)
# 自動化 ↑ 就業 ↓ (-0.03 * Auto)
# 互聯網 ↑ 就業 ↑ (0.02 * Internet)
# 教育 ↑ 就業 ↑ (0.5 * Education)
df['Employment_Growth_Pct'] = (
    0.05 * df['AI_Investment_USD_B'] 
    - 0.03 * df['Automation_Rate_Pct']
    + 0.02 * df['Internet_Penetration_Pct']
    + 0.5 * df['Education_Index']
    + np.random.normal(0, 1, n)
)

# ===== 2. EDA =====
print(df.describe())
print(df.corr())

# 散佈圖矩陣
sns.pairplot(df[['AI_Investment_USD_B', 'Automation_Rate_Pct', 
                  'Internet_Penetration_Pct', 'Education_Index',
                  'Employment_Growth_Pct']])
plt.show()

# ===== 3. OLS Regression =====
X = df[['AI_Investment_USD_B', 'Automation_Rate_Pct', 
        'Internet_Penetration_Pct', 'Education_Index']]
y = df['Employment_Growth_Pct']
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())

# ===== 4. 診斷 =====
# 殘差分析
residuals = model.resid
fitted = model.fittedvalues

# Q-Q Plot
sm.qqplot(residuals, line='45')
plt.title('Q-Q Plot of Residuals')
plt.show()

# 殘差 vs 擬合值
plt.scatter(fitted, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted')
plt.show()

# VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = pd.DataFrame()
vif['Variable'] = X.columns
vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif)

# ===== 5. 預測 =====
df['Predicted_Employment_Growth'] = model.predict(X)
df['Residual'] = model.resid

# 視覺化
plt.figure(figsize=(10, 6))
plt.scatter(df['Predicted_Employment_Growth'], df['Employment_Growth_Pct'])
plt.plot([df['Employment_Growth_Pct'].min(), df['Employment_Growth_Pct'].max()],
         [df['Employment_Growth_Pct'].min(), df['Employment_Growth_Pct'].max()],
         'r--')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Actual vs Predicted Employment Growth')
plt.show()
```

---

## 7. 結果解釋範例

```
                            OLS Regression Results
==============================================================================
Dep. Variable:     Employment_Growth_Pct   R-squared:                       0.785
Model:                                OLS   Adj. R-squared:                  0.768
Method:                     Least Squares   F-statistic:                     41.62
No. Observations:                      50   Prob (F-statistic):           1.23e-15
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -2.4508     0.823     -2.978      0.005      -4.107      -0.795
AI_Invest...    0.0512     0.008      6.400      0.000       0.035       0.067
Automation...  -0.0298     0.011     -2.709      0.010      -0.052      -0.008
Internet_Pe...  0.0198     0.009      2.200      0.033       0.002       0.038
Education_I...  0.5123     0.156      3.284      0.002       0.198       0.827
==============================================================================
```

**解釋：**
- **R² = 0.785：** 78.5% 嘅變異可由呢 4 個變量解釋
- **AI 投資係數 = 0.0512：** AI 投資每增加 10 億美元，就業增長率上升 0.51 個百分點
- **自動化係數 = -0.0298：** 自動化率每升 1%，就業增長率下降 0.03 個百分點
- **所有 p-value < 0.05：** 統計上顯著

---

## 8. 報告寫作結構

**1. 引言（Introduction）**
- 研究問題
- 假設
- 重要性

**2. 文獻回顧（Literature Review）**
- AI + 就業 過往研究
- 自動化對勞動力市場影響
- 政策回應

**3. 數據 + 方法（Data + Methodology）**
- 數據來源
- 變量定義
- OLS 模型設定

**4. 結果（Results）**
- 描述性統計
- 相關性分析
- 迴歸結果
- 診斷測試

**5. 討論（Discussion）**
- 經濟意義
- 政策建議
- 限制

**6. 結論（Conclusion）**
- 主要發現
- 未來研究方向

---

## 9. 必記關鍵詞

- OLS / MLE / GMM
- R² / Adjusted R²
- t-test / F-test / p-value
- Multicollinearity / VIF
- Heteroscedasticity / Breusch-Pagan
- Autocorrelation / Durbin-Watson
- Endogeneity / Instrumental Variable
- Fixed Effects / Random Effects
- Panel Data
- Time Series
- Stationarity / Unit Root
- Cointegration
- Ceteris Paribus
- Robust Standard Errors
- Causal Inference

---

## 📚 Resources

- MIT OCW Econometrics: https://ocw.mit.edu/courses/14-381-statistical-method-in-economics-fall-2018/
- Wooldridge Introductory Econometrics: https://www.cengage.com/c/introductory-econometrics-a-modern-approach-7e-wooldridge/9781337558860/
- statsmodels: https://www.statsmodels.org/
- Kaggle Datasets: https://www.kaggle.com/datasets
- World Bank Data: https://data.worldbank.org/
- OECD Data: https://data.oecd.org/
- IMF Data: https://data.imf.org/

---

## 📝 完成後

```bash
git add Week11_Econometrics/
git commit -m "Week 11: AF5641 Econometrics + Python Regression Model (AI 對就業影響)"
git push
```
