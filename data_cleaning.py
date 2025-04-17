import pandas as pd

# Load the data and parse the datetime column
df = pd.read_csv("NIFTY_BANK_minute_data.csv", parse_dates=['date'])

# 1. Filter data from 1st January 2020 to 31st March 2025
start_date = "2020-01-01"
end_date = "2025-03-31"
df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

# 2. Drop rows with missing or corrupted values
df.dropna(inplace=True)

# 3. Remove duplicate timestamps and sort chronologically
df.drop_duplicates(subset='date', inplace=True)
df.sort_values('date', inplace=True)

# 4. Set datetime as index for resampling
df.set_index('date', inplace=True)

# 5. Resample the data to desired timeframe, e.g., hourly using OHLCV
resampled_df = df.resample('1H').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
})

# Drop any rows with NaNs from incomplete intervals
resampled_df.dropna(inplace=True)

# View the cleaned and resampled data
print(resampled_df.head())

resampled_df.to_csv("resampled_data.csv")

