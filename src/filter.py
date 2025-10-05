def filter_players(matches, players):
    output = []
    for m in matches:
        for p in players:
            if p.lower() in m.team1.lower() or p.lower() in m.team2.lower():
                output.append(m)
                break
    return output


def filter_tournaments(matches, tournaments):
    output = []
    for m in matches:
        for t in tournaments:
            if t.lower() in m.league.name.lower():
                output.append(m)
                break
    return output

def filter_all(matches, players, tournaments):
    play_matches = filter_players(matches, players)
    tour_matches = filter_tournaments(matches, tournaments)
    return list(set(play_matches) | set(tour_matches))

def create_player_array(players):
    if not players:
        return None
    return players.split(",")

def create_tournament_array(tournaments):
    if not tournaments:
        return None
    return tournaments.split(",")