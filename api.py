import requests
import json

from constants import MATCH_KEYS

def fetch(url: str):
    world_cup_results_data: requests = requests.get(url=url, timeout=30)
    return world_cup_results_data.json();

def fetch_played_matches(url: str):
    world_cup_results_data = fetch(url)
    played_matches = [match for match in world_cup_results_data if match[MATCH_KEYS["group"]] is not None]
    return played_matches

