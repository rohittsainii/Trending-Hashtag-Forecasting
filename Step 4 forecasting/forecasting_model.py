# forecasting_model.py

import pandas as pd
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load the dataset
df = pd.read_csv("Step-2.csv")
df.rename(columns={"Post_Date": "ds", "Likes": "y"}, inplace=True)
df["ds"] = pd.to_datetime(df["ds"])

# Step 2: Group by date and smooth using 7-day rolling average
df = df.groupby("ds").sum().reset_index()
df["y_smooth"] = df["y"].rolling(window=7).mean()

# Step 3: Split into train and test sets
train = df[:-30].copy()
test = df[-30:].copy()

# Step 4: Train Prophet model on smoothed data
prophet_train = train[["ds", "y_smooth"]].dropna().rename(columns={"y_smooth": "y"})
model = Prophet(daily_seasonality=True, weekly_seasonality=True, yearly_seasonality=True)
model.fit(prophet_train)

# Step 5: Forecast for test dates
future = test[["ds"]]
forecast = model.predict(future)

# Step 6: Compare predicted vs actual
result = forecast[["ds", "yhat"]].merge(test[["ds", "y"]], on="ds")

# Step 7: Save outputs as CSV
forecast.to_csv("forecast_smooth.csv", index=False)
result.to_csv("actual_vs_predicted_smooth.csv", index=False)

# Step 8: Evaluate performance
mae = mean_absolute_error(result["y"], result["yhat"])
rmse = np.sqrt(mean_squared_error(result["y"], result["yhat"]))
r2 = r2_score(result["y"], result["yhat"])

print("\n📊 Model Evaluation")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")
print("\nCSVs saved: forecast_smooth.csv & actual_vs_predicted_smooth.csv")


