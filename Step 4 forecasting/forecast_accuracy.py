import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load CSV
df = pd.read_csv('TRENDING#.csv')

# Choose which metrics to test
metrics_to_test = ['estimated_reach', 'sentiment_score']

# How many days to forecast
test_days = 30

# Loop through each metric
for METRIC in metrics_to_test:
    print("==============================")
    print(f"Checking forecast for: {METRIC}\\n")

    agg = (
        df
        .groupby('date', as_index=False)[METRIC]
        .sum()
        .rename(columns={'date':'ds', METRIC:'y'})
    )
    agg['ds'] = pd.to_datetime(agg['ds'])

    # Sort by date
    agg = agg.sort_values('ds')

    train_df = agg.iloc[:-test_days]
    test_df  = agg.iloc[-test_days:]

    print(f"Training samples: {len(train_df)}")
    print(f"Testing samples: {len(test_df)}\\n")

    m = Prophet()
    m.fit(train_df)

    future = m.make_future_dataframe(periods=test_days)
    forecast = m.predict(future)

    # Keep only forecast rows matching test dates
    forecast_test = forecast[forecast['ds'].isin(test_df['ds'])]

    comparison = test_df.merge(
        forecast_test[['ds','yhat']],
        on='ds',
        how='left'
    )

    # Compute errors
    mae  = mean_absolute_error(comparison['y'], comparison['yhat'])
    rmse = mean_squared_error(comparison['y'], comparison['yhat'])
    rmse = rmse ** 0.5
    mape = (abs((comparison['y'] - comparison['yhat']) / comparison['y'])).mean() * 100

    print("Model Accuracy Metrics:")
    print(f"MAE:  {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAPE: {mape:.2f}%\n")

    # Print comparison preview
    print("First few rows of actual vs. forecast:")
    print(comparison.head(), "\n")









