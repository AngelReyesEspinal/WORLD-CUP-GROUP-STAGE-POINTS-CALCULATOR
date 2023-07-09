from typing import List
from models.team import Team

class Group:
    def  __init__(self):
        self.teams: List[Team]  = []

    def add_team(self, team: Team):
        self.teams.append(team)

    def update_team(self, new_team_data: Team):
        team_to_update = next((team for team in self.teams if team["name"] == new_team_data["name"]), None)
        team_to_update["points_earned"] += new_team_data["points_earned"]
        team_to_update["goals_scored"] += new_team_data["goals_scored"]
        team_to_update["goals_conceded"] += new_team_data["goals_conceded"]
        team_to_update["goals_difference"] += new_team_data["goals_difference"]
        team_to_update["total_wins"] += new_team_data["total_wins"]
        team_to_update["total_losses"] += new_team_data["total_losses"]
        team_to_update["total_drawn"] += new_team_data["total_drawn"]
