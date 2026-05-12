# Project Hypotheses
## Beyond Last-Click: A Multi-Channel Performance Analysis in E-Commerce

**Author:** Soheila Zamani
**School:** SPICED Academy Berlin — Data Analytics Bootcamp 2026
**GitHub:** https://github.com/soheila-zamani/beyond-last-click

---

## Business Question

> Which marketing channel — influencer content or paid advertising — drives higher performance value in e-commerce?
> And does influencer size (tier) and content niche make a measurable difference in engagement efficiency?

---

## Datasets

| Dataset | Source | Rows | What it covers |
|---|---|---|---|
| YouTube Influencer Data | YouTube Data API v3 — collected by me | **3,848 channels** (after filter) | All 4 tiers · 9 niches · 82 countries |
| Marketing A/B Testing | Kaggle (FavioVázquez) — real marketing campaign A/B test | 588,101 real users | Paid vs Organic conversion rates |

> Filter applied: `subscribers ≥ 1,000` (industry-standard nano tier lower bound). Ensures all channels represent real, discoverable creators.

---

## Hypotheses & Results

### H1 — Influencer Tier vs Engagement Efficiency
**"Nano influencers generate higher views per subscriber than mega influencers."**

- **Metric:** `view_per_subscriber` = total views ÷ subscriber count
- **Dataset:** YouTube API (3,848 channels)
- **Groups:** nano (< 10K) · micro (10K–100K) · macro (100K–1M) · mega (1M+)
- **Test:** Kruskal-Wallis test across all four tiers
- **Result:** Confirmed — Nano median VPS: 0.884 vs Mega: 0.326 → **2.7× advantage**
- **Significance:** p = 9.21e-263 — well past any conventional threshold
- **Why it matters:** Brands using last-click attribution undervalue nano influencers because their subscriber count looks small. The data shows they deliver more engagement per subscriber — meaning more value per euro spent.

---

### H2 — Content Niche vs Engagement Rate
**"Engagement rate varies significantly across content niches on YouTube."**

- **Metric:** `view_per_subscriber` by niche
- **Dataset:** YouTube API (3,848 channels)
- **Groups:** Fashion · Lifestyle · Beauty · Travel · Film & Streaming · Food · Gaming · Fitness · Shopping
- **Test:** Kruskal-Wallis test across niches
- **Result:** Confirmed — Fashion leads with median VPS 0.71. Fitness shows the lowest engagement.
- **Why it matters:** E-commerce brands need to know which content niches deliver the highest engagement efficiency. Fashion consistently outperforms.

---

### H3 — Channel Size vs Content Efficiency
**"Smaller influencers produce relatively more views per subscriber than larger influencers."**

- **Metric:** Log-log regression: log10(subscribers) → log10(view_per_subscriber)
- **Dataset:** YouTube API (3,848 channels)
- **Test:** Spearman correlation on log-transformed data + linear regression
- **Result:** Confirmed — Spearman r = −0.51, R² = 0.27
- **Interpretation:** Every 10× increase in subscribers → ~41% drop in views per subscriber
- **Why it matters:** Audience loyalty and content efficiency decline as channels grow. A brand investing in 10 nano creators will likely outperform one mega creator on engagement metrics.

---

### H4 — Paid Advertising vs Organic Conversion
**"Users exposed to a paid advertisement convert at a statistically significantly higher rate than users who saw no paid ad."**

- **Metric:** Conversion rate (converted = True)
- **Dataset:** Marketing A/B Testing (588,101 users)
- **Groups:** "ad" group (paid) vs "psa" group (organic baseline)
- **Test:** Chi-square test for proportions
- **Result:** Confirmed — Paid: 2.55% · Organic: 1.79% → **+43% conversion lift**
- **Significance:** p < 0.001
- **Why it matters:** Quantifies the value of paid advertising vs organic reach. Confirms that paid ads are worth the investment at the moment of conversion — while influencer content does the earlier awareness work.

---

### H5 (Bonus) — Geographic Origin and Influencer Engagement
**"Geographic origin affects influencer engagement rates — some countries produce significantly higher VPS than others."**

- **Metric:** Median `view_per_subscriber` by country
- **Dataset:** YouTube API (3,848 channels)
- **Filter:** Minimum 10 channels per country (excludes 'Unknown' group)
- **Test:** Median comparison across countries with sufficient sample size
- **Result:** Confirmed — Top countries: **Brazil (1.12), Turkey (0.79), South Africa (0.75)**
- **Pattern:** All top countries are dominated by nano/micro creators in Fashion, Lifestyle, and Beauty niches — the same pattern seen in H1 and H2 at a country level
- **Why it matters:** For brands targeting international markets, country of origin is a meaningful filter. Nano creators in these markets outperform global averages.

---

### H6 (Bonus) — Ad Timing and Conversion Rate
**"Conversion rate varies significantly by time of day and day of week — certain windows perform significantly better."**

- **Metric:** Conversion rate by day × hour grid
- **Dataset:** Marketing A/B Testing (paid group only)
- **Test:** Heatmap analysis of conversion rate across 7 × 24 grid
- **Result:** Confirmed — Peak windows identified:
  - Saturday 5:00 AM: **5.68%** (highest in the dataset)
  - Saturday 6:00 AM: **5.16%**
  - Tuesday 4:00 PM: **4.56%**
  - Monday 2:00–3:00 PM: **4.29–4.49%**
- **Why it matters:** The same ad budget produces measurably more purchases when scheduled in these windows. Saturday early morning and Monday–Tuesday afternoon are hidden high-conversion opportunities.

---

## How the Two Datasets Connect

| Channel | Dataset | Key Metric |
|---|---|---|
| Influencer (nano) | YouTube API | `view_per_subscriber` = 0.884 median |
| Influencer (mega) | YouTube API | `view_per_subscriber` = 0.326 median |
| Paid advertising | A/B Testing — "ad" group | Conversion rate = 2.55% |
| Organic content | A/B Testing — "psa" group | Conversion rate = 1.79% |

**The bridge:** Paid ads convert 43% better than organic at the moment of decision. Nano influencers deliver 2.7× more engagement per subscriber in the awareness phase. Last-click attribution credits the ad and ignores the influencer — which is exactly the problem this project addresses.

---

## Methodology Note

Direct conversion comparison between YouTube API and A/B Testing data is not possible — the datasets come from different users, products, and environments. Instead, we compare **relative efficiency metrics** (engagement lift and conversion lift) across channels, consistent with industry practice when brand-level conversion data is not publicly available.

---

*Last updated: April 2026*
