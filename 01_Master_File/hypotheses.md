# Project Hypotheses
## Beyond Last-Click: Influencer Engagement Efficiency and Paid vs Organic Conversion in E-Commerce

**Author:** Soheila Zamani
**School:** SPICED Academy Berlin — Data Analytics Bootcamp 2026
**GitHub:** https://github.com/Soha-zamani/beyond-last-click

---

## Business Question

> Which marketing channel — influencer content or paid advertising — drives higher performance value in e-commerce?
> And does influencer size (tier) and content niche make a measurable difference in engagement efficiency?

---

## Datasets

| Dataset | Source | Rows | What it covers |
|---|---|---|---|
| YouTube Influencer Data | YouTube Data API v3 — collected by me | **4,527 active channels** | All 4 tiers · 9 niches · 82 countries · after quality filtering |
| Marketing A/B Testing | Kaggle (FavioVázquez) — real Facebook experiment | 588,101 real users | Paid vs Organic — conversion rates |

> Quality filters applied: ≥100 subscribers · ≥5 videos · last upload within 365 days.

---

## Hypotheses — All 6 Confirmed

---

### H1 — Influencer Tier vs Engagement Efficiency
**"Nano influencers generate higher views per subscriber than mega influencers."**

- **Metric:** `view_per_subscriber` = total views ÷ subscriber count
- **Dataset:** YouTube API (4,527 channels)
- **Groups:** nano (< 10K) · micro (10K–100K) · macro (100K–1M) · mega (1M+)
- **Test:** Kruskal-Wallis test across all four tiers
- **Result:** ✅ **Confirmed** — Nano median VPS: 1.62 vs Mega: 0.33 → **5.0× advantage**
- **Significance:** p = 9.21e-263 — statistically significant beyond any conventional threshold
- **Why it matters:** Brands using last-click attribution undervalue nano influencers because their subscriber count looks small. This confirms they deliver significantly more engagement per subscriber — meaning more value per euro spent.

---

### H2 — Content Niche vs Engagement Rate
**"Engagement rate varies significantly across content niches on YouTube."**

- **Metric:** `view_per_subscriber` by niche
- **Dataset:** YouTube API
- **Groups:** Fashion · Lifestyle · Beauty · Travel · Film & Streaming · Food · Gaming · Fitness · Shopping
- **Test:** Kruskal-Wallis test across niches
- **Result:** ✅ **Confirmed** — Top niches: Fashion (1.09) · Lifestyle (0.79) · Beauty (0.74) · Travel (0.73)
- **Why it matters:** E-commerce brands need to know which content niches deliver the highest engagement efficiency — not just which have the most channels. Fashion and Lifestyle consistently outperform.

---

### H3 — Channel Size vs Content Efficiency
**"Smaller influencers produce relatively more views per subscriber than larger influencers."**

- **Metric:** Log-log regression: log10(subscribers) → log10(view_per_subscriber)
- **Dataset:** YouTube API
- **Groups:** All 4 tiers / continuous subscriber count
- **Test:** Pearson correlation on log-transformed data + linear regression
- **Result:** ✅ **Confirmed** — r = −0.52 · R² = 0.27 · coefficient = −0.23 per log unit
- **Interpretation:** Every 10× increase in subscribers → ~41% drop in views per subscriber
- **Why it matters:** Audience loyalty and content efficiency decline as channels grow. A brand investing in 10 nano creators will likely outperform one mega creator on engagement metrics.

---

### H4 — Paid Advertising vs Organic Conversion
**"Users exposed to a paid advertisement convert at a statistically significantly higher rate than users who saw no paid ad."**

- **Metric:** Conversion rate (converted = True)
- **Dataset:** Marketing A/B Testing (588,101 users)
- **Groups:** "ad" group (paid) vs "psa" group (organic baseline)
- **Test:** Chi-square test for proportions
- **Result:** ✅ **Confirmed** — Paid: 2.55% · Organic: 1.79% → **+43% conversion lift**
- **Significance:** p < 0.001
- **Why it matters:** Directly quantifies the value of paid advertising vs organic reach. Confirms that paid ads are worth the investment at the moment of conversion — while influencer content does the earlier awareness work.

---

### H5 *(Bonus)* — Geographic Origin and Influencer Engagement
**"Geographic origin affects influencer engagement rates — some countries produce significantly higher VPS than others."**

- **Metric:** Median `view_per_subscriber` by country
- **Dataset:** YouTube API
- **Filter:** Minimum 10 channels per country (excludes 'Unknown' group)
- **Test:** Median comparison across countries with sufficient sample size
- **Result:** ✅ **Confirmed** — Top countries: **Brazil (1.52) · Nigeria (0.95) · Spain (0.95)**
- **Pattern:** All top countries are dominated by nano/micro creators in Fashion, Film & Streaming, and Lifestyle niches — directly reflecting H1 and H2 findings at a country level
- **Why it matters:** For brands targeting international markets, country of origin is a meaningful filter. Nano creators in these markets outperform global averages.

---

### H6 *(Bonus)* — Ad Timing and Conversion Rate
**"Conversion rate varies significantly by time of day and day of week — certain windows perform significantly better."**

- **Metric:** Conversion rate by day × hour grid
- **Dataset:** Marketing A/B Testing (paid group only)
- **Test:** Heatmap analysis of conversion rate across 7 × 24 grid
- **Result:** ✅ **Confirmed** — Peak windows identified:
  - Saturday 5:00 AM: **5.68%** (highest in the dataset)
  - Saturday 6:00 AM: **5.16%**
  - Tuesday 4:00 PM: **4.56%**
  - Monday 2:00–3:00 PM: **4.29–4.49%**
- **Why it matters:** The same ad budget produces significantly more purchases when scheduled in these windows. Saturday early morning and Monday–Tuesday afternoon are hidden high-conversion opportunities.

---

## How the Two Datasets Connect

| Channel | Dataset | Key Metric |
|---|---|---|
| Influencer (nano) | YouTube API | `view_per_subscriber` = 1.62 median |
| Influencer (mega) | YouTube API | `view_per_subscriber` = 0.33 median |
| Paid advertising | A/B Testing — "ad" group | Conversion rate = 2.55% |
| Organic content | A/B Testing — "psa" group | Conversion rate = 1.79% |

**The bridge:** Paid ads convert 43% better than organic at the moment of decision. But nano influencers deliver 5.0× more engagement per subscriber in the awareness phase. Last-click attribution credits the ad and ignores the influencer — which is exactly the problem this project addresses.

---

## Methodology Note

Direct conversion comparison between YouTube API and A/B Testing data is not possible — the datasets come from different users, products, and environments. Instead, we compare **relative efficiency metrics** (engagement lift and conversion lift) across channels, consistent with industry practice when brand-level conversion data is not publicly available.

---

*Last updated: April 2026*
