import argparse
import os
import pandas as pd
import time
from tqdm import tqdm
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# Create directory for raw data if it doesn't exist
os.makedirs('../data/raw_data', exist_ok=True)

parser = argparse.ArgumentParser(description="NBA Player Stats Scraper")
parser.add_argument('--fresh', action='store_true', help='Rescrape all data from scratch')
args = parser.parse_args()

# Load previously saved data if resuming fetch
try:
    existing_df = pd.read_csv('../data/raw_data/partial_all_players.csv')
    processed_ids = set(existing_df['PLAYER_ID'].unique())
    print(f"Resuming from {len(processed_ids)} already processed players.")
except FileNotFoundError:
    existing_df = pd.DataFrame()
    processed_ids = set()
    print("No checkpoint found. Starting fresh.")

try:
    active_df = pd.read_csv('../data/raw_data/partial_active_players.csv')
    active_ids = set(active_df['PLAYER_ID'].unique())
    print(f"Resuming from {len(active_ids)} already processed active players.")
except FileNotFoundError:
    active_df = pd.DataFrame()
    active_ids = set()
    print("No checkpoint found for active players. Starting fresh.")

player_list_all = players.get_players()
all_players_data = []
active_players_data = []


for player in tqdm(player_list_all, desc="Fetching player stats"):
    player_id = player['id']

    if player['is_active'] and player_id in active_ids:
        continue

    if player_id in processed_ids and not player['is_active']:
        continue  

    try:
        stats = playercareerstats.PlayerCareerStats(player_id=player_id)
        df = stats.get_data_frames()[0]
        season_avgs = df[[
            'SEASON_ID', 'TEAM_ID', 'PLAYER_AGE', 'GP', 'GS',
            'MIN', 'PTS', 'AST', 'REB', 'FG_PCT', 'FG3_PCT', 'FT_PCT'
        ]].copy()
        season_avgs['PLAYER_NAME'] = player['full_name']
        season_avgs['PLAYER_ID'] = player_id
        season_avgs['IS_ACTIVE'] = player['is_active']

        if player_id not in processed_ids:
            all_players_data.append(season_avgs)
        if player['is_active']:
            active_players_data.append(season_avgs)

        # Save every 20 players to avoid data loss
        if len(all_players_data) % 20 == 0:
            pd.concat(all_players_data + [existing_df], ignore_index=True).to_csv('../data/raw_data/partial_all_players.csv', index=False)
            pd.concat(active_players_data + [active_df], ignore_index=True).to_csv('../data/raw_data/partial_active_players.csv', index=False)
        
        time.sleep(0.5)  # Lowered to speed up if API allows
    
    except KeyboardInterrupt:
        print("Manual interrupt received.")
        break
    except Exception as e:
        print(f"Error processing player {player_id}: {e}")
        continue

# === Final Save ===
all_df = pd.concat(all_players_data + [existing_df], ignore_index=True)
active_df = pd.concat(active_players_data + [active_df], ignore_index=True)

all_df.to_csv('../data/raw_data/all_players_career_stats.csv', index=False)
active_df.to_csv('../data/raw_data/active_players_career_stats.csv', index=False)

print(f"\n✅ Done. Processed {len(all_df['PLAYER_ID'].unique())} total players.")
