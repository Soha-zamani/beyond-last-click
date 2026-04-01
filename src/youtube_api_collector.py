from googleapiclient.discovery import build
import pandas as pd
import time

# ============================================
# PASTE YOUR API KEY HERE — keep it private
# ============================================
API_KEY = "AIzaSyA8Ux9_TM8hDK6BNJC9EAvUBAzaPWS-JAY"

youtube = build('youtube', 'v3', developerKey=API_KEY)

# ============================================
# FUNCTIONS
# ============================================

def search_channels(query, max_results=50):
    """Search YouTube for channels by keyword"""
    try:
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="channel",
            maxResults=max_results,
            relevanceLanguage="en"
        )
        response = request.execute()
        return [item['id']['channelId'] for item in response['items']]
    except Exception as e:
        print(f"Search error for '{query}': {e}")
        return []


def get_channel_stats(channel_ids):
    """Get real stats for a list of channel IDs"""
    try:
        request = youtube.channels().list(
            part="statistics,snippet",
            id=",".join(channel_ids)
        )
        response = request.execute()

        data = []
        for ch in response['items']:
            stats = ch.get('statistics', {})
            snippet = ch.get('snippet', {})

            subscribers = int(stats.get('subscriberCount', 0))
            views = int(stats.get('viewCount', 0))
            videos = int(stats.get('videoCount', 1))

            # Engagement proxy: average views per video
            avg_views = views / videos if videos > 0 else 0

            # Attribution value: how much each subscriber engages
            view_per_sub = avg_views / subscribers if subscribers > 0 else 0

            # Assign influencer tier based on subscribers
            if subscribers < 10_000:
                tier = 'nano'
            elif subscribers < 100_000:
                tier = 'micro'
            elif subscribers < 1_000_000:
                tier = 'macro'
            else:
                tier = 'mega'

            data.append({
                'channel_name': snippet.get('title', 'Unknown'),
                'channel_id': ch['id'],
                'subscribers': subscribers,
                'total_views': views,
                'video_count': videos,
                'avg_views_per_video': round(avg_views),
                'view_per_subscriber': round(view_per_sub, 4),
                'country': snippet.get('country', 'Unknown'),
                'tier': tier,
                'niche': query_niche  # added below
            })
        return data

    except Exception as e:
        print(f"Stats error: {e}")
        return []


# ============================================
# SEARCH QUERIES — covers all your target industries
# ============================================
search_queries = {
    # Beauty & Fashion
    "beauty makeup tutorial": "Beauty",
    "skincare routine channel": "Beauty",
    "fashion haul outfit": "Fashion",
    "style fashion blogger": "Fashion",

    # Fitness & Lifestyle
    "fitness workout channel": "Fitness",
    "lifestyle vlog channel": "Lifestyle",
    "health wellness youtube": "Fitness",

    # Film & Streaming (your target industry)
    "film movie review channel": "Film & Streaming",
    "netflix series review": "Film & Streaming",
    "cinema critic youtube": "Film & Streaming",

    # Food & Travel
    "food recipe cooking": "Food",
    "travel vlog channel": "Travel",

    # Micro/Nano specific searches — gets smaller channels
    "small beauty creator": "Beauty",
    "micro fashion influencer": "Fashion",
    "indie film review channel": "Film & Streaming",
    "nano lifestyle creator": "Lifestyle",
}


# ============================================
# RUN THE COLLECTION
# ============================================
all_channels = []

for query, niche in search_queries.items():
    print(f"Collecting: {query}...")
    query_niche = niche  # used inside get_channel_stats
    channel_ids = search_channels(query, max_results=50)

    if channel_ids:
        stats = get_channel_stats(channel_ids)
        all_channels.extend(stats)
        print(f"  → {len(stats)} channels added")

    time.sleep(1)  # polite pause between requests

# ============================================
# CLEAN AND SAVE
# ============================================
df = pd.DataFrame(all_channels)
df = df.drop_duplicates(subset='channel_id')  # remove duplicates
df = df[df['subscribers'] > 0]               # remove empty channels

# Save to CSV
df.to_csv('youtube_influencers_real.csv', index=False)

# ============================================
# SUMMARY
# ============================================
print(f"\n✅ DONE!")
print(f"Total unique channels: {len(df)}")
print(f"\nTier distribution:")
print(df['tier'].value_counts())
print(f"\nNiche distribution:")
print(df['niche'].value_counts())
print(f"\nCountry distribution (top 10):")
print(df['country'].value_counts().head(10))
print(f"\nSubscriber range:")
print(f"  Min: {df['subscribers'].min():,}")
print(f"  Max: {df['subscribers'].max():,}")
print(f"\nFile saved: youtube_influencers_real.csv")
