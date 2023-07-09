from constants import MATCH_KEYS
from models.group import Group

filter_matches_by_group = lambda played_matches, current_group: [match for match in played_matches if match[MATCH_KEYS["group"]] == current_group]

def create_team(match, team_name, home_team, away_team):
    is_winning_team = int(match[home_team]) > int(match[away_team])
    is_losing_team = int(match[home_team]) < int(match[away_team])
    is_drawn = int(match[home_team]) == int(match[away_team])
    points_earned = 0

    if is_winning_team:
        points_earned = 3
    elif is_drawn:
        points_earned = 1
    else:
        points_earned = 0

    new_team = {
        'name': match[team_name],
        'points_earned': points_earned,
        'goals_scored': match[home_team],
        'goals_conceded': match[away_team],
        'goals_difference': match[home_team] - match[away_team],
        'total_wins': 1 if is_winning_team else 0,
        'total_losses': 1 if is_losing_team else 0,
        'total_drawn': 1 if is_drawn else 0
    }
    return new_team

def sort_teams_by_group(matches_by_group):
    group: Group = Group()
    
    for match in matches_by_group:
        home_team = create_team(match, MATCH_KEYS["homeTeam"], MATCH_KEYS["homeTeamScore"], MATCH_KEYS["awayTeamScore"])
        away_team = create_team(match, MATCH_KEYS["awayTeam"], MATCH_KEYS["awayTeamScore"], MATCH_KEYS["homeTeamScore"])

        # HOME
        if any([team for team in group.teams if team['name'] == match[MATCH_KEYS["homeTeam"]]]):
            group.update_team(home_team)
        else:
            group.add_team(home_team)

        # AWAY 
        if any([team for team in group.teams if team['name'] == match[MATCH_KEYS["awayTeam"]]]):
            group.update_team(away_team)
        else:
            group.add_team(away_team)

    sorted_arr = sorted(group.teams, key=lambda x: x["points_earned"], reverse=True)
    return sorted_arr