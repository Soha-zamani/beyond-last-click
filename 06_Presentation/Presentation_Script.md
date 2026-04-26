# Beyond Last-Click — Presentation Script
**Soheila Zamani · SPICED Academy Berlin · April 2026**

*Estimated time: 12–15 minutes. Pause after each slide transition.*

---

## SLIDE 1 — Title

"Good morning / afternoon. My name is Soheila Zamani, and my project is called **Beyond Last-Click: A Multi-Channel Performance Analysis in E-Commerce**.

The title refers to a problem that every digital marketer knows — but most companies still haven't solved. I'll explain what that problem is in just a moment.

Before I start, a quick number from the results: nano influencers in this dataset deliver **5.0 times more views per subscriber** than mega influencers. That finding alone has real budget implications — and by the end of this presentation, you'll understand exactly why."

---

## SLIDE 2 — The Problem

"Let me start with the problem.

In digital marketing, most companies use what's called **last-click attribution**. This means: whoever gets the last click before a purchase, gets 100% of the credit.

The problem is that a customer rarely makes a purchase from a single touchpoint. They might first see a nano influencer's video about a product. Three days later, they see a paid ad. They click the ad and buy. Under last-click, the influencer gets zero credit — and the paid ad gets everything.

So brands keep increasing their paid ad budget, keep overlooking smaller influencers, and keep wondering why their marketing feels expensive and inefficient.

This project asks: what does the data actually show about which channels and which strategies perform?"

---

## SLIDE 3 — The Data

"To answer that question, I worked with two real datasets.

The first is a YouTube influencer dataset I built myself using the **YouTube Data API v3**. I searched by content niche, pulled channel data, and applied quality filters — minimum 100 subscribers, at least 5 videos, and a last upload within the past year. After cleaning, I had **4,527 active creator channels** across 9 content niches and 82 countries.

The second dataset is a real **Facebook A/B test** from Kaggle — 588,101 rows of user data comparing paid ads against organic content, tracking purchases, website clicks, and app downloads.

One important note: the YouTube data was collected via keyword search, which means it reflects searchable, public channels — not a random sample of all YouTube creators. I'll keep that in mind when drawing conclusions."

---

## SLIDE 4 — Research Design

"With those two datasets, I formulated **6 hypotheses** — and all 6 were confirmed.

I tested whether nano influencers outperform mega influencers. Whether content niche matters. Whether channel size correlates with performance. Whether paid ads actually convert better than organic. Whether geography affects engagement. And whether the time of day affects conversion rates.

Each hypothesis used a different statistical method — Kruskal-Wallis tests, Pearson correlation, regression, and A/B testing — depending on what the data required.

Let me walk through the key findings."

---

## SLIDE 5 — H1: Nano Advantage

"The first and strongest finding: **nano influencers deliver 5.0 times more views per subscriber** than mega influencers.

The median views per subscriber for nano channels is 1.62 — compared to just 0.33 for mega channels. This difference is not random. The Kruskal-Wallis test returns a p-value of 9.21 times 10 to the power of minus 263 — that is statistically significant beyond any reasonable threshold.

Why does this happen? Nano channels have smaller, more loyal audiences. Their subscribers actively watch their content, not just passively follow. For an e-commerce brand, that translates directly to higher content reach per euro spent on a partnership.

I also want to be precise here: this metric is views per subscriber — meaning how many views a channel generates relative to its audience size. It is a measure of content reach efficiency."

---

## SLIDE 6 — H2 + H3: Niche and Size

"Moving to hypotheses 2 and 3 — niche and channel size.

For niche: **Fashion leads** with a median views per subscriber of 1.09, followed by Lifestyle at 0.79, Beauty at 0.74, and Travel at 0.73. These top niches consistently outperform across tiers and geographies — which becomes important later in my recommendations.

For channel size and engagement: I ran a **Pearson correlation** between subscriber count and views per subscriber. The result is r = minus 0.52 — a moderate to strong negative correlation. The regression shows an R² of 0.27, meaning subscriber count explains 27% of the variation in engagement.

In plain terms: every time subscriber count increases by a factor of 10, views per subscriber drops by about 41%. Bigger channel, less efficient reach. This confirms the nano advantage we just saw."

---

## SLIDE 7 — H4: Conversion Lift

"Hypothesis 4 comes from the A/B test data.

The question was simple: do paid Facebook ads convert better than organic content?

Yes — by **43%**. The paid group had a conversion rate of 2.55%, compared to 1.79% for the organic group. That's a statistically significant lift across 588,101 users.

This confirms that paid ads are worth the investment — but notice what this finding does NOT say. It doesn't say paid ads should replace influencer content. It says they convert better at the moment of decision. The influencer may have already done the awareness work. This is exactly why last-click attribution is misleading."

---

## SLIDE 8 — H5: Geography

"Hypothesis 5 looks at geography.

When I filtered for countries with at least 10 channels in the dataset, three countries stood out: **Brazil** with a median VPS of 1.52, **Nigeria** at 0.95, and **Spain** at 0.95.

All three share a pattern: they are dominated by nano and micro tier channels in Fashion, Film, and Lifestyle niches. This is not a coincidence — it reinforces the same story. Small, niche-focused creators in the right content categories consistently outperform regardless of where they are based.

For a brand targeting international markets, this is actionable: don't just look for influencers by follower count — look for nano creators in these niches, in these markets."

---

## SLIDE 9 — H6: Best Time for Ads

"The final hypothesis looked at timing.

When is the best time to run a paid ad for maximum conversion?

The answer is surprisingly specific: **Saturday at 5am** has the highest conversion rate in the entire dataset at 5.68%. Saturday 6am follows at 5.16%. For weekdays, **Monday and Tuesday between 2pm and 4pm** are the top windows.

Saturday early morning is a hidden opportunity — low competition, high intent users. Monday and Tuesday afternoons capture people at the start of the week when purchasing decisions are fresh.

These are the windows where the same ad budget produces the most purchases."

---

## SLIDE 10 — Recommendations

"Based on all six findings, I have three concrete recommendations for e-commerce brands.

**First:** Match your influencer tier to your campaign goal. Use nano creators for reach and awareness — they have the highest views per subscriber. Use macro creators for engagement-driven campaigns — they have the highest engagement rate. These are two different tools for two different jobs.

**Second:** Schedule paid ads on Saturday between 5 and 7 in the morning, and on Monday and Tuesday between 2 and 4 in the afternoon. Those are your highest-converting windows.

**Third:** Prioritise Fashion, Lifestyle, and Beauty niches in your influencer selection. These consistently outperform across all tiers and geographies — they should be the first filter before you look at anything else."

---

## SLIDE 11 — New Finding: 4 Creator Types

"Now I want to show you something I built beyond the original hypotheses — a framework for segmenting creators.

Using two metrics that I had full data for — **views per subscriber** and **days since last upload** — I mapped all 4,527 channels into four quadrants, split at the median value for each axis.

**Q1 — High Views Per Subscriber, Recently Active:** 1,515 channels. These are your best candidates for influencer partnerships right now. Nano-dominated, Beauty niche, median VPS of 1.45.

**Q2 — High Views Per Subscriber, Less Active:** 750 channels. Their content still performs well — but they haven't uploaded recently. Worth monitoring but not activating immediately.

**Q3 — Low VPS, Recently Active:** 1,928 channels. Posting consistently but not getting the views. High effort, low return.

**Q4 — Low VPS, Less Active:** 334 channels. Neither performing nor posting. These should be removed from any influencer shortlist.

This framework makes influencer screening practical and scalable."

---

## SLIDE 12 — New Finding: Ideal Creator Profile

"Using the same logic, I defined what an **ideal e-commerce influencer** looks like — based purely on the data.

The definition: top 25% for views per subscriber — meaning at least 1.655 — AND uploaded within the last 30 days. No guessing, no gut feeling.

Out of 4,527 channels, **668 meet this profile — that is 14.8% of the dataset.**

What do they look like? 50% are nano creators. The top niches are Beauty and Fashion. Their median views per subscriber is 3.21 — that is 5.1 times the dataset average of 0.63. And they post, on average, every 2 days.

This is not a persona built from intuition. It is built from 4,527 real channels."

---

## SLIDE 13 — Closing

"I want to end on something personal.

Before this bootcamp, I spent 4 years at Healy World running A/B tests, managing campaigns, and building performance reports. Throughout those four years, I kept asking the same question: *why does this actually work?*

I had the instincts — but not the tools to prove it. This project is my answer.

The analysis confirms what experienced marketers often sense: that nano creators are undervalued, that timing matters, that not all niches are equal. But now I can say that with a p-value, a correlation coefficient, and a dataset of 588,000 users behind it.

Data analytics and marketing strategy are not two separate things. They are the same conversation — spoken in different languages. I now speak both.

Thank you."

---

## Timing Guide

| Slide | Target Time |
|-------|------------|
| 1 — Title | 45 sec |
| 2 — Problem | 1 min |
| 3 — Data | 1 min |
| 4 — Hypotheses | 45 sec |
| 5 — H1 Nano | 1.5 min |
| 6 — H2+H3 | 1.5 min |
| 7 — H4 A/B | 1 min |
| 8 — H5 Geography | 1 min |
| 9 — H6 Timing | 1 min |
| 10 — Recommendations | 1.5 min |
| 11 — 4 Quadrants | 1.5 min |
| 12 — Ideal Creator | 1 min |
| 13 — Closing | 1 min |
| **Total** | **~14 min** |

---

## Tips for Delivery

- **Slide 5 (Nano):** Say the p-value out loud — "nine point two one times ten to the power of minus two hundred and sixty-three." It sounds impressive because it is. The ratio is 5.0× (nano VPS 1.62 vs mega VPS 0.33).
- **Slide 7 (A/B Test):** Pause after "+43%" — let the number land before you explain it.
- **Slide 11 (Quadrants):** Point to each quadrant as you name it. Don't just read.
- **Slide 13 (Closing):** Slow down. This is the personal part — don't rush it.
- **If asked about limitations:** Say the YouTube data is keyword-based, not a random sample. Engagement rate data was missing for 93% of channels due to YouTube API privacy settings — which is why you used views per subscriber as the primary metric.
