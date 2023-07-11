import pandas as pd
from models.team import Team

def printTable (group_name: str, sorted_teams: list[Team]):
    team_names = [team["name"] for team in sorted_teams]
    team_total_games_played = [team["total_wins"] + team["total_losses"] + team["total_drawn"] for team in sorted_teams]
    team_total_wins = [team["total_wins"] for team in sorted_teams]
    team_total_drawn = [team["total_drawn"] for team in sorted_teams]
    team_total_losses = [team["total_losses"] for team in sorted_teams]
    team_goals_difference = [f"+{team['goals_difference']}" if team["goals_difference"] > 0 else team["goals_difference"] for team in sorted_teams]
    team_points_earned = [team["points_earned"] for team in sorted_teams]

    df = pd.DataFrame(
        {
            "Country": team_names,
            "Played": team_total_games_played,
            "W": team_total_wins,
            "D": team_total_drawn,
            "L": team_total_losses,
            "GD": team_goals_difference,
            "Pts": team_points_earned,
        }
    )

    print(f"----------------- GROUP {group_name} -----------------")
    print(df)
    print("-------------------------------------------")
    print("")