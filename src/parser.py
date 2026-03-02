from datetime import datetime
from match import Match
from league import League
import json

def convert_time(ts):
    return datetime.fromtimestamp(int(ts)).strftime("%H:%M")

def parse_feed(raw_text):
    objects = raw_text.split("~")
    leagues = []
    matches = []
    current_league = None

    for obj in objects:
        if not obj.strip():
            continue

        fields = obj.split("¬")
        data = {}

        for field in fields:
            if "÷" in field:
                key, value = field.split("÷", 1)
                data[key] = value

        # League block
        if "ZA" in data:
            current_league = data["ZA"]
            continue

        # Match block
        if "AE" in data and "FH" in data:
            match = {
                "league": current_league,
                "player1": data.get("AE"),
                "player2": data.get("FH"),
                "time": convert_time(data.get("AD"))
            }
            matches.append(match)

    return matches


import json

def map_feed_to_objects(raw_text):
    objects = raw_text.split("~")
    leagues = {}
    current_league = None
    for obj in objects:
        if not obj.strip():
            continue
        fields = obj.split("¬")
        data = {}
        for field in fields:
            if "÷" in field:
                key, value = field.split("÷", 1)
                data[key] = value

        # League
        if "ZA" in data:
            league_name = data["ZA"]
            current_league = League(league_name)
            leagues[league_name] = current_league
            continue

        # Match
        if "AE" in data and "FH" in data:
            # Extract channel from AL field
            get_channel = None
            al_raw = data.get("AL")
            if al_raw:
                try:
                    al_data = json.loads(al_raw)
                    # Grab first channel's name from any round key
                    for round_key, entries in al_data.items():
                        if entries:
                            get_channel = entries[0].get("BN")
                            break
                except (json.JSONDecodeError, AttributeError):
                    pass

            match = Match(
                player1=data.get("CX"),
                player2=data.get("AF"),
                time=convert_time(data.get("AD")),
                league=current_league,
                channel=get_channel
            )
            current_league.add_match(match)

    return list(leagues.values())

def extract_all_matches(leagues):
    return [match for league in leagues for match in league.matches]