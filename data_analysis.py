# LEVEL 4 — DATA ANALYSIS

# mean
print(df["Salary"].mean())

# median
print(df["Salary"].median())

# mode
print(df["City"].mode())

# sum
print(df["Salary"].sum())

# min
print(df["Salary"].min())

# max
print(df["Salary"].max())

# std
print(df["Salary"].std())

# var
print(df["Salary"].var())

# quantile
print(df["Salary"].quantile(0.25))
print(df["Salary"].quantile(0.50))
print(df["Salary"].quantile(0.75))

# corr
print(
    df.corr(
        numeric_only=True
    )
)

# cov
print(
    df.cov(
        numeric_only=True
    )
)

# sample
print(df.sample())
print(df.sample(5))

print(
    df.sample(
        frac=0.2,
        random_state=42
    )
)

# rank
df["Rank"] = df["Marks"].rank()

df["Rank"] = df["Marks"].rank(
    ascending=False
)