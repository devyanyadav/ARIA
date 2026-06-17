# ARIA — Adaptive Research & Intelligence Analyser

A rule-based AI system that analyses the World Happiness Report (2015–2019) to diagnose what makes a country happy. ARIA combines statistical analysis with a custom inference engine to evaluate the strengths and weaknesses of any country's happiness factors.

---

## What ARIA Does

- Analyses correlations between happiness and factors like GDP, health, freedom, and corruption
- Builds a scored profile (1–5) for any country across all happiness factors
- Runs a chain of reasoning to diagnose why a country is happy or unhappy
- Outputs a structured conclusion with strengths, weaknesses, and moderate factors

---

## Key Findings

- GDP per capita correlates most strongly with happiness (0.789)
- Health/life expectancy follows at 0.742, social support at 0.648
- No country below the 25th percentile of GDP has been found above the 75th percentile of happiness
- Global happiness remained flat from 2015 to 2019

---

## File Structure

aria/

├── data/

│   └── processed/

│       └── merged.csv          # Cleaned, merged dataset (2015–2019)

├── notebooks/

│   ├── pipeline.ipynb          # Layer 1 — data cleaning and merging

│   └── analysis.ipynb          # Layer 2 — statistical analysis

├── outputs/

│   └── graphs/                 # All matplotlib/seaborn visualisations

├── patterns.py                 # Layer 3 — pattern engine, country profiler

├── inference.py                # Layer 4 — inference engine, chain of reasoning

├── report.py                   # Layer 5 — report formatter

├── main.py                     # Entry point — argparse CLI

└── RESEARCH_REPORT.md          # Full research report

---

## How to Use

**Install dependencies**
pip install pandas numpy matplotlib seaborn

**Run ARIA on any country**
python main.py --country "South Korea"

**Example Output**
=======================================================

ARIA — Analysing: South Korea
[4/5] GDP per capita is high.

South Korea is wealthy and scores above average in happiness. Investigating why...

[4/5] Life expectancy is high — a core driver of happiness here.

[3/5] Social support is moderate — not a major driver but not a drag.

[2/5] Freedom is low in South Korea.

[2/5] Corruption perception is high in South Korea — governance is distrusted.
CONCLUSION — South Korea
Strengths:   gdp per capita (4/5), life expectancy (4/5)

Moderate:    social support (3/5)

Weaknesses:  freedom (2/5), corruption (2/5)

---

## Dataset

World Happiness Report (2015–2019) — [Kaggle](https://kaggle.com/datasets/unsdsn/world-happiness)  
Published by the Sustainable Development Solutions Network for the United Nations.

---

## Research Report

The full analysis, methodology, and findings are documented in [`RESEARCH_REPORT.md`](./RESEARCH_REPORT.md).

Published Report : https://www.kaggle.com/code/devyanyadav/aria-happiness-data-pipeline-analysis