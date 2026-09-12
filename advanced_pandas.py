# LEVEL 6 — ADVANCED PANDAS

# pivot
result = df.pivot(
    index="Name",
    columns="Subject",
    values="Marks"
)
print(result)

# pivot_table
result = pd.pivot_table(
    df,
    values="Sales",
    index="City",
    columns="Year",
    aggfunc="mean"
)
print(result)

# melt
result = pd.melt(
    df,
    id_vars=["Name"]
    var_name="Subject",
    value_name="Marks"
)
print(result)

# crosstab
result = pd.crosstab(
    df["Gender"],
    df["Result"]
)
print(result)

# stack
result = df.stack()
print(result)

# unstack
result = df.unstack()
print(result)

# explode
df = pd.DataFrame({
    "Name": ["A", "B"],
    "Skills": [
        ["Python", "Pandas"],
        ["ML", "SQL"]
    ]
})

result = df.explode("Skills")
print(result)

# MultiIndex
index = pd.MultiIndex.from_tuples([
    ("Delhi", 2025),
    ("Delhi", 2026),
    ("Mumbai", 2025),
    ("Mumbai", 2026)
])

df = pd.DataFrame(
    {
        "Sales": [100, 120, 90, 110]
    },
    index=index
)

df.index.names = [
    "City",
    "Year"
]

print(df)

# expanding
df["Cumulative_Average"] = (
    df["Sales"]
    .expanding()
    .mean()
)

print(df)

# ewm
df["EMA"] = (
    df["Sales"]
    .ewm(span=3)
    .mean()
)

print(df)


# BONUS — OUTLIER HANDLING

# clip
lower = df["Sales"].quantile(0.01)
upper = df["Sales"].quantile(0.99)

df["Sales"] = df["Sales"].clip(
    lower,
    upper
)

# IQR Method
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[
    (df["Sales"] >= lower) &
    (df["Sales"] <= upper)
]

# copy
new_df = df.copy()

# to_numpy
X = df.to_numpy()

# to_dict
data = df.to_dict()

# to_list
data = df.values.tolist()