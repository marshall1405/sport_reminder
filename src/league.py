class League:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def __repr__(self):
        return f"League(name={self.name})"