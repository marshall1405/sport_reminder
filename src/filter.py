import json

def filter_players(matches, players):
    if not players:
        return matches

    filtered = []

    for m in matches:
        p1 = m.player1.lower()
        p2 = m.player2.lower()

        if any(player in p1 or player in p2 for player in players):
            filtered.append(m)

    return filtered

def filter_tournaments(matches, tournaments):
    if not tournaments:
        return matches

    filtered = []

    for m in matches:
        league_name = m.league.name.lower()

        if any(t in league_name for t in tournaments):
            filtered.append(m)

    return filtered


def filter_matches(matches, players=None, tournaments=None):
    result = matches

    if players:
        result = filter_players(result, players)

    if tournaments:
        result = filter_tournaments(result, tournaments)

    return result

def load_settings(path="settings.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def normalize_players(filter_string):
    if not filter_string:
        return None
    return [p.strip().lower() for p in filter_string.split(",") if p.strip()]    