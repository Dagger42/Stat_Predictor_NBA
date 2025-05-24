import pandas as pd
import streamlit as st

df_pred = pd.read_csv('../data/predicted_stats/active_players_next_season_predictions.csv')
df_past = pd.read_csv('../data/processed_data/active_players_pg_stats.csv')

player_names = df_pred['PLAYER_NAME'].unique()
selected_player = st.sidebar.selectbox("Choose a player", player_names)


player_data_pred = df_pred[df_pred['PLAYER_NAME'] == selected_player]
player_data_past = df_past[df_past['PLAYER_NAME'] == selected_player]
stats_df_past = player_data_past[['SEASON_NUM', 'PLAYER_AGE', 'PTS', 'AST', 'REB', 'GP', 'MIN', 'SEASON_ID']]
stats_df_past.columns = ['Season #', 'Player Age', 'PPG', 'APG', 'RPG', 'Games Played', 'Minutes per game', 'Season']
stats_df_past = stats_df_past.round(1)
stats_df_past = stats_df_past.astype(str).replace(r'\.0$', '', regex=True)

stats_df_pred = player_data_pred[['SEASON_NUM', 'PLAYER_AGE', 'PRED_PTS', 'PRED_AST', 'PRED_REB', 'PRED_GP', 'PRED_MIN', 'SEASON_ID']]
stats_df_pred.columns = ['Season #', 'Player Age', 'Pred PPG', 'Pred APG', 'Pred RPG', 'Pred Games Played', 'Pred Minutes', 'Season']
stats_df_pred = stats_df_pred.round(1)
stats_df_pred = stats_df_pred.astype(str).replace(r'\.0$', '', regex=True)

st.title(f"{selected_player} - Past Stats")
st.dataframe(stats_df_past, use_container_width=True)

st.title(f"{selected_player} - Predicted Stats for Next Season")
st.dataframe(stats_df_pred, use_container_width=True)

