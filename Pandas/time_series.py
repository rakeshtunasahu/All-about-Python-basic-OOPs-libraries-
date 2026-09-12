# LEVEL 5 — TIME SERIES

# to_datetime
df["Date"] = pd.to_datetime(
    df["Date"]
)

# dt.year
df["Year"] = df["Date"].dt.year

# dt.month
df["Month"] = df["Date"].dt.month

# dt.day
df["Day"] = df["Date"].dt.day

# dt.hour
df["Hour"] = df["Date"].dt.hour

# diff
df["Difference"] = (
    df["Sales"].diff()
)

# shift
df["Previous_Sales"] = (
    df["Sales"].shift(1)
)

# pct_change
df["Growth"] = (
    df["Sales"].pct_change()
)

# rolling
df["Rolling_Average"] = (
    df["Sales"]
    .rolling(7)
    .mean()
)

# resample
df["Date"] = pd.to_datetime(
    df["Date"]
)

df = df.set_index("Date")

monthly_sales = (
    df["Sales"]
    .resample("ME")
    .mean()
)

print(monthly_sales)