# 📊 Quantitative Trading Strategies Portfolio

## 🧠 Overview

This report outlines a portfolio of **three quantitative trading strategies** developed for the Kailasa Capital Challenge under General Championship Tech. These strategies target **Nifty 50** and **Bank Nifty** instruments across 15-minute, hourly, and daily timeframes, optimizing for **profit consistency, drawdown control**, and **risk-adjusted returns** using an initial capital of ₹1 Crore.

---

## 📊 Strategy 1: MACD-Hull MA Crossover with Supertrend Exit

**Timeframe:** 15-minute  
**Instruments:** Nifty 50 & Bank Nifty  

### ✅ Logic

- **Entry Conditions:**
  - Long: MACD(25,50,15) histogram > 0 AND Close > 50-HMA
  - Short: MACD histogram < 0 AND Close < 50-HMA
- **Exit Conditions:**
  - Long Exit: Price < Supertrend(10,3)
  - Short Exit: Price > Supertrend(10,3)
- **Stop Loss:** 2 × ATR  
- **Capital Allocation:** ₹15 Lakhs

### ⚙️ Key Features

- Combines trend-following (HMA, MACD) with volatility-based exits (Supertrend)
- Short-term swing strategy for intraday moves

### 📈 Performance Metrics

| Metric              | Nifty 50    | Bank Nifty |
|---------------------|-------------|------------|
| Initial Capital     | ₹15,00,000  | ₹15,00,000 |
| Final Equity        | ₹27,88,350  | ₹29,83,073 |
| Total Return (%)    | 79.22%      | 98.87%     |
| CAGR (%)            | 0.46%       | 0.54%      |
| Sharpe Ratio        | 0.14        | 0.13       |
| Calmar Ratio        | 0.01        | 0.01       |
| Max Drawdown (%)    | 33.93%      | 32.49%     |
| Win Rate (%)        | 46.03%      | 43.72%     |
| Profit Factor       | 1.24        | 1.34       |

### ✅ Strengths

- High returns
- Good risk-reward ratio

### ⚠️ Weaknesses

- Low Sharpe & Calmar ratios due to high drawdowns
- Sub-50% win rate (common in trend-following)

---

## 📊 Strategy 2: Volatility-Bounded Trend-Following

**Timeframe:** Hourly  
**Instruments:** Nifty 50 & Bank Nifty  

### ✅ Core Logic

- Long: Price > 200-SMA AND EMA(9) > EMA(21) AND ADX > 25
- Short: Price < 200-SMA AND EMA(9) < EMA(21) AND ADX > 25

### 📐 Instrument-Specific ATR Ranges

| Component  | ATR(14) Range |
|------------|---------------|
| Nifty 50   | 50–200        |
| Bank Nifty | 150–400       |

### 📈 Performance Metrics

| Metric              | Nifty 50    | Bank Nifty |
|---------------------|-------------|------------|
| Initial Capital     | ₹15,00,000  | ₹15,00,000 |
| Final Equity        | ₹37,29,856  | ₹28,79,784 |
| Total Return (%)    | 148.65%     | 91.98%     |
| CAGR (%)            | 2.68%       | 1.91%      |
| Sharpe Ratio        | 0.39        | 0.29       |
| Calmar Ratio        | 0.09        | 0.06       |
| Max Drawdown (%)    | 29.26%      | 29.94%     |
| Win Rate (%)        | 41.81%      | 43.85%     |
| Profit Factor       | 1.84        | 2.16       |

### ✅ Strengths

- Filters false signals with ATR
- Strong trend identification

### ⚠️ Weaknesses

- May miss trades during high volatility
- Delay from ADX confirmation

---

## 📊 Strategy 3: MACD-Supertrend Long-Only

**Timeframe:** Daily  
**Instruments:** Nifty 50 & Bank Nifty  

### ✅ Rules

- **Entry:** MACD(12,26,9) > Signal Line AND Price > Supertrend(10,3)
- **Exit:** MACD < Signal OR Price < Supertrend
- **Stop-Loss:** 0.1 × ATR trailing stop
- **Max Holding:** 10 trading days  
- **Only Long Positions**

### 📈 Performance Metrics

| Metric              | Nifty 50    | Bank Nifty |
|---------------------|-------------|------------|
| Initial Capital     | ₹15,00,000  | ₹15,00,000 |
| Final Equity        | ₹72,47,929  | ₹78,11,485 |
| Total Return (%)    | 383.20%     | 420.77%    |
| CAGR (%)            | 36.93%      | 38.99%     |
| Sharpe Ratio        | 0.87        | 1.04       |
| Calmar Ratio        | 0.66        | 1.00       |
| Max Drawdown (%)    | 55.75%      | 38.90%     |
| Win Rate (%)        | 45.45%      | 48.89%     |
| Profit Factor       | 1.64        | 1.69       |

### ✅ Strengths

- High Sharpe & Calmar ratios
- Dual exit protection

### ⚠️ Concerns

- Tight stops may trigger early exits
- No short-side participation

---

## 💰 Position Sizing & ROI Strategy

- Deployed 3 strategies × 2 instruments = 6 strategies
- Capital per strategy: ₹15 Lakhs (₹90L total), ₹10L as buffer
- No compounding, constant 1-lot trades for risk control
- **Final Portfolio Value:** ₹2,84,78,679  
- **Total Return:** 184.78%

---

## 📌 Final Thoughts

This multi-strategy, multi-timeframe approach:

- Combines low-correlation systems for stability
- Works across market conditions
- Prioritizes risk-adjusted return
- Can serve as a strong base for future algo strategy development

---

> ⚙️ Built with statistical discipline, technical indicators, and capital efficiency in mind – ready for real-world deployment.
