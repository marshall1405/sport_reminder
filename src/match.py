class Match:
    def __init__(self, id=0, start_index=0, end_index=0):
        self.id = id
        self.start_index = start_index
        self.end_index = end_index
        self.team1 = None
        self.team2 = None
        self.league = None
        self.time = None

    def set_teams(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def set_league(self, league):
        self.league = league
    
    def set_time(self, time):
        self.time = time

    def print(self):
        print("Match ", self.id, ", Start:", self.start_index, ", End: ", self.end_index)