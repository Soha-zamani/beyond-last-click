-- ============================================================
-- Beyond Last-Click — SQL Analysis Queries
-- Author: Soheila Zamani | SPICED Academy Berlin 2026
-- Schema: s_soheilazamani
-- ============================================================

--  setting my personal schema
SET search_path TO s_soheilazamani;

-- ============================================================
-- SECTION 1 — DATA PREVIEW
-- ============================================================

-- Preview: YouTube Channels (first 5 rows)
SELECT * FROM youtube_channels LIMIT 5;

-- Preview: A/B Testing (first 5 rows)
SELECT * FROM ab_testing LIMIT 5;

-- Row counts — verify data loaded correctly
SELECT
    'youtube_channels' AS table_name,
    COUNT(*) AS total_rows
FROM youtube_channels
UNION ALL
SELECT
    'ab_testing',
    COUNT(*)
FROM ab_testing;


-- ============================================================
-- SECTION 2 — H1: ENGAGEMENT BY INFLUENCER TIER
-- Hypothesis: Nano/micro have higher engagement than mega
-- ============================================================

-- H1: Engagement by tier — mean, median, and filtered comparison
SELECT
    tier,
    COUNT(*) AS channels,
    ROUND(AVG(view_per_subscriber)::numeric, 4) AS mean_engagement,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP 
          (ORDER BY view_per_subscriber)::numeric, 4) AS median_engagement
FROM youtube_channels
GROUP BY tier
ORDER BY median_engagement DESC;

-- H1 filtered: same query, channels with >= 100 subscribers only
SELECT
    tier,
    COUNT(*) AS channels,
    ROUND(AVG(view_per_subscriber)::numeric, 4) AS mean_engagement,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP 
          (ORDER BY view_per_subscriber)::numeric, 4) AS median_engagement
FROM youtube_channels
WHERE subscribers >= 100
GROUP BY tier
ORDER BY median_engagement DESC;


-- ============================================================
-- SECTION 3 — H2: ENGAGEMENT BY NICHE
-- Hypothesis: Fashion/beauty higher than fitness/lifestyle
-- ============================================================

-- All niches: mean + median side by side
SELECT
    niche,
    COUNT(*) AS channels,
    ROUND(AVG(view_per_subscriber)::numeric, 4) AS mean_engagement,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP
          (ORDER BY view_per_subscriber)::numeric, 4) AS median_engagement
FROM youtube_channels
GROUP BY niche
ORDER BY median_engagement DESC;

-- H2 filtered: channels >= 100 subscribers, median only
SELECT
    niche,
    COUNT(*) AS channels,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP
          (ORDER BY view_per_subscriber)::numeric, 4) AS median_engagement
FROM youtube_channels
WHERE subscribers >= 100
GROUP BY niche
ORDER BY median_engagement DESC;

-- H2 direct comparison: the 4 key niches (filtered + median)
-- FINDING: Fashion clearly #1. Beauty ≈ Lifestyle (0.0050 diff — confirmed by Kruskal-Wallis).
-- Fitness is clearly last.
SELECT
    niche,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP
          (ORDER BY view_per_subscriber)::numeric, 4) AS median_engagement
FROM youtube_channels
WHERE niche IN ('Fashion', 'Beauty', 'Fitness', 'Lifestyle')
  AND subscribers >= 100
GROUP BY niche
ORDER BY median_engagement DESC;


-- ============================================================
-- SECTION 4 — H3: SUBSCRIBER SIZE vs ENGAGEMENT
-- Does channel size negatively correlate with engagement?
-- ============================================================

-- Engagement summary by tier (mean + median, ordered by channel size)
SELECT
    tier,
    ROUND(AVG(subscribers)::numeric, 0)           AS avg_subscribers,
    ROUND(AVG(view_per_subscriber)::numeric, 4)   AS mean_engagement,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP
          (ORDER BY view_per_subscriber)::numeric, 4) AS median_engagement,
    COUNT(*) AS channels
FROM youtube_channels
GROUP BY tier
ORDER BY avg_subscribers ASC;

-- Top 10 most efficient nano channels (>= 1000 subscribers, reliable only)
SELECT
    channel_name,
    subscribers,
    ROUND(view_per_subscriber::numeric, 4) AS engagement,
    niche,
    country
FROM youtube_channels
WHERE tier = 'nano'
  AND subscribers >= 1000
ORDER BY view_per_subscriber DESC
LIMIT 10;

-- ============================================================
-- SECTION 5 — H4: PAID vs ORGANIC CONVERSION
-- Hypothesis: Paid advertising converts better than organic
-- ============================================================

SELECT
    test_group,
    COUNT(*) AS total_users,
    SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        AVG(CASE WHEN converted = TRUE THEN 1.0 ELSE 0.0 END) * 100,
        2
    ) AS conversion_rate_pct
FROM ab_testing
GROUP BY test_group
ORDER BY conversion_rate_pct DESC;


-- ============================================================
-- SECTION 6 — BONUS: BEST DAY & HOUR FOR PAID ADS
-- When do paid ads convert best?
-- ============================================================

-- Conversion rate by day of week (paid group only)
SELECT
    most_ads_day,
    COUNT(*) AS users,
    SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        AVG(CASE WHEN converted = TRUE THEN 1.0 ELSE 0.0 END) * 100,
        2
    ) AS conversion_rate_pct
FROM ab_testing
WHERE test_group = 'ad'
GROUP BY most_ads_day
ORDER BY conversion_rate_pct DESC;

-- Conversion rate by hour of day (paid group only)
SELECT
    most_ads_hour,
    COUNT(*) AS users,
    SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        AVG(CASE WHEN converted = TRUE THEN 1.0 ELSE 0.0 END) * 100,
        2
    ) AS conversion_rate_pct
FROM ab_testing
WHERE test_group = 'ad'
GROUP BY most_ads_hour
ORDER BY most_ads_hour ASC;

-- Best hour overall
SELECT
    most_ads_hour AS best_hour,
    ROUND(
        AVG(CASE WHEN converted = TRUE THEN 1.0 ELSE 0.0 END) * 100,
        2
    ) AS conversion_rate_pct
FROM ab_testing
WHERE test_group = 'ad'
GROUP BY most_ads_hour
ORDER BY conversion_rate_pct DESC
LIMIT 3;
