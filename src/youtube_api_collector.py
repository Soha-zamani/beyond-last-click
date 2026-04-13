# ============================================================
# Beyond Last-Click — YouTube API Channel Collector (MAX MODE)
# Author: Soheila Zamani | SPICED Academy Berlin 2026
# ============================================================
# THREE COLLECTION PASSES — all runnable TODAY with 3 API keys
#
#   PASS 1 — Global search, 2 pages per query  → uses YOUTUBE_API_KEY
#     Quota cost:  ~9,800 / 10,000 units
#     Expected:    ~4,000–5,000 raw → ~2,500 new unique channels
#
#   PASS 2 — German/EU region search           → uses YOUTUBE_API_KEY_2
#     Quota cost:  ~9,300 / 10,000 units (auto-stops at limit)
#     Expected:    ~3,000 raw → ~1,500 new unique channels
#
#   PASS 3 — Video search (finds micro channels) → uses YOUTUBE_API_KEY_3
#     Quota cost:  ~4,900 / 10,000 units
#     Expected:    ~2,400 raw → ~1,000 new unique channels
#
# TOTAL TODAY: ~5,000–7,000+ unique channels (up from 1,738)
#
# HOW TO RUN ALL THREE TODAY:
#   1. Create 2 more free API keys at console.cloud.google.com
#   2. Paste them into your .env file as YOUTUBE_API_KEY_2 and _3
#   3. Run each pass in a separate terminal:
#        PASS=1 python src/youtube_api_collector.py
#        PASS=2 python src/youtube_api_collector.py
#        PASS=3 python src/youtube_api_collector.py
#   Or run them one after another in the same terminal — they merge automatically.
# ============================================================

from googleapiclient.discovery import build
from dotenv import load_dotenv
import pandas as pd
import os
import time

# ============================================================
# CONFIGURATION
# PASS is read from environment variable so you can run all 3
# in separate terminals at the same time:
#   PASS=1 python src/youtube_api_collector.py
#   PASS=2 python src/youtube_api_collector.py
#   PASS=3 python src/youtube_api_collector.py
# Or just set PASS manually below if running one at a time.
# ============================================================
PASS = int(os.environ.get("PASS", 1))   # default = 1 if not set
PAGES = 2         # Pages per query (each page = 50 results, costs 100 quota units)
MAX_RESULTS = 50  # Results per page (YouTube maximum is 50)

# Region codes for Pass 2 — adds geographic diversity
# WHY: same query in different regions returns completely different creators
REGION_CODES = ["DE", "AT", "CH", "GB", "NL", "FR"]  # German-speaking + Western EU

# ============================================================
# STEP 1 — Load the correct API key for this pass
# WHY: each pass uses a different key so all 3 can run today.
#   Pass 1 → YOUTUBE_API_KEY   (your original key)
#   Pass 2 → YOUTUBE_API_KEY_2 (second Google Cloud project)
#   Pass 3 → YOUTUBE_API_KEY_3 (third Google Cloud project)
# Each key has its own 10,000 unit daily quota — completely independent.
# ============================================================
load_dotenv()

KEY_MAP = {
    1: "YOUTUBE_API_KEY",
    2: "YOUTUBE_API_KEY_2",
    3: "YOUTUBE_API_KEY_3",
}
key_name = KEY_MAP[PASS]
API_KEY  = os.getenv(key_name)

if not API_KEY or API_KEY.startswith("PASTE_"):
    raise ValueError(
        f"❌ {key_name} not found or not filled in.\n"
        f"   Go to console.cloud.google.com → create a new project → "
        f"enable YouTube Data API v3 → create an API key → "
        f"paste it into your .env file as {key_name}=your_key_here"
    )

youtube = build('youtube', 'v3', developerKey=API_KEY)
print(f"✅ YouTube API client ready — PASS {PASS} using {key_name}")

# ── Live quota tracker ──────────────────────────────────────
# WHY: YouTube gives 10,000 free units/day.
# search.list  = 100 units per call
# channels.list = 1 unit per call
# We track this so you never accidentally go over the limit.
quota_used = 0
DAILY_LIMIT = 10_000

def use_quota(units, operation):
    global quota_used
    quota_used += units
    remaining = DAILY_LIMIT - quota_used
    print(f"   📊 Quota: {quota_used:,} used / {DAILY_LIMIT:,} limit  ({remaining:,} remaining) [{operation}]")
    if quota_used > DAILY_LIMIT * 0.95:
        print("   ⚠️  Approaching daily quota limit — stopping soon")
        return False  # signal to stop
    return True  # signal to continue


# ============================================================
# STEP 2 — Assign influencer tier by subscriber count
# ============================================================
def assign_tier(subscribers):
    if subscribers < 10_000:    return 'nano'    # 1 – 9,999
    elif subscribers < 100_000: return 'micro'   # 10,000 – 99,999
    elif subscribers < 1_000_000: return 'macro' # 100,000 – 999,999
    else:                       return 'mega'    # 1,000,000+


# ============================================================
# STEP 3 — Search for CHANNELS by keyword (Pass 1 & 2)
# WHY: returns up to 50 channel IDs per page.
#      With pagination we call this twice per query to get up to 100 IDs.
#      regionCode filters results to that country's YouTube — entirely
#      different channels than global results.
# ============================================================
def search_channels_paginated(query, niche, pages=2, region_code=None):
    """Search YouTube for channels, paginating through multiple result pages."""
    all_ids = []
    next_page_token = None

    for page_num in range(1, pages + 1):

        # Stop if quota almost full
        if not use_quota(100, f"search '{query}' page {page_num}"):
            break

        try:
            params = {
                "part":            "snippet",
                "q":               query,
                "type":            "channel",
                "maxResults":      MAX_RESULTS,
                "relevanceLanguage": "en"
            }
            # Add region code if doing a regional pass
            if region_code:
                params["regionCode"] = region_code

            # Add page token to get the next page of results
            if next_page_token:
                params["pageToken"] = next_page_token

            response = youtube.search().list(**params).execute()

            ids = [item['id']['channelId'] for item in response.get('items', [])]
            all_ids.extend(ids)

            # Get token for the next page — if None, no more pages exist
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break   # YouTube says there are no more pages

        except Exception as e:
            print(f"   ⚠️  Search error '{query}' page {page_num}: {e}")
            break

        time.sleep(0.5)  # small pause between pages

    return all_ids


# ============================================================
# STEP 4 — Search for VIDEOS and extract their channel IDs (Pass 3)
# WHY: YouTube's channel search surfaces popular/established channels.
#      Searching VIDEOS instead finds creators who make great content
#      but whose channels are too small to rank in channel search.
#      This is the best way to find micro and nano creators.
# ============================================================
def search_via_videos(query, niche):
    """Search for videos, extract unique channel IDs."""
    use_quota(100, f"video search '{query}'")
    try:
        response = youtube.search().list(
            part="snippet",
            q=query,
            type="video",          # searching VIDEOS not channels
            maxResults=MAX_RESULTS,
            relevanceLanguage="en",
            order="viewCount"      # sort by views to get a range of sizes
        ).execute()

        # Extract the channel ID from each video result
        # WHY: each video belongs to a channel — this is our indirect route
        channel_ids = list(set([
            item['snippet']['channelId']
            for item in response.get('items', [])
        ]))
        return channel_ids, niche

    except Exception as e:
        print(f"   ⚠️  Video search error '{query}': {e}")
        return [], niche


# ============================================================
# STEP 5 — Fetch real stats for a list of channel IDs
# WHY: search only gives us IDs. channels.list gives us the actual
#      data: subscribers, views, video count, country, name.
#      We batch up to 50 IDs per API call to save quota.
# ============================================================
def get_channel_stats(channel_ids, niche):
    """Fetch statistics for up to 50 channel IDs in one API call."""
    if not channel_ids:
        return []

    # Batch in groups of 50 (YouTube API maximum per call)
    all_data = []
    for i in range(0, len(channel_ids), 50):
        batch = channel_ids[i:i+50]
        use_quota(1, f"channels.list batch of {len(batch)}")  # 1 unit per call

        try:
            response = youtube.channels().list(
                part="statistics,snippet",
                id=",".join(batch)
            ).execute()

            for ch in response.get('items', []):
                stats   = ch.get('statistics', {})
                snippet = ch.get('snippet', {})

                subscribers = int(stats.get('subscriberCount', 0))
                views       = int(stats.get('viewCount', 0))
                videos      = int(stats.get('videoCount', 1))

                avg_views    = views / videos if videos > 0 else 0
                view_per_sub = avg_views / subscribers if subscribers > 0 else 0

                all_data.append({
                    'channel_name':        snippet.get('title', 'Unknown'),
                    'channel_id':          ch['id'],
                    'subscribers':         subscribers,
                    'total_views':         views,
                    'video_count':         videos,
                    'avg_views_per_video': round(avg_views),
                    'view_per_subscriber': round(view_per_sub, 4),
                    'country':             snippet.get('country', 'Unknown'),
                    'tier':                assign_tier(subscribers),
                    'niche':               niche
                })
        except Exception as e:
            print(f"   ⚠️  Stats error for batch: {e}")

        time.sleep(0.3)

    return all_data


# ============================================================
# STEP 6 — Search queries (49 queries across all niches)
# Long-tail queries → smaller, more niche creators (micro/nano)
# Broad queries    → larger, established creators (macro/mega)
# ============================================================
search_queries = {
    # ── BEAUTY ───────────────────────────────────────────────
    "beauty makeup tutorial":               "Beauty",
    "skincare routine channel":             "Beauty",
    "affordable skincare under 30":         "Beauty",
    "daily skincare minimalist routine":    "Beauty",
    "drugstore makeup beginner":            "Beauty",
    "natural beauty no filter":             "Beauty",
    "skincare over 40 youtube":             "Beauty",
    "german beauty influencer":             "Beauty",

    # ── FASHION ──────────────────────────────────────────────
    "fashion haul outfit":                  "Fashion",
    "style fashion blogger":                "Fashion",
    "minimalist capsule wardrobe":          "Fashion",
    "thrift store outfit ideas":            "Fashion",
    "slow fashion sustainable style":       "Fashion",
    "plus size fashion youtube":            "Fashion",
    "berlin street style":                  "Fashion",

    # ── FITNESS ──────────────────────────────────────────────
    "fitness workout channel":              "Fitness",
    "home workout no equipment":            "Fitness",
    "30 day fitness challenge beginner":    "Fitness",
    "yoga for beginners at home":           "Fitness",
    "running training plan youtube":        "Fitness",
    "strength training women beginners":    "Fitness",

    # ── LIFESTYLE ────────────────────────────────────────────
    "lifestyle vlog channel":               "Lifestyle",
    "slow living simple life vlog":         "Lifestyle",
    "morning routine productivity":         "Lifestyle",
    "minimalist living apartment":          "Lifestyle",
    "study with me vlog":                   "Lifestyle",
    "berlin life expat vlog":               "Lifestyle",

    # ── FILM & STREAMING ─────────────────────────────────────
    "film movie review channel":            "Film & Streaming",
    "netflix series review":                "Film & Streaming",
    "indie film analysis deep dive":        "Film & Streaming",
    "hidden gem movies youtube":            "Film & Streaming",
    "documentary review channel":           "Film & Streaming",

    # ── FOOD ─────────────────────────────────────────────────
    "food recipe cooking channel":          "Food",
    "easy meal prep weekly":                "Food",
    "budget cooking recipes student":       "Food",
    "vegan recipes beginners":              "Food",
    "german food recipes traditional":      "Food",

    # ── TRAVEL ───────────────────────────────────────────────
    "travel vlog channel":                  "Travel",
    "budget backpacking europe":            "Travel",
    "solo travel female europe":            "Travel",
    "weekend trips from berlin":            "Travel",

    # ── GAMING ───────────────────────────────────────────────
    "gaming youtube channel":               "Gaming",
    "indie game review small channel":      "Gaming",
    "retro games nostalgia channel":        "Gaming",
    "mobile gaming tips":                   "Gaming",

    # ── SHOPPING ─────────────────────────────────────────────
    "amazon finds haul":                    "Shopping",
    "best deals online shopping":           "Shopping",
    "sustainable shopping guide":           "Shopping",
    "budget shopping tips":                 "Shopping",
}


# ============================================================
# STEP 7 — Run the correct pass
# ============================================================
all_new_channels = []

print(f"\n{'='*60}")
print(f"PASS {PASS} — ", end="")

# ── PASS 1: Global channel search, 2 pages ─────────────────
if PASS == 1:
    print(f"Global search ({len(search_queries)} queries × {PAGES} pages)")
    print(f"Estimated quota cost: ~{len(search_queries) * PAGES * 100:,} units")
    print(f"{'='*60}\n")

    for i, (query, niche) in enumerate(search_queries.items(), 1):
        print(f"[{i:02d}/{len(search_queries)}] '{query}'")
        ids = search_channels_paginated(query, niche, pages=PAGES, region_code=None)
        if ids:
            stats = get_channel_stats(ids, niche)
            all_new_channels.extend(stats)
            print(f"         → {len(stats)} channels collected")
        time.sleep(1)

# ── PASS 2: Regional search across 6 EU countries ──────────
elif PASS == 2:
    print(f"EU/Germany region search ({len(search_queries)} queries × {len(REGION_CODES)} regions)")
    print(f"Estimated quota cost: ~{len(search_queries) * len(REGION_CODES) * 100:,} units")
    print(f"⚠️  This exceeds 1 day quota — script will auto-stop at 95% limit")
    print(f"{'='*60}\n")

    for region in REGION_CODES:
        print(f"\n🌍 Region: {region}")
        for i, (query, niche) in enumerate(search_queries.items(), 1):
            if quota_used > DAILY_LIMIT * 0.93:
                print(f"\n⛔ Quota limit reached at {quota_used:,} units. Stopping safely.")
                break
            print(f"  [{i:02d}] '{query}' [{region}]")
            ids = search_channels_paginated(query, niche, pages=1, region_code=region)
            if ids:
                stats = get_channel_stats(ids, niche)
                all_new_channels.extend(stats)
                print(f"         → {len(stats)} channels")
            time.sleep(0.8)

# ── PASS 3: Video search (finds micro channels) ─────────────
elif PASS == 3:
    print(f"Video search ({len(search_queries)} queries — extracts channel IDs from videos)")
    print(f"Estimated quota cost: ~{len(search_queries) * 100:,} units")
    print(f"WHY: video search surfaces creators too small to rank in channel search")
    print(f"{'='*60}\n")

    for i, (query, niche) in enumerate(search_queries.items(), 1):
        print(f"[{i:02d}/{len(search_queries)}] '{query}'")
        ids, niche = search_via_videos(query, niche)
        if ids:
            stats = get_channel_stats(ids, niche)
            all_new_channels.extend(stats)
            print(f"         → {len(stats)} channels collected via videos")
        time.sleep(1)

else:
    raise ValueError(f"❌ Invalid PASS value: {PASS}. Must be 1, 2, or 3.")

print(f"\n✅ Pass {PASS} collection complete")
print(f"   Raw results collected: {len(all_new_channels)}")
print(f"   Total quota used: {quota_used:,} / {DAILY_LIMIT:,} units")


# ============================================================
# STEP 8 — Clean new results
# ============================================================
df_new = pd.DataFrame(all_new_channels)
df_new = df_new[df_new['subscribers'] > 0]   # remove zero-subscriber channels
df_new = df_new.drop_duplicates(subset='channel_id', keep='first')
print(f"   After internal dedup + cleaning: {len(df_new)} unique channels")


# ============================================================
# STEP 9 — Merge with existing dataset
# WHY: we never overwrite existing data. We stack old + new,
#      deduplicate by channel_id (keeping the existing record),
#      and save the combined result. Every pass ADDS to the dataset.
# ============================================================
OUTPUT_PATH   = "02_Datasets/youtube_influencers_real.csv"
EXISTING_PATH = OUTPUT_PATH  # always read from same file we write to — so passes chain correctly

if os.path.exists(EXISTING_PATH):
    df_existing = pd.read_csv(EXISTING_PATH)
    print(f"\n📂 Existing dataset: {len(df_existing):,} channels")
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
else:
    print("\n📂 No existing dataset found — saving new results only")
    df_combined = df_new

before = len(df_combined)
df_combined = df_combined.drop_duplicates(subset='channel_id', keep='first')
after  = len(df_combined)
net_new = after - (len(df_existing) if os.path.exists(EXISTING_PATH) else 0)

df_combined.to_csv(OUTPUT_PATH, index=False)


# ============================================================
# STEP 10 — Final summary
# ============================================================
tier_order = ['nano', 'micro', 'macro', 'mega']
tier_counts = df_combined['tier'].value_counts().reindex(tier_order)

print(f"\n{'='*55}")
print(f"PASS {PASS} COMPLETE — FINAL SUMMARY")
print(f"{'='*55}")
print(f"\n  Channels before this pass:  {len(df_existing) if os.path.exists(EXISTING_PATH) else 0:,}")
print(f"  Net new channels added:     {net_new:,}")
print(f"  Total dataset size:         {after:,}")
print(f"  Quota used:                 {quota_used:,} / {DAILY_LIMIT:,}")

print(f"\n  Tier distribution:")
for tier, count in tier_counts.items():
    bar = "█" * (count // 30)
    pct = count / after * 100
    print(f"    {tier:6s}  {count:5,}  ({pct:.1f}%)  {bar}")

print(f"\n  Niche distribution:")
for niche, count in df_combined['niche'].value_counts().items():
    print(f"    {niche:22s}  {count:,}")

print(f"\n  Countries represented: {df_combined['country'].nunique()}")
print(f"\n  💾 Saved to: {OUTPUT_PATH}")
print(f"{'='*55}")
print(f"\nNEXT STEP: Run Pass {PASS + 1 if PASS < 3 else 1} tomorrow (or with a second API key)")
print(f"           Then copy output to 02_Datasets/processed/youtube_influencers_clean.csv")
