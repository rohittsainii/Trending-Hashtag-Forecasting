import pandas as pd
from prophet import Prophet
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load and prepare data
df = pd.read_csv("Step-2.csv")
df.rename(columns={"Post_Date": "ds", "Likes": "y"}, inplace=True)
df["ds"] = pd.to_datetime(df["ds"])
df = df.groupby("ds").sum().reset_index()

# Step 2: Interpolate missing values and apply smoothing
df['y'] = df['y'].interpolate(method='linear')
df['y'] = df['y'].rolling(window=7, min_periods=1).mean()

# Step 3: Split data into training and testing (last 30 days for test)
train = df[:-30]
test = df[-30:].copy()

# Step 4: Train tuned Prophet model
model = Prophet(
    daily_seasonality=True,
    weekly_seasonality=True,
    seasonality_mode='multiplicative',
    changepoint_prior_scale=0.5
)
model.fit(train)

# Step 5: Predict on test set
future = test[['ds']]
forecast = model.predict(future)

# Step 6: Merge predictions with actuals
merged = forecast[['ds', 'yhat']].merge(test[['ds', 'y']], on='ds')
merged['yhat'] = merged['yhat'].round(2)
merged['y'] = merged['y'].round(2)

# Step 7: Evaluate
mae = mean_absolute_error(merged['y'], merged['yhat'])
rmse = np.sqrt(mean_squared_error(merged['y'], merged['yhat']))
r2 = r2_score(merged['y'], merged['yhat'])

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# Step 8: Export to Power BI-ready CSV
merged.to_csv("actual_vs_predicted_fixed.csv", index=False)
print("Exported: actual_vs_predicted_fixed.csv")
