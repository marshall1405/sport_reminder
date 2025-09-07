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

    
def parse_matches(matches, text):
    for m in matches:
        relevant_text = text[m.start_index: m.end_index]

def parse_leagues(leagues, text):
    for l in leagues:
        relevant_text = text[l.start_index:l.end_index]
        parse_name(l, relevant_text)
        parse_single(l, relevant_text)


# MATCH
def parse_teams(match, relevant_text):
    return

def parse_league(match, relevant_text):
    return

def parse_time(match, relevant_text):
    return


# LEAGUE
def parse_name(league, relevant_text):
    league.set_name((re.search(r'<a title="([^"]+)"', relevant_text)).group(1))

def parse_single(league, relevant_text):
    single = re.search(r'>([^<]+)<', relevant_text)
    league.set_single("DVOUHRY" in single.group(1))

def find_match_indices(text):
    return [m.start() for m in re.finditer(r'<a href="https://www.livesport.cz/zapas', text)]

def find_league_indices(text):
    return [m.start() for m in re.finditer("headerLeague__category-text", text)]

