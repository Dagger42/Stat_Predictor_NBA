# NBA Stat Predictor

**NBA Stat Predictor** is a machine learning-powered web app that predicts next-season statistics for active NBA players. The prediction model is trained on comprehensive historical data and presented through an interactive Streamlit interface.

---

## Overview

This application predicts season-level performance metrics for over **400 active NBA players**, including:

- Points  
- Assists  
- Rebounds  
- Games Played  
- Minutes  

The underlying model is trained on data from more than **5,000 past and present NBA players**, leveraging season-by-season statistics retrieved using the [NBA API](https://github.com/swar/nba_api).

### Model Performance

The model achieves the following **mean absolute error (MAE)** values on the test set:

| Metric     | MAE  |
|------------|------|
| Points     | 2.5  |
| Assists    | 0.6  |
| Rebounds   | 1.0  |

---

## Features

- Predicts player statistics for the upcoming NBA season
- Interactive player selection through a Streamlit sidebar
- Displays both predicted and historical stats for comparison
- Built with a multi-output XGBoost regression model
- Simple and intuitive user interface

---

## Live Demo

[Click here to view the app](https://nbastatpredictor.streamlit.app/) 

You can also run the app by cloning the repository and accessing the frontend directory and running
'''bash
git clone https://github.com/Dagger42/Stat_Predictor_NBA.git
# Install the required dependencies
pip install -r requirements.txt

#Run the app locally
streamlit run frontend/app.py
'''

---
