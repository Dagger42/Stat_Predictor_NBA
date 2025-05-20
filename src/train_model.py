from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_absolute_error
import numpy as np
import pandas as pd

df_all = pd.read_csv('../data/processed_data/all_players_pg_stats.csv')

df_all['SEASON_NUM'] = df_all.groupby('PLAYER_ID')['SEASON'].cumcount() + 1

