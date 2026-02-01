# WIDS Quant Agent: Minority Game Simulation

![Python](https://img.shields.io/badge/python-3.9+-blue)
![Status](https://img.shields.io/badge/status-stable-green)

## 📊 Project Abstract
This project implements an agent-based model (ABM) of the **Minority Game**, a classic Game Theory problem used in Econophysics to model financial markets. 

Unlike standard equilibrium models, this simulation features **heterogeneous, adaptive agents** who use inductive reasoning (Reinforcement Learning) to compete for scarce resources. The project demonstrates the **Phase Transition** between efficient coordination and herding-induced volatility.

## 🚀 Key Features
1.  **Adaptive Intelligence:** Agents possess a "Gene Pool" of strategies and dynamically switch based on historical performance (virtual scoring).
2.  **Market Alpha Metric:** Calculates $\alpha = \sigma^2 / N$ to quantitatively measure market efficiency against a random coin-toss baseline.
3.  **Regime Detection:** successfully models the "Efficient Phase" where $\sigma^2/N < 1$, proving agents can self-organize without central control.

## 📈 Simulation Results
**Configuration:** $N=101$, Memory $m=10$, Strategies $S=20$.

Our simulation demonstrates a **Sub-Critical Phase** (Efficient Market):
- **Volatility:** The market demand fluctuates narrowly around the equilibrium ($N/2$).
- **Efficiency:** The Alpha metric consistently stays below 1.0, indicating that the "Smart" Quant agents successfully arbitrage away predictable patterns, leaving only random noise.

![Simulation Result](data/final_report.png)

## 🛠 Tech Stack
- **Simulation Core:** `Mesa` (Agent-based modeling)
- **Data Analysis:** `Pandas`, `NumPy`
- **Visualization:** `Matplotlib`

## 📂 Repository Structure
- `src/`: Core logic modules (Agents, Strategies, Market Engine).
- `main.py`: CLI entry point for the simulation.
- `data/`: Output metrics and visualization.

---
*Built for the WIDS Quant Competition.*
