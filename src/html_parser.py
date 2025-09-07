import re

from match import Match


def create_matches(text):
    if text.startswith("Something Went Wrong"):
        return [Match()]
    else:
        output = []
        indices = find_match_indices(text)
        for m in range(len(indices)):
            if m < len(indices)-1:
                output.append(Match(m+1, indices[m], indices[m+1]-1))
            else:
                output.append(Match(m+1, indices[m], indices[m]+5000))
        return output


def find_match_indices(text):
    return [m.start() for m in re.finditer(r'<a href="https://www.livesport.cz/zapas', text)]

