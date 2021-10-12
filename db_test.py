from db_strat import GetEvents
import pandas as pd
from pathlib import Path
import mplfinance as mpf

df = pd.read_csv(Path("./Resources/BTC-5YRS-D.csv"), index_col="Date", parse_dates=True, infer_datetime_format=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)
print(df.head())
print(df.tail())

df = df.dropna()
mpf.plot(df, type="candle", style="yahoo", volume=True)

events = db_strat.GetEvents(df)
new_df = events.Output()
new_df.head()