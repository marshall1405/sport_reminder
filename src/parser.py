from datetime import datetime
from match import Match
from league import League

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
            match = Match(
                match_id=data.get("AA"),
                player1=data.get("CX"),
                player2=data.get("AF"),
                time=convert_time(data.get("AD")),
                league=current_league
            )
            current_league.add_match(match)

    return list(leagues.values())


def extract_all_matches(leagues):
    return [match for league in leagues for match in league.matches]