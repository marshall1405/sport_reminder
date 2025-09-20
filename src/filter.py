def filter_players(matches, players):
    output = []
    for m in matches:
        for p in players:
            if p.lower() in m.team1.lower() or p.lower() in m.team2.lower():
                output.append(m)
    return output


def filter_tournaments(matches, tournaments):
    output = []
    for m in matches:
        for t in tournaments:
            if t.lower() in m.league.name.lower():
                output.append(m)
    return output

def filter_all(matches, players, tournaments):
    output = []
    for m in matches:
        if any(p.lower() in m.team1.lower().split() or p.lower() in m.team2.lower() for p in players) or any(t.lower() in m.league.name.lower() for t in tournaments):
            output.append(m)
    return output

def create_player_array(players):
    return players.split(",")

def create_tournament_array(tournaments):
    return tournaments.split(",")