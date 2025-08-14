import pandas as pd
from prophet import Prophet

# Load & clean
df = pd.read_csv("Step-2.csv")
df.rename(columns={"Post_Date": "ds", "Likes": "y"}, inplace=True)
df["ds"] = pd.to_datetime(df["ds"])
df = df.groupby("ds").sum().reset_index()

# Check: enough recent dates?
print("Last date in dataset:", df["ds"].max())

# Fit Prophet
model = Prophet()
model.fit(df)

# Forecast future
future = model.make_future_dataframe(periods=900)  # ~2.5 years
forecast = model.predict(future)

# Save forecast
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("forecast_mentions_2027.csv", index=False)
