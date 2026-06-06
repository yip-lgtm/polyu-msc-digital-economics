"""
AI 對就業影響 — OLS Regression Model (Python)
PolyU AF5641 Econometrics | Week 11 | 2026年6月

對應 Notebook: AI_Employment_Regression_Model.ipynb
數據來源: Kaggle Global AI Adoption & Workforce Impact Dataset
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson

plt.rcParams['figure.figsize'] = (10, 6)
sns.set_style('whitegrid')

# ============================================================
# 1. 讀取數據
# ============================================================
# 請先從 Kaggle 下載: https://www.kaggle.com/datasets/mohankrishnathalla/global-ai-adoption-and-workforce-impact-dataset
# 將 CSV 檔案放入 Week11_Econometrics/ 資料夾

try:
    df = pd.read_csv("global_ai_adoption_workforce_impact.csv")
    print(f"✅ 成功讀取真實數據: {df.shape[0]} 筆, {df.shape[1]} 個變量")
except FileNotFoundError:
    print("⚠️ 找不到 CSV 檔案，使用模擬數據示範")
    # 模擬數據（基於 Brookings / OECD AI 對就業研究嘅典型值）
    np.random.seed(42)
    n = 50
    data = {
        'AI_Adoption_Level': np.random.choice(['Low', 'Medium', 'High'], n, p=[0.4, 0.4, 0.2]),
        'Automation_Rate': np.random.uniform(10, 80, n),
        'Company_Size': np.random.uniform(50, 50000, n),
    }
    df = pd.DataFrame(data)
    # 模擬 Workforce_Change
    # 將類別編碼
    df['AI_Adoption_Level_Code'] = df['AI_Adoption_Level'].map({'Low': 0, 'Medium': 1, 'High': 2})
    df['Workforce_Change'] = (
        0.8 * df['AI_Adoption_Level_Code']
        - 0.03 * df['Automation_Rate']
        + 0.00001 * df['Company_Size']
        + np.random.normal(0, 1, n)
    )

print("\n========== 數據預覽 ==========")
print(df.head(10))
print(f"\n數據形狀: {df.shape}")

# ============================================================
# 2. 資料清理
# ============================================================
print("\n========== 2. 資料清理 ==========")
print(f"原始數據: {df.shape[0]} 筆")
df = df.dropna(subset=['AI_Adoption_Level', 'Workforce_Change', 'Automation_Rate', 'Company_Size'])
print(f"清理後: {df.shape[0]} 筆")

# 將類別變數轉 dummy
df = pd.get_dummies(df, columns=['AI_Adoption_Level'], drop_first=True)
print(f"\nDummy 變量:")
print([c for c in df.columns if 'AI_Adoption_Level' in c])

# ============================================================
# 3. 定義變量
# ============================================================
print("\n========== 3. 變量定義 ==========")
y = df['Workforce_Change']

# 自動偵測 dummy 變量
dummy_cols = [c for c in df.columns if c.startswith('AI_Adoption_Level_')]
X_cols = ['Automation_Rate', 'Company_Size'] + dummy_cols
X = df[X_cols]
X = sm.add_constant(X)

print(f"應變量 Y: Workforce_Change")
print(f"自變量 X: {X_cols}")
print(f"樣本數: {len(y)}")

# ============================================================
# 4. 建立 OLS 模型（使用 HC3 robust standard errors）
# ============================================================
print("\n========== 4. OLS 估計 (HC3 Robust SE) ==========")
model = sm.OLS(y, X).fit(cov_type='HC3')
print(model.summary())

# ============================================================
# 5. 模型診斷
# ============================================================
print("\n========== 5. 模型診斷 ==========")

# 5.1 VIF (多重共線性)
print("\n--- 5.1 VIF (多重共線性) ---")
vif = pd.DataFrame()
vif['Variable'] = X.columns
vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif)
print("✅ VIF < 10 表示無嚴重多重共線性" if vif['VIF'].max() < 10 else "⚠️ VIF >= 10 表示有共線性問題")

# 5.2 Breusch-Pagan (同方差性)
print("\n--- 5.2 Breusch-Pagan (同方差性) ---")
residuals = model.resid
bp_test = het_breuschpagan(residuals, X)
print(f"LM Statistic: {bp_test[0]:.4f}")
print(f"p-value: {bp_test[1]:.4f}")
print("✅ p > 0.05: 同方差性假設成立" if bp_test[1] > 0.05 else "⚠️ p < 0.05: 存在異方差性（已用 HC3 修正）")

# 5.3 Durbin-Watson (自相關)
print("\n--- 5.3 Durbin-Watson (自相關) ---")
dw = durbin_watson(residuals)
print(f"DW = {dw:.4f}")
print("✅ DW ≈ 2: 無自相關" if abs(dw - 2) < 0.5 else "⚠️ DW 偏離 2: 存在自相關")

# 5.4 R-squared
print("\n--- 5.4 模型擬合 ---")
print(f"R² = {model.rsquared:.4f}")
print(f"Adjusted R² = {model.rsquared_adj:.4f}")
print(f"F-statistic = {model.fvalue:.4f}, p-value = {model.f_pvalue:.4f}")

# ============================================================
# 6. 視覺化
# ============================================================
print("\n========== 6. 視覺化 ==========")

# 6.1 自動化率 vs 就業變化
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.regplot(x='Automation_Rate', y='Workforce_Change', 
            data=df, scatter_kws={'alpha': 0.3}, ax=axes[0])
axes[0].set_title('Automation Rate vs Workforce Change')
axes[0].set_xlabel('Automation Rate (%)')
axes[0].set_ylabel('Workforce Change (%)')

# 6.2 AI 採用水平 vs 就業變化（boxplot）
# 重組 AI_Adoption_Level
if 'AI_Adoption_Level_Low' in df.columns:
    df['AI_Level'] = df.apply(lambda r: 'Low' if r['AI_Adoption_Level_Low'] == 1 
                              else ('Medium' if r.get('AI_Adoption_Level_Medium', 0) == 1 
                                    else 'High'), axis=1)
    sns.boxplot(x='AI_Level', y='Workforce_Change', data=df, ax=axes[1])
    axes[1].set_title('AI Adoption Level vs Workforce Change')
    axes[1].set_xlabel('AI Adoption Level')
    axes[1].set_ylabel('Workforce Change (%)')

plt.tight_layout()
plt.savefig('regression_visualization.png', dpi=150, bbox_inches='tight')
print("✅ 已儲存視覺化: regression_visualization.png")
plt.show()

# 6.3 殘差分析
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Q-Q Plot
sm.qqplot(residuals, line='45', ax=axes[0])
axes[0].set_title('Q-Q Plot of Residuals')

# Residuals vs Fitted
fitted = model.fittedvalues
axes[1].scatter(fitted, residuals, alpha=0.6)
axes[1].axhline(y=0, color='r', linestyle='--')
axes[1].set_xlabel('Fitted Values')
axes[1].set_ylabel('Residuals')
axes[1].set_title('Residuals vs Fitted')

# 殘差分佈
axes[2].hist(residuals, bins=15, edgecolor='black')
axes[2].set_xlabel('Residuals')
axes[2].set_ylabel('Frequency')
axes[2].set_title('Residuals Distribution')

plt.tight_layout()
plt.savefig('regression_diagnostics.png', dpi=150, bbox_inches='tight')
print("✅ 已儲存診斷圖: regression_diagnostics.png")
plt.show()

# ============================================================
# 7. 結果輸出
# ============================================================
print("\n========== 7. 結果總結 ==========")
print(f"模型解釋力 (R²): {model.rsquared:.4f} ({model.rsquared*100:.1f}%)")
print(f"顯著變量 (p < 0.05):")
for var, pval in model.pvalues.items():
    if pval < 0.05 and var != 'const':
        coef = model.params[var]
        print(f"  {var}: β = {coef:+.4f}, p = {pval:.4f}")

print("\n========== 8. 政策建議 ==========")
print("1. 鼓勵企業採用 AI 創造新職位")
print("2. 自動化高嘅行業配套再培訓")
print("3. AI 普及至中小企")
print("4. 監測就業市場動態")

print("\n✅ 完成！")
