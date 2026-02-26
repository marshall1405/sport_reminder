from fetcher import fetch_match_detail

TELLY_CHANNELS = {
    "Premier Sport 1",
    "Premier Sport 2",
    "Premier Sport 3",
    "Sport 1",
    "Sport 2",
    "Nova Sport 1",
    "Nova Sport 2",
    "Nova Sport 3",
    "Nova Sport 4",
    "Nova Sport 5",
    "Nova Sport 6",
    "Eurosport 1",
    "Eurosport 2",
    "Strike TV",
    "Golf Channel",
    "Sporty TV",
    "Arena Sport 1",
    "Arena Sport 2",
    "Auto Motor Sport",
    "ČT sport",
}

def check_telly(match_id):
    detail_feed = fetch_match_detail(match_id)

    if not detail_feed:
        print('feed not found')
        return None

    detail_lower = detail_feed.lower()

    for channel in TELLY_CHANNELS:
        if channel.lower() in detail_lower:
            return channel

    return None