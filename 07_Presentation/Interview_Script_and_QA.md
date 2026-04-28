# Interview Script & Q&A Simulation
## Beyond Last-Click — Soheila Zamani · April 2026

---

## PART 1 — HOW TO TALK ABOUT THIS PROJECT

### The 30-Second Version (elevator pitch / "tell me about yourself")

> "My capstone project is called Beyond Last-Click. I analysed two real datasets — 4,527 YouTube influencer channels I collected via the YouTube API, and 588,000 users from a real Facebook A/B test — to answer the question: which marketing channel actually performs better in e-commerce? I confirmed 6 hypotheses using statistical tests including Kruskal-Wallis, chi-square, and regression analysis. The strongest finding: nano influencers deliver 5 times more views per subscriber than mega influencers. And paid ads convert 43% better than organic at the moment of purchase. The insight is that these two findings work together — influencers do the awareness work, paid ads close the sale. Last-click attribution misses that completely."

---

### The 2-Minute Version (job interview / "walk me through your project")

> "The project started from a real problem I saw in my 4 years at Healy World — most companies use last-click attribution, which means the last ad gets 100% of the credit for a sale, even if an influencer's video started the customer journey days earlier. That leads brands to overspend on paid ads and undervalue smaller creators.
>
> I built two datasets. The first I collected myself using the YouTube Data API — I searched by niche keywords, applied quality filters, and ended up with 4,527 active creator channels across 9 niches and 82 countries. The second is a real Facebook A/B test from Kaggle — 588,000 users split between paid ads and organic content.
>
> I tested 6 hypotheses. The key findings: nano influencers deliver 5× more views per subscriber than mega influencers, with a p-value of 9.21 times 10 to the power of minus 263 — essentially impossible to be random. Paid ads convert 43% better than organic. Fashion and Lifestyle are the highest-performing niches. And Saturday 5am and Monday–Tuesday afternoons are the best times to run ads.
>
> Beyond the hypotheses, I built a creator segmentation framework — 4 quadrants mapping all 4,527 channels by performance and recency. And I identified 668 channels that meet a data-defined ideal creator profile: top 25% VPS, active in the last 30 days, median VPS 3.21 — 5 times the dataset average.
>
> The tools I used were Python, Pandas, SciPy, PostgreSQL, Tableau, and the YouTube Data API. Everything is documented on GitHub."

---

## PART 2 — Q&A SIMULATION

*These are real questions you should expect — from graduation jury members, job interviewers, and recruiters. Read the question, cover the answer, and try to answer from memory first.*

---

### SECTION A — About the Data

**Q1: Why did you use YouTube specifically? Did you consider Instagram or TikTok?**

> YouTube was the right choice for two reasons. First, the YouTube Data API is free, well-documented, and returns structured data including subscriber count, total views, and video count — exactly what I needed to calculate VPS. Instagram's API is heavily restricted since 2018 and doesn't return this level of channel-level data. TikTok's API is also limited for research use. Second, YouTube is the dominant platform for long-form influencer content in e-commerce niches like Fashion, Beauty, and Fitness — which are my target categories.

---

**Q2: How did you collect your YouTube data? Walk me through the process.**

> I used the YouTube Data API v3. I searched by content niche keywords — for example "fashion YouTube", "beauty channel" — and retrieved channel IDs from the search results. Then for each channel ID I called the Channels endpoint to get subscriber count, total views, video count, and country. I also stored the uploads playlist ID so I could later retrieve the 5 most recent videos per channel for enrichment. After collection I applied quality filters: minimum 100 subscribers, at least 5 videos, and last upload within 365 days. That left me with 4,527 active channels from 7,281 raw records.

---

**Q3: You have 4,527 channels but 20% have unknown country. Doesn't that affect your geographic analysis?**

> Yes, and I addressed this explicitly. The 925 "Unknown" channels are excluded from the geographic hypothesis — I only compare countries with at least 10 identified channels. Interestingly, the Unknown group has a median VPS of 1.59, which is actually higher than most identified countries. Based on channel names and content patterns, most appear to be South Asian creators, likely India-based, who didn't set a country in their YouTube profile. Their high engagement is consistent with H1 — they're 44% nano creators in Beauty and Fashion. I note this as a limitation but it doesn't change the top-3 country finding.

---

**Q4: Your dataset has a sampling bias — you collected by keyword search. How does that affect your conclusions?**

> It's a real limitation and I state it clearly in the project. Keyword search tends to surface channels that rank well for those terms, which means established and well-optimised channels are overrepresented. It also means nano creators in my dataset may be more discoverable and therefore higher-performing than the average nano creator on YouTube. So my engagement numbers for nano might be slightly optimistic. However, the directional finding — that nano outperforms mega — is robust enough that even with this bias, the pattern holds. I would validate it with a random sample or platform-level data if I had access.

---

### SECTION B — About Methodology

**Q5: Why Kruskal-Wallis instead of ANOVA for H1 and H2?**

> ANOVA assumes that the data is normally distributed within each group. I tested for normality using the Shapiro-Wilk test and the data was clearly non-normal — the VPS distribution is heavily right-skewed with long tails. Kruskal-Wallis is the non-parametric equivalent of ANOVA — it tests whether groups come from the same distribution without assuming normality. It's the correct choice when the normality assumption is violated, which it was here.

---

**Q6: What exactly is "views per subscriber" and why did you use it instead of engagement rate?**

> Views per subscriber is total views divided by subscriber count. It measures how many views a channel generates relative to the size of its audience — essentially, how efficiently a channel turns followers into actual viewers. I call it content reach efficiency.
>
> I used it instead of engagement rate because YouTube's API privacy settings hide likes and comments for the vast majority of channels — 93% of channels in my dataset had no engagement rate data available. VPS was the only engagement proxy I could compute reliably for the full 4,527 channels. I do have engagement rate for a sample of ~1,000 channels from the enrichment notebook, and I found that VPS and engagement rate measure different things — nano leads on VPS, macro leads on engagement rate. Two metrics, two strategies.

---

**Q7: What does a p-value of 9.21e-263 actually mean?**

> It means the probability of seeing this result — or a more extreme one — if there were actually no difference between tiers, is 9.21 times 10 to the power of minus 263. That number is so close to zero it is effectively impossible for the result to be random. Any threshold you use in statistics — 0.05, 0.01, 0.001 — this result passes by an enormous margin. The difference between nano and mega engagement is not a sampling fluke. It is real.

---

**Q8: Your H3 shows R² = 0.27. Is that a strong result?**

> R² of 0.27 means subscriber count explains 27% of the variation in views per subscriber. In isolation that sounds modest. But in the context of human behaviour and social media, explaining 27% of variance with a single variable — channel size — is actually meaningful. Engagement on YouTube is affected by many factors: content quality, upload frequency, niche seasonality, algorithm changes. The fact that one structural variable explains more than a quarter of the performance difference is a strong finding. And the direction is clear: the relationship is negative, significant, and consistent.

---

**Q9: You used a log transformation for H3. Why?**

> Subscriber count spans several orders of magnitude — from under 1,000 for nano channels to over 10 million for mega. Plotting raw subscriber count against VPS produces a chart where all the nano and micro channels are crushed against the left axis. Log transformation compresses that scale so that the distance between 1K and 10K subscribers is visually equal to the distance between 100K and 1M. This makes the relationship visible and the regression meaningful. The coefficient of −0.23 on the log scale means every 10× increase in subscribers corresponds to about a 41% drop in VPS — which is a clean, interpretable result.

---

**Q10: Is the A/B test result causal? Can you say paid ads cause more conversions?**

> The Facebook A/B test was a controlled experiment — users were randomly assigned to the ad group or the organic group. Random assignment is the key condition for causal inference. So yes, within the scope of this experiment, we can say that seeing the paid ad caused the higher conversion rate, not just that it was correlated with it. That said, I'm careful about one thing: I don't know the product, the ad creative, or the target audience. The 43% lift is real for this experiment — whether it generalises to a different product or brand requires validation.

---

**Q11: Why chi-square for H4?**

> H4 compares two proportions — the conversion rate of the ad group versus the PSA group. Both groups have binary outcomes: converted or not converted. Chi-square test for independence is exactly the right tool for this — it tests whether the proportion of conversions is the same across the two groups. With 588,000 observations, statistical power is very high and the result is significant at p < 0.001.

---

### SECTION C — About the Findings

**Q12: What was your most surprising finding?**

> Two things genuinely surprised me. First, the timing result: Saturday at 5am has the highest conversion rate in the entire dataset at 5.68%. Intuitively you'd avoid advertising at 5am on a weekend. But the data shows that whoever is online at that hour has very high purchase intent and low competition for their attention. Second — the micro tier has fewer channels in my dataset (832) than the macro tier (1,261). You'd expect the opposite in a natural distribution. The reason is the API collection method: keyword search surfaces either very small channels (nano) or well-established ones (macro/mega). The growing mid-tier micro is underrepresented. That explains the anomaly in the network chart.

---

**Q13: Can you actually compare YouTube engagement with Facebook conversion rates? They're different platforms and different metrics.**

> You're right that a direct comparison is not possible — and I say that explicitly in my methodology section. They come from different users, different products, and different contexts. What I compare instead is relative efficiency. Within the influencer channel, nano delivers 5× more engagement per subscriber than mega. Within the paid channel, paid ads deliver 43% more conversions than organic. These are two separate, independently validated findings. The narrative connection — that influencers do awareness and paid ads close the sale — is a framework supported by both findings, not a single combined calculation.

---

**Q14: What would you do differently with more time or a bigger budget?**

> Four things. First, I'd collect conversion data at the brand level — matching influencer posts to downstream purchases with UTM tracking. That would allow a true multi-touch attribution model, which is the real answer to the last-click problem. Second, I'd expand the YouTube data using a random sample rather than keyword search, to remove the sampling bias. Third, I'd build a predictive model — using the features I have (tier, niche, country, posting frequency) to predict which creator is most likely to land in Q1. That turns the quadrant framework into a scoring tool. Fourth, I'd track channel performance over time — right now the data is a snapshot.

---

**Q15: How did you define the quadrants? Why 30 days as the recency threshold?**

> The X axis is days since last upload and the Y axis is views per subscriber. Both axes are split at meaningful thresholds. For VPS I used the dataset median — 0.63 — so "high" means above average for this dataset. For recency I used 30 days as a fixed threshold, which represents "active within the last month." I chose 30 over the statistical median (which was 3 days) because 3 days would classify any channel that hadn't uploaded in the last 3 days as "less active" — too strict and not meaningful for monthly content creators. 30 days is a standard content marketing benchmark for active creators. The Tableau dashboard uses the same threshold for consistency.

---

**Q16: What is the ideal creator profile based on? Why those specific thresholds?**

> The ideal creator profile uses two filters. First, top 25% VPS — meaning a VPS of at least 1.66 — which I define as "high performance" relative to the dataset. The 75th percentile is a standard way to define "top performers" without being arbitrary. Second, uploaded within the last 30 days, which ensures the creator is currently active. Together these filters identify 668 channels — 14.8% of the dataset — whose median VPS is 3.21, which is 5.1× the dataset average of 0.63. The fact that 50% of them are nano creators and the top niches are Beauty and Fashion directly validates H1 and H2 at the individual channel level.

---

### SECTION D — Technical Questions

**Q17: How did you connect Python to PostgreSQL?**

> I used SQLAlchemy as the ORM layer and psycopg2 as the database driver. The connection string includes the host, port, database name, username and password — stored in a .env file that is blocked by .gitignore and never committed to GitHub. From the notebook I use `pd.read_sql()` to query and `df.to_sql()` to write. The PostgreSQL instance is hosted on AWS RDS.

---

**Q18: Why Tableau instead of Power BI or just Matplotlib?**

> Tableau was the right tool for this project for two reasons. First, the project requires interactive exploration — filtering by tier, niche, country — which Tableau handles natively without writing code. Second, the audience for the graduation presentation includes non-technical stakeholders who need to interact with the data themselves. Tableau's story points allow me to guide them through a narrative. For the static charts in the presentation I used Matplotlib and Seaborn because I needed pixel-level control over the output for the PDF export.

---

**Q19: Walk me through your SQL work. What queries did you write?**

> I used SQL for three things. First, data validation after loading — checking for nulls, duplicate channel IDs, and out-of-range values. Second, aggregation queries — median VPS by tier, by niche, by country — to cross-validate the Python Pandas results. Third, filtering queries — for example, pulling only channels with at least 5 videos and a last upload within 365 days to apply the quality filters before analysis. I used DBeaver as the SQL client connected to PostgreSQL on AWS RDS.

---

**Q20: Someone looks at your GitHub. What will they find?**

> They'll find a clean, well-documented repository. A README that explains the business question, all 6 confirmed hypotheses with results, the tech stack, and how to run the project in 5 steps. A hypotheses.md file with full methodology detail for each hypothesis. Eight Jupyter notebooks covering data collection, cleaning, SQL loading, hypothesis testing, regression analysis, visualisation, API enrichment, and new findings. A Tableau workbook. The final presentation. And a queries.sql file. The data files themselves are excluded via .gitignore because they contain real API data and the CSV is too large for GitHub. Everything else is there.

---

### SECTION E — Mindset & Growth Questions

**Q21: You come from a marketing background. How does that help you as a data analyst?**

> It means I already understand what the questions behind the data are. When I see a conversion rate drop, I don't just flag it — I think about whether it's a creative issue, a targeting issue, a timing issue, or a funnel issue. I know what A/B tests look like from the campaign side, so when I see this Facebook dataset I understand exactly what the experiment was trying to measure. Most analysts get the "how" — I already have the "why." That's what this project shows: the findings are technically rigorous but they're also directly actionable. I didn't just confirm hypotheses — I gave brands three specific things to do differently starting tomorrow.

---

**Q22: What was the hardest part of this project?**

> The hardest part was the data version problem. I collected the YouTube data at one point in time, ran my analysis, and embedded the numbers in the presentation. Then I had to regenerate the enriched dataset — which changed the relative `days_since_last_upload` values because "today" was a different date. The result: numbers in my notebooks no longer matched numbers in my Tableau dashboard. I had to do a full cross-check of every single number across all 7 notebooks, the PPT, the Tableau dashboards, and the script. The lesson: always save the exact data snapshot you used for analysis, and document which version of the data each result came from. I now understand why data lineage and versioning matter in production analytics.

---

**Q23: If a company gave you €10,000 for influencer marketing today, what would you recommend based on your findings?**

> Based on this data, I'd split it roughly 70/30. Seventy percent — €7,000 — goes to 10 to 15 nano creators in Fashion or Lifestyle with a VPS above 1.66 and an upload in the last 30 days. That's the ideal creator profile — 668 channels meet it. At nano rates, €7,000 gets you meaningful reach across multiple creators. Thirty percent — €3,000 — goes to paid ads, scheduled on Saturday between 5 and 7am and on Monday and Tuesday between 2 and 4pm. Those are the highest-converting windows in the dataset. The logic is: nano creators build awareness and trust, paid ads close the sale at the right moment. That's exactly what last-click attribution fails to see.

---

## PART 3 — QUICK ANSWERS FOR RAPID-FIRE QUESTIONS

*These are one-sentence answers for when the interviewer wants speed, not depth.*

| Question | Answer |
|---|---|
| How many channels in your dataset? | 4,527 active creator channels after quality filtering |
| What is VPS? | Total views divided by subscriber count — content reach efficiency |
| What's a nano influencer? | A channel with fewer than 10,000 subscribers |
| What's the nano advantage? | 5.0× more views per subscriber than mega influencers |
| What statistical test for H1? | Kruskal-Wallis — non-parametric, because the data is not normally distributed |
| What's the paid ads lift? | +43% conversion rate vs organic (2.55% vs 1.79%) |
| Best time to run a paid ad? | Saturday 5am (5.68% conversion) and Monday–Tuesday 2–4pm |
| Top performing niche? | Fashion — median VPS 1.09 |
| What are the 4 quadrants? | Dream Creators, Evergreen Creators, Active but Struggling, Fading Out |
| How many ideal creators? | 668 channels — 14.8% of the dataset |
| What's the ideal creator's median VPS? | 3.21 — 5.1× the dataset average |
| Why not ANOVA? | Data is not normally distributed — Shapiro-Wilk confirmed this |
| What's R² = 0.27 mean? | Subscriber count explains 27% of the variation in engagement |
| Can you compare YouTube and Facebook data? | Not directly — I compare relative efficiency metrics, not absolute values |
| What would you do differently? | Add actual conversion tracking at brand level to enable real attribution modelling |

---

*Last updated: April 2026 · SPICED Academy Berlin*
