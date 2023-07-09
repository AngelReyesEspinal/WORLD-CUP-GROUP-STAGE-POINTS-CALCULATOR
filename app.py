from api import fetch_played_matches
from constants import API_URL, GROUPS
from match_service import filter_matches_by_group, sort_teams_by_group

played_matches = fetch_played_matches(API_URL)

for group_name in GROUPS:
    current_group = filter_matches_by_group(played_matches, f"Group {group_name}")
    sorted_teams = sort_teams_by_group(current_group)
    print(sorted_teams)