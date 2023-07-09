class Team: 
    def  __init__(self, name, points_earned, goals_scored, goals_conceded, goals_difference, total_wins, total_losses, total_drawn):
        self.name: str = name
        self.points_earned: int = points_earned
        self.goals_scored: int = goals_scored
        self.goals_conceded: int = goals_conceded
        self.goals_difference: int = goals_difference
        self.total_wins: int = total_wins
        self.total_losses: int = total_losses
        self.total_drawn: int = total_drawn
