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
├── 01_Master_File/          ← Project planning, task tracker, hypotheses
│
├── 02_Datasets/             ← Data files (NOT uploaded — see README inside)
│   └── processed/
│       ├── youtube_influencers_clean.csv      ← After cleaning (Notebook 02)
│       ├── youtube_influencers_enriched.csv   ← After API enrichment (Notebook 06)
│       └── ab_testing_clean.csv               ← Cleaned A/B test data
│
├── 03_SQL/
│   └── queries.sql                            ← All analysis queries (PostgreSQL)
│
├── 04_Analysis/             ← Charts and visualisations exported from notebooks
│
├── 05_Notebooks/            ← All Jupyter notebooks — run in order
│   ├── 01_data_collection_eda.ipynb
│   ├── 02_data_cleaning_sql.ipynb
│   ├── 03_hypothesis_testing.ipynb
│   ├── 04_visualisations.ipynb
│   ├── 05_Insights_Summary.ipynb
│   ├── 06_YouTube_Enrichment.ipynb
│   ├── 07_New_Findings.ipynb
│   └── 08_Regression_Analysis.ipynb
│
├── 06_Tableau/              ← Tableau workbook (.twb) + dashboard screenshots
│
├── 07_Presentation/         ← Final presentation slides + speaker scripts
│
├── src/
│   └── youtube_api_collector.py               ← YouTube API data collection script
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Datasets

| # | Dataset | Source | Rows | Scope |
|---|---|---|---|---|
| 1 | YouTube Influencer Dataset | YouTube Data API v3 | 7,281 raw → **3,848 filtered** | 4 tiers, 9 niches, 82 countries |
| 2 | Facebook A/B Test | Kaggle (FavioVázquez) | **588,101 users** | Paid ad vs organic conversion |

> ⚠️ Data files are not uploaded to GitHub. See `02_Datasets/README.md` for sources and reproduction steps.
>
> Filter applied to YouTube data: `subscribers ≥ 1,000` (industry-standard nano tier lower bound) — ensures all channels represent real, discoverable creators.

---

## 🔬 Hypotheses — All 6 Confirmed

| # | Hypothesis | Dataset | Test | Result |
|---|---|---|---|---|
| H1 | Nano influencers outperform mega on engagement efficiency | YouTube | Kruskal-Wallis | ✅ **2.7× advantage** — Nano VPS 0.884 vs Mega 0.326 (p = 9.21e-263) |
| H2 | Engagement varies significantly across content niches | YouTube | Kruskal-Wallis | ✅ Fashion leads (median VPS 0.71), Fitness lowest |
| H3 | Subscriber count negatively correlates with engagement | YouTube | Spearman + Regression | ✅ r = −0.51, every 10× size increase → −41% VPS |
| H4 | Paid ads convert at a higher rate than organic | A/B Test | Chi-square | ✅ **+43% lift** — 2.55% vs 1.79% (causal, randomised) |
| H5 *(bonus)* | Geographic origin affects influencer engagement | YouTube | Median by Country | ✅ Brazil (1.12), Turkey (0.79), South Africa (0.75) lead |
| H6 *(bonus)* | Conversion rate varies by time of day and day of week | A/B Test | Conversion heatmap | ✅ Saturday 5am (5.68%), Mon–Tue 14–16:00 consistently strong |

Full details in `01_Master_File/hypotheses.md`

---

## 🆕 New Findings (Beyond the Hypotheses)

### 4 Creator Quadrants
All 3,848 channels mapped by VPS × recency (30-day activity threshold):

| Quadrant | Description |
|---|---|
| Q1 — Dream Creators | High VPS + recently active → best partnership candidates |
| Q2 — Evergreen Creators | High VPS + less active → worth monitoring |
| Q3 — Active but Struggling | Posting often, low engagement → not recommended |
| Q4 — Fading Out | Low VPS + inactive → remove from shortlists |

### Ideal Creator Profile
**448 channels (11.6% of 3,848)** meet the data-defined ideal: top 25% VPS + uploaded within 30 days.
- Median VPS: **2.89** — 3.3× the nano average
- Top combinations: Nano × Fashion (1.777), Nano × Shopping (1.097), Nano × Travel (0.951)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.9+ | Main analysis language |
| Pandas | Data manipulation and cleaning |
| Matplotlib + Seaborn | Data visualisation |
| SciPy + scikit-posthocs | Statistical testing (Kruskal-Wallis, Dunn's, chi-square) |
| SQLAlchemy + psycopg2 | Python-to-PostgreSQL connection |
| PostgreSQL (AWS RDS) | Data storage and SQL analysis |
| DBeaver | SQL client |
| YouTube Data API v3 | Live channel data collection |
| Tableau Public | Interactive dashboards |
| VSCode | Development environment |
| GitHub | Version control and portfolio |

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Soha-zamani/beyond-last-click.git
cd beyond-last-click

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add credentials
# Create a .env file with your PostgreSQL and YouTube API credentials

# 4. Add data files to 02_Datasets/processed/ (see 02_Datasets/README.md)

# 5. Run notebooks in order (05_Notebooks/)
```

**Notebook order:**
1. `01_data_collection_eda.ipynb` — Load and validate raw data
2. `02_data_cleaning_sql.ipynb` — Clean and load into PostgreSQL
3. `03_hypothesis_testing.ipynb` — H1–H4 statistical tests
4. `04_visualisations.ipynb` — Final charts
5. `05_Insights_Summary.ipynb` — Conclusions and recommendations
6. `06_YouTube_Enrichment.ipynb` — YouTube API enrichment
7. `07_New_Findings.ipynb` — 4 Quadrants + Ideal Creator Profile
8. `08_Regression_Analysis.ipynb` — Log-log regression for H3

---

## 📬 Contact

**Soheila Zamani**
Data Analytics | Marketing Strategy | SPICED Academy Berlin 2026
📍 Berlin, Germany
🔗 [GitHub](https://github.com/Soha-zamani) | [LinkedIn](https://www.linkedin.com/in/soheila-zamani)
