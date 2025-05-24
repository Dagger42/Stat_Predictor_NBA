NBA Stat Predictor
This project predicts next-season statistics for active NBA players using a machine learning model trained on historical player data. The predictions are presented through an interactive Streamlit web application.

Overview
The NBA Stat Predictor is a data-driven tool that forecasts performance metrics such as points, assists, rebounds, games played, and minutes for over 400 active NBA players. The model is trained on data from more than 5,000 current and former NBA players, using season-by-season statistics obtained from the official NBA API.

The model achieves the following mean absolute error (MAE) values on the test set:

MAE for Points: 2.5

MAE for Assists: 0.6

MAE for Rebounds: 1.0

Users can explore individual player predictions and compare them with historical data through an intuitive web interface.

Features
Predicts player statistics for the upcoming season, including points, assists, rebounds, games played, and minutes
Provides an interactive sidebar to search and select specific players
Displays both predicted and past season statistics in a clean, scrollable format
Utilizes an XGBoost-based multi-output regression model for accurate predictions
