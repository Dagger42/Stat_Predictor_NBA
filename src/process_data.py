import pandas as pd

targets = ['PTS', 'AST', 'REB', 'GP', 'MIN']

# Need to load data and convert to per game statistics

df_active = pd.read_csv('../data/raw_data/active_players_career_stats.csv')

#make per game statistics dataframe for active players

df_pg_active = df_active.copy()

df_pg_active.drop(['FG_PCT','FG3_PCT','FT_PCT', 'GS'], axis = 1, inplace=True)

df_pg_active = df_pg_active.groupby(['PLAYER_ID', 'SEASON_ID'], as_index=False).agg({
    'PTS': 'sum',
    'AST': 'sum',
    'REB': 'sum',
    'GP': 'last',
    'MIN': 'sum',
    'TEAM_ID': 'last',
    'IS_ACTIVE': 'last',
    'PLAYER_NAME': 'last',
    'PLAYER_AGE': 'last',
})

df_pg_active['GP'] = df_pg_active['GP'].replace(0, pd.NA)

df_pg_active['PTS'] = df_pg_active['PTS'] / df_pg_active['GP']
df_pg_active['PTS'] = df_pg_active['PTS'].round(2)
df_pg_active['AST'] = df_pg_active['AST'] / df_pg_active['GP']  
df_pg_active['AST'] = df_pg_active['AST'].round(2)
df_pg_active['REB'] = df_pg_active['REB'] / df_pg_active['GP']
df_pg_active['REB'] = df_pg_active['REB'].round(2)
df_pg_active['MIN'] = df_pg_active['MIN'] / df_pg_active['GP']
df_pg_active['MIN'] = df_pg_active['MIN'].round(2)

#create a new coloumn to track season number
df_pg_active['SEASON_NUM'] = df_pg_active.groupby('PLAYER_ID').cumcount() + 1

# create new coloumns to track the stats of the next season, set to Nan values if its their final season
for stat in targets:
    df_pg_active[f'{stat}_NEXT'] = df_pg_active.groupby('PLAYER_ID')[stat].shift(-1)

df_pg_active = df_pg_active.sort_values(by=['PLAYER_ID', 'SEASON_NUM'])

df_pg_active.to_csv('../data/processed_data/active_players_pg_stats.csv', index=False)


# do the same for all the players
df_all = pd.read_csv('../data/raw_data/all_players_career_stats.csv')

df_pg_all = df_all.copy()

df_pg_all.drop(['FG_PCT','FG3_PCT','FT_PCT', 'GS'], axis=1, inplace=True)

df_pg_all = df_pg_all.groupby(['PLAYER_ID', 'SEASON_ID'], as_index=False).agg({
    'PTS': 'sum',
    'AST': 'sum',
    'REB': 'sum',
    'MIN': 'sum',
    'GP' : 'last',
    'TEAM_ID': 'last',
    'IS_ACTIVE': 'last',
    'PLAYER_NAME': 'last',
    'PLAYER_AGE': 'last',
})


df_pg_all['GP'] = df_pg_all['GP'].replace(0, pd.NA)
df_pg_all['PTS'] = df_pg_all['PTS'] / df_pg_all['GP']
df_pg_all['PTS'] = df_pg_all['PTS'].round(2)
df_pg_all['AST'] = df_pg_all['AST'] / df_pg_all['GP']
df_pg_all['AST'] = df_pg_all['AST'].round(2)
df_pg_all['REB'] = df_pg_all['REB'] / df_pg_all['GP']
df_pg_all['REB'] = df_pg_all['REB'].round(2)
df_pg_all['MIN'] = df_pg_all['MIN'] / df_pg_all['GP']
df_pg_all['MIN'] = df_pg_all['MIN'].round(2)

df_pg_all['SEASON_NUM'] = df_pg_all.groupby('PLAYER_ID').cumcount() + 1

for stat in targets:
    df_pg_all[f'{stat}_NEXT'] = df_pg_all.groupby('PLAYER_ID')[stat].shift(-1)


df_pg_all = df_pg_all.sort_values(by=['PLAYER_ID', 'SEASON_NUM'])

df_pg_all.to_csv('../data/processed_data/all_players_pg_stats.csv', index=False)