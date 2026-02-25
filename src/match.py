class Match:
    def __init__(self, player1, player2, time, league):
        self.player1 = player1
        self.player2 = player2
        self.time = time
        self.league = league

    def __repr__(self):
        return f"{self.player1} vs {self.player2} ({self.time})"