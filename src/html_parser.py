import re

from match import Match
from league import League


def create_matches_leagues(text):
    if text.startswith("Something Went Wrong"):
        return [Match()]
    else:
        matches = []
        leagues = []
        matches_indices = find_match_indices(text)
        league_indices = find_league_indices(text)

        est_league_size = 500
        est_match_size = 15000

        for l in range(len(league_indices)):
            leagues.append(League(l, league_indices[l], league_indices[l]+est_league_size))

        for m in range(len(matches_indices)):
            if m < len(matches_indices)-1:
                matches.append(Match(m+1, matches_indices[m], matches_indices[m+1]-1))
            else:
                matches.append(Match(m+1, matches_indices[m], matches_indices[m]+est_match_size))

        return matches, leagues

    
def parse_matches(matches, leagues, text):
    for m in matches:
        relevant_text = text[m.start_index: m.end_index]
        parse_teams(m, relevant_text)
        parse_league(m, leagues)
        parse_time(m, relevant_text)

def parse_leagues(leagues, text):
    for l in leagues:
        relevant_text = text[l.start_index:l.end_index]
        parse_name(l, relevant_text)
        parse_single(l, relevant_text)


# MATCH
def parse_teams(match, relevant_text):
    team1 = re.search(r'event__participant--home[^"]*">([^<]+)<', relevant_text)
    team2 = re.search(r'event__participant--away[^"]*">([^<]+)<', relevant_text)
    if not team1 or not team2:
        match.set_teams("NO TEAM", "NO TEAM")
    else:
        match.set_teams(team1.group(1), team2.group(1))

def parse_league(match, leagues):
    match_start = match.start_index
    for l in range(len(leagues)):
        if l < len(leagues)-1:
            if match_start > leagues[l].start_index and match_start < leagues[l+1].start_index:
                match.set_league(leagues[l])
                break
        else:
            match.set_league(leagues[l])

def parse_time(match, relevant_text):
    time = re.search(r'"event__time">([^<]+)<', relevant_text)
    if time:
        match.set_time(time.group(1))
    else:
        match.set_time("No Time")


# LEAGUE
def parse_name(league, relevant_text):
    league.set_name((re.search(r'<a title="([^"]+)"', relevant_text)).group(1))

def parse_single(league, relevant_text):
    single = re.search(r'>([^<]+)<', relevant_text)
    league.set_single("DVOUHRY" in single.group(1))


#HELPERS
def find_match_indices(text):
    return [m.start() for m in re.finditer(r'<a href="https://www.livesport.cz/zapas', text)]

def find_league_indices(text):
    return [m.start() for m in re.finditer("headerLeague__category-text", text)]

