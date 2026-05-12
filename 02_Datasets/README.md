# Datasets

The data files are not included in this repository (excluded via `.gitignore`) because:
- The YouTube dataset is collected from the YouTube Data API v3 (terms of service prohibit redistribution).
- The Marketing A/B Test CSV is large (~21 MB) and is the original property of its Kaggle author.

Both datasets are reproducible — see the source links and instructions below.

## Datasets Used

### 1. YouTube Influencer Dataset (collected by me via API)
- **File:** `processed/youtube_influencers_clean.csv` and `processed/youtube_influencers_enriched.csv`
- **Source:** Collected directly from the **YouTube Data API v3** using the script in `src/youtube_api_collector.py`. Channels are discovered via niche-keyword search across 9 niches, then enriched with channel statistics (subscribers, total views, video count, country, upload recency).
- **Raw size:** 7,281 channels across 9 niches and 82 countries
- **Filter applied for analysis:** `subscribers >= 1,000` (industry-standard nano tier lower bound) → **3,848 channels** in the analysis dataset
- **Key columns:** `channel_name`, `subscribers`, `total_views`, `view_per_subscriber`, `tier`, `niche`, `country`, `days_since_last_upload`

### 2. Marketing A/B Test Dataset (public Kaggle dataset)
- **File:** `processed/ab_testing_clean.csv`
- **Source:** Kaggle — [Marketing A/B Testing by FavioVázquez](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing)
- **Size:** 588,101 users — randomly assigned to `ad` (paid) group or `psa` (organic baseline) group
- **Key columns:** `test_group`, `converted`, `total_ads`, `most_ads_day`, `most_ads_hour`

## How to Reproduce

1. **YouTube data:** Run `src/youtube_api_collector.py`. The script collects channel data via the YouTube Data API v3 — it handles pagination, batching, quota tracking, and deduplication. Setup instructions for the API key are in the script itself.
2. **A/B test data:** Download the CSV from the Kaggle link above and place it in `02_Datasets/processed/` as `ab_testing_clean.csv`.
3. Run `05_Notebooks/01_data_collection_eda.ipynb` for initial exploration.
4. Run `05_Notebooks/02_data_cleaning_sql.ipynb` to clean and load into PostgreSQL.
5. Run subsequent notebooks (`03` through `08`) for analysis and modeling.
