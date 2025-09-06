import re


def parse_whole_page(text):
    if text.startswith("Something Went Wrong"):
        return [0]
    else:
        return find_match_indices(text)
    

def find_match_indices(text):
    return [m.start() for m in re.finditer(r'<a href="https', text)]
