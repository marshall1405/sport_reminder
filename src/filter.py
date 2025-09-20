def filter_players(matches, player):
    output = []
    for m in matches:
        if player.lower() in m.team1.lower() or player in m.team2.lower():
            output.append(m)
    return output


def filter_tournaments(matches, tournament):
    output = []
    for m in matches:
        if tournament.lower() in m.league.name.lower():
            output.append(m)
    return output

def filter_all(matches, player, tournament):
    return

