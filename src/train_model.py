from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
import numpy as np
import pandas as pd
import joblib

#features we want to train off of
features = ['PTS', 'AST', 'REB', 'GP', 'MIN', 'PLAYER_AGE', 'SEASON_NUM']

#targets we want to predict
targets = ['PTS', 'AST', 'REB', 'GP', 'MIN']

#Load all players data
df_all = pd.read_csv('../data/processed_data/all_players_pg_stats.csv')


#proceed by training multioutput regression model 

target_columns = []
for target in targets:
    target_columns.append(target + '_NEXT')


df_all = df_all.dropna(subset=target_columns)

X = df_all[features]
y = df_all[target_columns]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=69)

model = MultiOutputRegressor(XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=7, random_state=69))

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


for i, col in enumerate(y_test.columns):
    mae = mean_absolute_error(y_test[col], y_pred[:, i])
    print(f'Mean Absolute Error for {col}: {mae:.2f}')

joblib.dump(model, '../model/xgb_model_next_season.pkl')