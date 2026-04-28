# Beyond Last-Click — Natural Presentation Script
### with Complete Tableau Switching Guide
**Soheila "Soha" Zamani · SPICED Academy Berlin · April 28, 2026**

> **How to use this:** Read it out loud 3 times tonight — then put it away. Tomorrow, speak from memory. These are not words to read. They are ideas to express.
> Stage directions are in *[brackets]* — don't say them out loud.

---

## ⚙️ SETUP — Before anyone is in the room

- [ ] Keynote open on Slide 1, presentation mode ready but not started
- [ ] Browser Tab 1 open → **YouTube Influencer Analysis** dashboard (Tableau Public)
- [ ] Browser Tab 2 open → **New Findings** dashboard — Quadrant + Niche Strategy Map (Tableau Public)
- [ ] Both dashboards: click blank area to **clear all filters**
- [ ] Minimise browser — only Keynote visible on screen
- [ ] Water. Breathe. You know this better than anyone in the room.

---

## SLIDE 1 — TITLE
*[Stand. Smile. Wait one beat before you start talking.]*

"Hi everyone — my name is Soha.

Before coming to SPICED, I spent about 10 years in marketing and sales — running campaigns, managing budgets, and working with data every day.

And before every new product launch, we always had the same question: where should we invest our budget? What actually works?

We had opinions. We had reports. But we never had a clear answer.

This project is my attempt to finally find one."

*[Click → Slide 2]*

---

## SLIDE 2 — THE PROBLEM
"The method most e-commerce brands use is called last-click attribution.

It means 100% of the sale credit goes to the very last thing the customer clicked — usually a paid ad.

So imagine this: a nano influencer makes a video, someone watches it, gets interested, waits three days — and then clicks a retargeting ad and buys. The sale goes entirely to the ad. The influencer gets zero credit.

And brands are making real budget decisions based on this right now. They're cutting influencer budgets that are actually working. That's what I wanted to fix."

*[Click → Slide 3]*

---

## SLIDE 3 — THE DATA
"I worked with two datasets.

A YouTube influencer dataset — 4,527 channels, 9 niches, 82 countries.

And a Facebook A/B test — 588,000 users who were randomly assigned to either see a paid ad or not. Because it was a controlled experiment, I can actually say the ads *caused* more conversions — not just correlated with them. That's an important distinction.

Six hypotheses. All six confirmed."

*[Click → Slide 4]*

---

## SLIDE 4 — HYPOTHESES OVERVIEW
"Here's the roadmap — six hypotheses.

The first three are about influencer channels. The next two are about paid ads. One geographic bonus. And I found two extra insights the data led me to that I didn't originally plan for.

Let me walk you through each one —

*[Click — then immediately switch to Tableau]*

---

## 🔀 SWITCH TO TABLEAU — Tab 1
### YouTube Influencer Analysis Dashboard

*[Alt-Tab → browser → click Tab 1]*
*[The dashboard shows: H1 tier bar (top left) + H2 niche bar (top right) + Sankey (bottom)]*

---

## TABLEAU MOMENT 1 — H1 + H2 + Sankey
*[Point to the H1 tier bar chart — top left]*

"— starting with this.

This is my first hypothesis: do nano influencers outperform larger tiers on engagement?

Look at the numbers. Nano channels — under 10,000 subscribers — deliver a VPS of 0.884. VPS stands for Views Per Subscriber — it tells you how efficiently a channel turns its followers into actual viewers.

Mega channels — over one million subscribers — deliver 0.326.

That's roughly **2.7 times** the efficiency. And the p-value is 9.21e-263 — statistically certain, not random."

*[Click the orange **Nano < 1K** bar in the tier chart]*
*[The Sankey at the bottom will highlight Nano's flows]*

"And look at this Sankey down here — I click Nano, and you can see the flow goes almost entirely into 'High' engagement. Across every single niche. No exceptions."

*[Pause 2 seconds — let them look]*

*[Click a blank area to clear the highlight]*
*[Point to H2 niche bar chart — top right]*

"Now hypothesis two — does the content niche matter?

Fashion at 1.09, Lifestyle at 0.79, Beauty at 0.74, Travel at 0.73. They all cluster clearly above the rest.

These are visual, aspirational niches — exactly the categories where someone watches a video and thinks 'I want that.'

The takeaway is simple: if your brand is in Fashion, Lifestyle, Beauty, or Travel — YouTube influencers should already be in your strategy."

*[Alt-Tab → back to Keynote → Click → Slide 7 (H3)]*

---

## SLIDE 7 — H3: SIZE VS ENGAGEMENT
"Third hypothesis — as channels grow bigger, does their engagement drop?

Yes. For every 10× increase in subscriber count, VPS drops by 41%.

Why? Larger channels collect passive followers over time — people who subscribed years ago and don't really watch anymore. Smaller creators have tighter, more active communities. Their audience actually shows up.

This reinforces everything we just saw with nano creators."

*[Click → Slide 8]*

---

## SLIDE 8 — H4: PAID ADS
"Now the other side of the funnel — what happens at the moment of purchase?

In a controlled experiment with 588,000 real users, paid ads converted 43% better than organic. Organic group: 1.79%. Paid group: 2.55%.

This is a causal result — not a correlation. Paid ads don't just appear when sales happen. They cause them.

So the full picture is: influencers build awareness and trust. Paid ads close the sale. Both have a role. The mistake is measuring them the same way."

*[Click → Slide 9]*

---

## SLIDE 9 — H5: GEOGRAPHY
"Quick geographic finding — Brazil leads with a median VPS of 1.12, Turkey and South Africa follow at 0.79 and 0.75.

And when you look at why — these markets are dominated by nano and micro creators in Fashion, Lifestyle, and Beauty. Exactly the pattern we already found in H1 and H2 — just at a country level.

If you're running a global influencer campaign, these are the markets worth prioritising."

*[Click → Slide 10]*

---

## SLIDE 10 — H6: AD TIMING
"Last hypothesis — does the timing of a paid ad affect its conversion rate?

Yes — and this one genuinely surprised me.

Saturday at 5am converts at 5.68% — more than double the daily average. Monday and Tuesday afternoons, 2 to 4pm, are also consistently strong.

Saturday 5am sounds strange — but think about who is online at that hour. Someone already browsing with intent. Almost zero ad competition.

Same budget, same creative, just better timing — and you could more than double your conversion rate. That's essentially free improvement."

*[Click → Slide 11]*

---

## SLIDE 11 — RECOMMENDATIONS
"So based on everything — three concrete recommendations.

**One:** partner with nano creators in Fashion, Lifestyle, and Beauty. They deliver 2.7× the engagement efficiency. The data tells you exactly what the ideal profile looks like.

**Two:** schedule your paid ads for Saturday 5–7am and Monday–Tuesday 2–4pm. These are the highest-converting windows from 588,000 real users.

**Three:** stop using last-click attribution. Influencers open the door. Paid ads close it. If you only measure the last click, you'll systematically undervalue the influencer's role — and put your budget in the wrong place."

*[Click → Slide 12 — then immediately switch to Tableau]*

---

## 🔀 SWITCH TO TABLEAU — Tab 2
### New Findings Dashboard — Quadrant + Niche Strategy Map

*[Alt-Tab → browser → click Tab 2]*
*[The dashboard shows: Quadrant scatter on top, Niche Strategy Map on bottom]*

---

## TABLEAU MOMENT 2 — Quadrant + Niche Strategy Map
*[Point to the quadrant scatter — top half]*

"This maps all 4,527 channels.

X-axis is days since last upload — how recently they posted. Y-axis is VPS — engagement.

The green dots are what I call Dream Creators: top 25% VPS AND active in the last 30 days.

Four quadrants — Q1 top left, these are your best partnership candidates. Q3 bottom left — posting often but low engagement, not recommended. Q4 bottom right — inactive and low performing, remove from your lists."

*[Now point to the Niche Strategy Map — bottom half]*

"And this is the Niche Strategy Map. Each bubble is a niche — plotted by how many channels exist versus how much engagement they generate.

Fashion sits up here — high engagement, not yet saturated. That's the ideal position for a brand entering influencer marketing.

Now watch this —"

*[Click the **Fashion** bubble in the Niche Strategy Map]*
*[The quadrant scatter on top will filter to show only Fashion channels]*

"I click Fashion — and the scatter immediately filters to show only Fashion channels. You can see the green Q1 dots — those are your ideal Fashion creators. Active, high engagement, ready to partner with."

*[Click the **Beauty** bubble]*

"Same for Beauty — different cluster, same story."

*[Click the **Travel** bubble]*

"And Travel."

*[Click a blank area to clear all filters]*

"Across all niches combined — 448 channels meet the ideal criteria. That's your starting shortlist."

*[Alt-Tab → back to Keynote → Click → Slide 13]*

---

## SLIDE 13 — IDEAL CREATOR PROFILE
"And here's what the ideal creator actually looks like according to the data.

This heatmap shows median VPS by niche and tier. The pattern is completely consistent: nano tier dominates every single niche.

Top combinations — Nano × Fashion at 1.777, Nano × Travel at 0.951, Nano × Beauty at 0.816.

448 channels meet the full profile: nano creator, Beauty or Fashion, active in the last 30 days. Median VPS of 2.89 — that's 3.3× the nano average.

This is your shortlist. Built from data, not assumptions."

*[Click → Slide 14]*

---

## SLIDE 14 — CLOSING
*[Slow down here. This is the most important part. Look at the audience.]*

"I want to end with something personal.

Before this bootcamp, I spent four years at Healy World running A/B tests, managing YouTube campaigns, and building performance reports. I was working with data every day — but on top of it, not inside it.

This project changed that. For the first time, I can look at a 43% conversion lift and explain exactly where it comes from. I can build a hypothesis, test it properly, and defend the result.

Data analytics and marketing strategy are not two separate fields. They're the same conversation — just spoken in different languages.

I now speak both.

Thank you."

*[Pause. Smile. Wait. Don't fill the silence.]*

---

## ⏱️ TIMING
| Section | Time |
|---------|------|
| Slides 1–4 (Intro + Setup) | ~2 min |
| Tableau 1: H1 + H2 + Sankey | ~1 min 15 sec |
| Slides 7–10 (H3–H6) | ~2 min 30 sec |
| Slide 11 (Recommendations) | ~40 sec |
| Tableau 2: Quadrant + Niche Map | ~1 min 15 sec |
| Slides 13–14 (Ideal + Closing) | ~1 min 30 sec |
| **TOTAL** | **~9 min 10 sec** |

Comfortable within 10–12 minutes with natural pauses.

---

## 🖥️ SWITCHING CHEAT SHEET — memorise these 4 steps

| When | What to do |
|------|------------|
| After Slide 4 | **Alt-Tab → Tab 1** (YouTube Influencer Analysis) |
| After H1+H2 demo | Click blank area to clear → **Alt-Tab → Keynote → Slide 7** |
| After Slide 11 | **Alt-Tab → Tab 2** (New Findings: Quadrant + Map) |
| After Quadrant demo | Click blank area to clear → **Alt-Tab → Keynote → Slide 13** |

---

## 🖱️ WHAT TO CLICK IN EACH TABLEAU DASHBOARD

### Tab 1 — YouTube Influencer Analysis

| Step | What to click | What happens | What to say |
|------|--------------|-------------|-------------|
| 1 | Nothing — just show full view | All 4 tiers visible | Point to H1 bars, read out Nano=1.624, Macro=0.326 |
| 2 | Click orange **Nano < 1K** bar | Sankey highlights Nano flows | "Look — flows almost entirely to High engagement" |
| 3 | Click blank area | Sankey resets | "Let's look at niche now" |
| 4 | Point to H2 bars (right) | No click needed | Name top 4 niches |

### Tab 2 — New Findings (Quadrant + Niche Strategy Map)

| Step | What to click | What happens | What to say |
|------|--------------|-------------|-------------|
| 1 | Nothing — show full view | All dots visible, all bubbles | Explain Q1–Q4 quadrants |
| 2 | Click **Fashion** bubble (Niche Map) | Scatter filters to Fashion only | "Green dots = ideal Fashion creators" |
| 3 | Click **Beauty** bubble | Scatter filters to Beauty | Short pause, let them see it |
| 4 | Click **Travel** bubble | Scatter filters to Travel | Short pause |
| 5 | Click blank area | All channels return | "668 across all niches — your shortlist" |

---

## 💬 Q&A — READY ANSWERS

**"Can you show how tier and niche interact?"**
→ Stay in Tab 2 or switch to Tab 1 → point to Sankey → click Nano → flows to High → 20 sec

**"R² is 0.27 — isn't that weak?"**
→ "27% explained by a single variable in complex human behaviour is meaningful. The remaining 73% is content quality, community age, posting frequency — those don't invalidate the finding, they add nuance to it."

**"Nano creators are too small to scale — how do you deal with that?"**
→ "You don't replace one mega creator with one nano. You build a portfolio. Ten nano creators at 10K subscribers each equals 100K reach — with 2.7× better engagement per subscriber. Strategy shifts from reach-first to efficiency-first."

**"Your datasets are from different platforms — can you really compare them?"**
→ "I'm not comparing them directly. YouTube answers how influencers perform. Facebook answers how paid ads convert. Two separate questions, two separate datasets. Together they map the full funnel."

**"Why the 30-day threshold for 'active'?"**
→ "Standard content freshness window used by platform algorithms. The finding holds across 60 and 90 days too — 30 days is a defensible, conservative choice."

---

## 🔢 KEY NUMBERS — know without looking

| Number | What it means |
|--------|--------------|
| **2.7×** | Nano vs Mega efficiency |
| **0.884** | Nano median VPS |
| **0.326** | Mega median VPS |
| **+43%** | Paid ads conversion lift |
| **1.79% → 2.55%** | Organic to paid conversion |
| **5.68%** | Saturday 5am conversion rate |
| **588,000** | Facebook A/B test users |
| **448** | Ideal creator shortlist (11.6%) |
| **6/6** | All hypotheses confirmed |
