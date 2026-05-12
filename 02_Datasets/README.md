# Datasets

The data files are not included in this repository (excluded via `.gitignore`).

## Datasets Used

### 1. YouTube Influencer Dataset
- **File:** `processed/youtube_influencers_clean.csv` and `processed/youtube_influencers_enriched.csv`
- **Source:** Kaggle — [Social Blade YouTube dataset](https://www.kaggle.com/)
- **Size:** 7,281 channels across 9 niches and 82 countries
- **Filter applied for analysis:** `subscribers >= 1,000` (industry-standard nano tier lower bound) → 3,848 channels
- **Key columns:** `channel_name`, `subscribers`, `total_views`, `view_per_subscriber`, `tier`, `niche`, `country`, `days_since_last_upload`

### 2. Facebook A/B Test Dataset
- **File:** `processed/ab_testing_clean.csv`
- **Source:** Kaggle — [Facebook Ad Campaign A/B Testing dataset](https://www.kaggle.com/)
- **Size:** 588,101 users randomly assigned to `ad` or `psa` (organic) group
- **Key columns:** `test_group`, `converted`, `total_ads`, `most_ads_day`, `most_ads_hour`

## How to Reproduce

1. Download both datasets from Kaggle (links above)
2. Run `05_Notebooks/01_data_collection_eda.ipynb` for initial exploration
3. Run `05_Notebooks/02_data_cleaning_sql.ipynb` to clean and load into PostgreSQL
4. Run `05_Notebooks/06_YouTube_Enrichment.ipynb` to enrich with YouTube API data
5. All subsequent notebooks read from the processed CSVs or PostgreSQL directly
