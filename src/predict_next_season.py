import pandas as pd
import joblib

# Load the model
model = joblib.load('../model/xgb_model_next_season.pkl')

#Load the active players data
df_active = pd.read_csv('../data/processed_data/active_players_pg_stats.csv')

features = ['PTS', 'AST', 'REB', 'GP', 'MIN', 'PLAYER_AGE', 'SEASON_NUM']
targets = ['PTS', 'AST', 'REB', 'GP', 'MIN']

# Get the latest season for each player
latest_season = df_active.groupby('PLAYER_ID')['SEASON_NUM'].max().reset_index()

df_latest = df_active.merge(latest_season, on=['PLAYER_ID', 'SEASON_NUM'])

X_active_latest = df_latest[features]

predictions = model.predict(X_active_latest)

predicted_stats = pd.DataFrame(predictions, columns=[f'PRED_{target}' for target in targets]).round(2)

results_df = pd.concat([df_latest[['PLAYER_ID', 'PLAYER_NAME', 'SEASON_NUM', 'PLAYER_AGE']], predicted_stats], axis=1)
results_df['SEASON_NUM'] += 1  # Increment the season number for the predictions
results_df['SEASON_ID'] = '2025-2026'
results_df['PRED_GP'] = results_df['PRED_GP'].round(0)
results_df['PLAYER_AGE'] = results_df['PLAYER_AGE'] + 1  # Increment the age for the predictions


results_df.to_csv('../data/predicted_stats/active_players_next_season_predictions.csv', index=False)