import datetime
import yfinance as yf
import mplfinance as mpf
import pandas as pd

start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2023, 12, 31)

data = yf.download("RELIANCE.NS", start=start, end=end)

# 🔥 Fix 1: Reset columns (VERY IMPORTANT)
data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]

# 🔥 Fix 2: Keep only required columns
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

# 🔥 Fix 3: Convert to float
data = data.astype(float)

# 🔥 Fix 4: Drop NaN
data = data.dropna()

print(data.head())  # debug

mpf.plot(data, type='candle', volume=True)
import datetime
import yfinance as yf
import mplfinance as mpf
import pandas as pd

start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2023, 12, 31)

data = yf.download("RELIANCE.NS", start=start, end=end)

# Fix columns
data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data = data.astype(float)
data = data.dropna()

# 🔥 Moving Averages
data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# 🔥 RSI
delta = data['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
rs = gain / loss
data['RSI'] = 100 - (100 / (1 + rs))

# 🔥 MACD
exp1 = data['Close'].ewm(span=12, adjust=False).mean()
exp2 = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = exp1 - exp2
data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

# 📊 Plot
apds = [
    mpf.make_addplot(data['MA20'], color='blue'),
    mpf.make_addplot(data['MA50'], color='red'),
    mpf.make_addplot(data['RSI'], panel=1, color='purple', ylabel='RSI'),
    mpf.make_addplot(data['MACD'], panel=2, color='green', ylabel='MACD'),
    mpf.make_addplot(data['Signal'], panel=2, color='orange')
]

mpf.plot(
    data,
    type='candle',
    volume=True,
    addplot=apds,
    panel_ratios=(3,1,1),
    title='Reliance Analysis'
)
mpf.plot(
    data,
    type='candle',
    style='yahoo',   # 🔥 better visuals
    volume=True,
    title='Reliance Candlestick Chart',
    ylabel='Price',
    ylabel_lower='Volume'
)