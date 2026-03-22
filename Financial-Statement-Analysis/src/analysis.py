import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../tcs_financials.csv")

# Calculate ratios
df['Revenue Growth (%)'] = df['Revenue'].pct_change() * 100
df['Profit Margin (%)'] = (df['Net_Profit'] / df['Revenue']) * 100
df['Debt to Equity'] = df['Total_Debt'] / df['Equity']
df['ROA (%)'] = (df['Net_Profit'] / df['Total_Assets']) * 100
df['ROE (%)'] = (df['Net_Profit'] / df['Equity']) * 100
df['Asset Turnover'] = df['Revenue'] / df['Total_Assets']

# Print data
print("\n📊 Financial Analysis:\n")
print(df)

# 📈 Revenue vs Profit
plt.figure()
plt.plot(df['Year'], df['Revenue'], marker='o', label='Revenue')
plt.plot(df['Year'], df['Net_Profit'], marker='o', label='Net Profit')
plt.title("TCS: Revenue vs Net Profit")
plt.xlabel("Year")
plt.ylabel("INR Crores")
plt.legend()
plt.savefig("output/revenue_profit.png")

# 📉 Debt to Equity
plt.figure()
plt.plot(df['Year'], df['Debt to Equity'], marker='o')
plt.title("TCS: Debt to Equity")
plt.xlabel("Year")
plt.ylabel("Ratio")
plt.savefig("output/de_ratio.png")

# 📈 ROE
plt.figure()
plt.plot(df['Year'], df['ROE (%)'], marker='o')
plt.title("TCS: ROE")
plt.xlabel("Year")
plt.ylabel("%")
plt.savefig("output/roe.png")

# 🧠 Insights
print("\n🧠 Analyst Insights:\n")

if df['Revenue Growth (%)'].iloc[-1] > 10:
    print("✔ Strong revenue growth indicates business expansion")

if df['Profit Margin (%)'].mean() > 15:
    print("✔ Consistently high profitability")

if df['ROE (%)'].iloc[-1] > 15:
    print("✔ Strong return on equity")

if df['Debt to Equity'].iloc[-1] < 0.5:
    print("✔ Low leverage, financially stable")

if df['Asset Turnover'].iloc[-1] > 1:
    print("✔ Efficient asset utilization")

print("\n📁 Charts saved in output folder ✅")