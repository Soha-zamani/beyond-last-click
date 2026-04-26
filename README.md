# Beyond Last-Click
## A Multi-Channel Performance Analysis in E-Commerce

**Author:** Soheila Zamani
**School:** SPICED Academy Berlin — Data Analytics Bootcamp 2026
**Graduation:** April 28, 2026
**GitHub:** https://github.com/Soha-zamani/beyond-last-click

---

## 🎯 Business Question

> Which marketing channel — influencer content or paid advertising — drives higher performance value in e-commerce? And does influencer size (tier) and content niche make a measurable difference in engagement efficiency?

---

## 💡 Why This Project?

Most e-commerce brands measure marketing success using **last-click attribution** — giving all the credit to the last channel a customer touched before buying. This systematically undervalues influencer content, which often starts the customer journey but rarely gets the final click.

This project analyses real data to build a more complete picture of channel performance — comparing influencer engagement efficiency across tiers and niches, and testing whether paid advertising converts significantly better than organic.

---

## 📁 Project Structure

```
beyond-last-click/
│
├── 01_Master_File/          ← Project planning documents, task tracker
│
├── 02_Datasets/             ← All data files (NOT uploaded to GitHub)
│   ├── youtube_influencers_real.csv        ← Raw YouTube API data (7,281 rows)
│   ├── 5- Marketing A:B Testing.csv        ← Raw Facebook A/B test data
│   └── processed/
│       ├── youtube_influencers_clean.csv   ← After cleaning (Notebook 02)
│       └── youtube_influencers_enriched.csv ← After API enrichment (Notebook 06)
│
├── 04_Analysis/             ← All charts and visualisations saved by notebooks
│
├── 05_Tableau/              ← Tableau workbook (.twb) — interactive dashboards
│
├── 06_Presentation/         ← Final presentation slides + script
│
├── notebooks/               ← All Jupyter notebooks — run in order
│   ├── 01_data_collection_eda.ipynb          ← Load, validate, first EDA
│   ├── 02_data_cleaning_sql.ipynb            ← Clean data + load into PostgreSQL
│   ├── 03_hypothesis_testing.ipynb           ← Statistical testing (H1–H4)
│   ├── Notebook_04_Regression_Analysis.ipynb ← Log-log regression for H3
│   ├── 04_visualisations.ipynb               ← Final charts for all hypotheses
│   ├── 05_Insights_Summary.ipynb             ← Conclusions and business insights
│   ├── 06_YouTube_Enrichment.ipynb           ← YouTube API enrichment (engagement rate)
│   └── 07_New_Findings.ipynb                 ← 4 Quadrants + Ideal Creator Profile
│
├── sql/
│   └── queries.sql                           ← Analysis queries (DBeaver / PostgreSQL)
│
├── src/
│   └── youtube_api_collector.py              ← Script to collect YouTube channel data
│
├── .gitignore                                ← Protects credentials + data files
├── hypotheses.md                             ← All 6 hypotheses documented
├── requirements.txt                          ← Python libraries needed
└── README.md                                 ← This file
```

---

## 📊 Datasets

| # | File | Source | Rows | What it covers |
|---|---|---|---|---|
| 1 | `youtube_influencers_enriched.csv` | YouTube Data API v3 — collected by me | **4,527** | Active creator channels — 4 tiers, 9 niches, 82 countries, after quality filtering |
| 2 | `5- Marketing A:B Testing.csv` | Kaggle (FavioVázquez) — real Facebook experiment | 588,101 | Paid ad vs organic — who converted |

> ⚠️ Data files are stored locally only and are NOT uploaded to GitHub (protected by .gitignore).
>
> Quality filters applied to YouTube data: ≥100 subscribers · ≥5 videos · last upload within 365 days.

---

## 🔬 Hypotheses — All 6 Confirmed

| # | Hypothesis | Dataset | Test | Result |
|---|---|---|---|---|
| H1 | Nano influencers have higher VPS than mega influencers | YouTube API | Kruskal-Wallis | ✅ 5.0× advantage (p = 9.21e-263) |
| H2 | Engagement varies significantly across content niches | YouTube API | Kruskal-Wallis | ✅ Fashion leads (VPS 1.09) |
| H3 | Smaller channels produce more views per subscriber | YouTube API | Pearson + Regression | ✅ r = −0.52, R² = 0.27 |
| H4 | Paid ads convert at a higher rate than organic | A/B Testing | Chi-square | ✅ +43% lift (2.55% vs 1.79%) |
| H5 *(bonus)* | Geographic origin affects influencer engagement | YouTube API | Median by Country | ✅ Brazil, Nigeria, Spain lead |
| H6 *(bonus)* | Conversion rate varies by time of day / day of week | A/B Testing | Conversion heatmap | ✅ Sat 5–7am · Mon–Tue 14–16:00 |

Full details in `hypotheses.md`

---

## 🆕 New Findings (Beyond the Hypotheses)

**4 Creator Quadrants** — All 4,527 channels mapped by VPS × recency (30-day threshold):

| Quadrant | Channels | Description |
|---|---|---|
| Q1 — Dream Creators | 1,515 | High VPS + recently active → best partnership candidates |
| Q2 — Evergreen Creators | 750 | High VPS + less active → worth monitoring |
| Q3 — Active but Struggling | 1,928 | Posting often, low reach → not recommended |
| Q4 — Fading Out | 334 | Low VPS + inactive → remove from shortlists |

**Ideal Creator Profile** — 668 channels (14.8%) meet the data-defined ideal: top 25% VPS (≥1.66) + uploaded within 30 days. Median VPS: 3.21 — 5.1× the dataset average of 0.63.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.9+ | Main analysis language |
| Pandas | Data manipulation and cleaning |
| Matplotlib + Seaborn | Data visualisation |
| SciPy | Statistical testing (Kruskal-Wallis, chi-square, Pearson) |
| SQLAlchemy + psycopg2 | Python-to-PostgreSQL connection |
| PostgreSQL (AWS RDS) | Data storage and querying |
| DBeaver | SQL client for writing and running queries |
| YouTube Data API v3 | Live data collection and enrichment |
| Tableau | Interactive dashboard (4 story points) |
| VSCode | Development environment |
| GitHub | Version control and portfolio |

---

## 🚀 How to Run This Project

### Step 1 — Clone the repository
```bash
git clone https://github.com/Soha-zamani/beyond-last-click.git
cd beyond-last-click
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Add credentials
Create a `.env` file in the root with your PostgreSQL and YouTube API credentials (see `.gitignore` — this file is never committed).

### Step 4 — Add your data files
Place these files in `02_Datasets/`:
- `youtube_influencers_real.csv`
- `5- Marketing A:B Testing.csv`

### Step 5 — Run notebooks in order
Open each notebook in `notebooks/` in VSCode and run from top to bottom:

1. `01_data_collection_eda.ipynb` — Load, validate, first EDA
2. `02_data_cleaning_sql.ipynb` — Clean + load into PostgreSQL
3. `03_hypothesis_testing.ipynb` — H1–H4 statistical tests
4. `Notebook_04_Regression_Analysis.ipynb` — Log-log regression for H3
5. `04_visualisations.ipynb` — Final charts
6. `05_Insights_Summary.ipynb` — Conclusions and recommendations
7. `06_YouTube_Enrichment.ipynb` — API enrichment (engagement rate)
8. `07_New_Findings.ipynb` — 4 Quadrants + Ideal Creator Profile

---

## 📅 Project Timeline

| Week | Dates | Focus |
|---|---|---|
| Week 9 | March 30 – April 5 | Planning, data collection, SH#1 |
| Week 10 | April 6 – 12 | EDA, cleaning, PostgreSQL, SH#2 |
| Week 11 | April 13 – 19 | Hypothesis testing, Tableau, SH#3 |
| Week 12 | April 20 – 27 | Polish, new findings, presentation, rehearsal |
| **April 28** | **Graduation** | **Capstone presentation to external guests** |

---

## 📬 Contact

**Soheila Zamani**
Data Analytics | SPICED Academy Berlin 2026
📍 Berlin, Germany
🔗 [GitHub](https://github.com/Soha-zamani) | [LinkedIn](https://www.linkedin.com/in/soheila-zamani)
