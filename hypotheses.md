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
| YouTube Influencer Data | YouTube Data API v3 — collected by me | 1,805 real channels | Influencer channel — all tiers, 9 niches |
| Marketing A/B Testing | Kaggle (FavioVázquez) — real Facebook experiment | 588,101 real users | Paid vs Organic — conversion rates |

---

## Hypotheses

---

### H1 — Influencer Tier vs Engagement Efficiency
**"Micro-influencers (10k–100k subscribers) generate a higher engagement rate per subscriber than mega-influencers (1M+ subscribers)."**

- **Metric:** `view_per_subscriber` = avg views per video ÷ subscriber count
- **Dataset:** YouTube API
- **Groups:** nano / micro / macro / mega
- **Test:** One-way ANOVA or Kruskal-Wallis test across tiers
- **Why it matters:** Brands using last-click attribution undervalue micro-influencers because they look smaller. This hypothesis tests whether smaller channels actually deliver more engagement per subscriber — which means more value per euro spent.

---

### H2 — Content Niche vs Engagement Rate
**"Beauty and fashion channels generate higher engagement rates than fitness and lifestyle channels on YouTube."**

- **Metric:** `view_per_subscriber` by niche
- **Dataset:** YouTube API
- **Groups:** Beauty · Fashion · Fitness · Lifestyle · Film & Streaming · Food · Travel
- **Test:** Kruskal-Wallis test + post-hoc pairwise comparison
- **Why it matters:** E-commerce brands in beauty and fashion need to know if their niche naturally performs better — or if engagement differences are driven by influencer size rather than topic.

---

### H3 — Channel Size vs Content Efficiency
**"Smaller influencers (nano/micro) produce relatively more views per video compared to their subscriber count than larger influencers (macro/mega)."**

- **Metric:** `avg_views_per_video` ÷ `subscribers` ratio by tier
- **Dataset:** YouTube API
- **Groups:** All 4 tiers
- **Test:** Descriptive statistics + correlation analysis (subscribers vs view_per_subscriber)
- **Why it matters:** Shows whether audience loyalty and content quality decline as channels grow — a key insight for brands choosing between small and large creators.

---

### H4 — Paid Advertising vs Organic Conversion
**"Users exposed to a paid advertisement convert at a statistically significantly higher rate than users who saw no paid ad."**

- **Metric:** Conversion rate (converted = True)
- **Dataset:** Marketing A/B Testing
- **Groups:** "ad" group (paid) vs "psa" group (organic baseline)
- **Actual values:** Paid = 2.55% · Organic = 1.79%
- **Test:** Chi-square test for proportions
- **Why it matters:** Directly quantifies the value of paid advertising vs organic reach. Provides the paid channel benchmark to compare against influencer engagement proxy.

---

## How the Two Datasets Connect

| Channel | Dataset | Key Metric |
|---|---|---|
| Influencer | YouTube API | `view_per_subscriber` (engagement proxy) |
| Paid | A/B Testing — "ad" group | Conversion rate 2.55% |
| Organic | A/B Testing — "psa" group | Conversion rate 1.79% |

**The bridge:** Paid ads convert 43% better than organic. Within the influencer channel, we test whether micro-influencers generate disproportionately higher engagement — suggesting that last-click attribution systematically undervalues smaller creator partnerships.

---

## Methodology Note

Direct conversion comparison between YouTube API and A/B Testing data is not possible — the datasets come from different users, products, and environments. Instead, we compare **relative efficiency metrics** (engagement lift and conversion lift) across channels, consistent with industry practice when brand-level conversion data is not publicly available.

---

*Last updated: April 2026*
