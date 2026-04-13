# Beyond Last-Click
## Beyond Last-Click: A Multi-Channel Performance Analysis in E-Commerce

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
├── 01_Master_File/          ← Project planning documents, meeting notes
│
├── 02_Datasets/             ← All data files (NOT uploaded to GitHub)
│   ├── raw/                 ← Original files — never edit these
│   │   ├── youtube_influencers_real.csv     ← Built via YouTube API
│   │   └── 5- Marketing A:B Testing.csv    ← Real Facebook experiment
│   └── processed/           ← Cleaned files produced by notebooks
│
├── 03_Papers/               ← Research papers and references
│
├── 04_Analysis/             ← Charts and visualisations saved by notebooks
│
├── 05_Tableau/              ← Tableau dashboard files
│
├── 06_Presentation/         ← Final presentation slides
│
├── notebooks/               ← All Jupyter notebooks — run in order
│   ├── 01_data_collection_eda.ipynb      ← Load, validate, first EDA
│   ├── 02_data_cleaning_sql.ipynb        ← Clean data + load into PostgreSQL
│   ├── 03_analysis_hypotheses.ipynb      ← Statistical hypothesis testing
│   └── 04_visualisations.ipynb           ← Final charts for presentation
│
├── sql/
│   └── queries.sql                       ← Analysis queries (DBeaver)
│
├── src/
│   └── youtube_api_collector.py          ← Script to collect YouTube data
│
├── .gitignore                            ← Protects credentials + data files
├── hypotheses.md                         ← All 4 hypotheses documented
├── requirements.txt                      ← Python libraries needed
└── README.md                             ← This file
```

---

## 📊 Datasets

| # | File | Source | Rows | What it covers |
|---|---|---|---|---|
| 1 | `youtube_influencers_real.csv` | YouTube Data API v3 — collected by me | 7,281 | Real YouTube channels — all influencer tiers and niches |
| 2 | `5- Marketing A:B Testing.csv` | Kaggle (FavioVázquez) — real Facebook experiment | 588,101 | Paid ad vs organic — who converted |

> ⚠️ Data files are stored locally only and are NOT uploaded to GitHub (protected by .gitignore).

---

## 🔬 Hypotheses

| # | Hypothesis | Dataset | Test |
|---|---|---|---|
| H1 | Nano/micro-influencers have higher engagement per subscriber than mega-influencers | YouTube API | Kruskal-Wallis |
| H2 | Fashion and beauty channels generate higher engagement than other niches | YouTube API | Kruskal-Wallis |
| H3 | Smaller channels produce more views per video relative to subscriber count | YouTube API | Pearson Correlation |
| H4 | Paid advertising converts significantly better than organic | A/B Testing | Chi-square test |

Full details in `hypotheses.md`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.13 | Main analysis language |
| Pandas | Data manipulation and cleaning |
| Matplotlib + Seaborn | Data visualisation |
| SciPy | Statistical testing (chi-square, Kruskal-Wallis, Pearson) |
| SQLAlchemy + psycopg2 | Python-to-PostgreSQL connection |
| PostgreSQL (AWS RDS) | Data storage and querying |
| DBeaver | SQL client for writing and running queries |
| Tableau | Interactive dashboard |
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
1. `01_data_collection_eda.ipynb` — Start here
2. `02_data_cleaning_sql.ipynb`
3. `03_analysis_hypotheses.ipynb`
4. `04_visualisations.ipynb`

---

## 📅 Project Timeline

| Week | Dates | What happens |
|---|---|---|
| Week 9 | March 30 – April 5 | Project planning, data collection, SH#1 with teacher |
| Week 10 | April 6 – 12 | EDA, data cleaning, load into PostgreSQL, SH#2 |
| Week 11 | April 13 – 19 | Hypothesis testing, Tableau dashboard, SH#3 |
| Week 12 | April 20 – 27 | Polish, rehearsal, final presentation prep |
| **April 28** | **Graduation** | **Capstone presentation to external guests** |

---

## 📬 Contact

**Soheila Zamani**  
Data Analytics | SPICED Academy Berlin 2026  
📍 Berlin, Germany  
🔗 [GitHub](https://github.com/Soha-zamani) | [LinkedIn](https://www.linkedin.com/in/soheila-zamani)
