# LEVEL 2 — DATA MANIPULATION

# apply
df["Age"] = df["Age"].apply(
    lambda x: x + 1
)

def categorize_age(age):
    if age < 18:
        return "Child"
    elif age < 30:
        return "Young"
    else:
        return "Adult"

df["Age_Group"] = df["Age"].apply(
    categorize_age
)

# map
df["Gender"] = df["Gender"].map({
    "Male": 0,
    "Female": 1
})

# replace
df["Gender"] = df["Gender"].replace({
    "Male": 0,
    "Female": 1
})

# groupby
result = df.groupby("City")["Salary"].mean()
print(result)

result = df.groupby("City")[["Salary", "Age"]].mean()
print(result)

# agg
result = df["Salary"].agg([
    "mean",
    "median",
    "min",
    "max",
    "std"
])
print(result)

# groupby + agg
result = df.groupby("City").agg({
    "Salary": "mean",
    "Age": "max"
})
print(result)

result = df.groupby("City")["Salary"].agg([
    "mean",
    "min",
    "max",
    "sum"
])
print(result)

# concat
df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Age": [20, 21]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Age": [22, 23]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)
print(result)

result = pd.concat(
    [df1, df2],
    axis=1
)
print(result)

# merge
students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [80, 90, 85]
})

result = pd.merge(
    students,
    marks,
    on="ID",
    how="inner"
)
print(result)

result = pd.merge(
    students,
    marks,
    on="ID",
    how="left"
)
print(result)

result = pd.merge(
    students,
    marks,
    on="ID",
    how="right"
)
print(result)

result = pd.merge(
    students,
    marks,
    on="ID",
    how="outer"
)
print(result)

# join
df1 = pd.DataFrame({
    "Name": ["A", "B", "C"]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    "Marks": [80, 90, 85]
}, index=[1, 2, 3])

result = df1.join(df2)
print(result)

# query
result = df.query("Age > 25")
print(result)

result = df.query(
    "Age > 25 and Salary > 50000"
)
print(result)

# isin
result = df[
    df["City"].isin(
        ["Delhi", "Mumbai"]
    )
]
print(result)

# between
result = df[
    df["Age"].between(20, 30)
]
print(result)

# set_index
df = df.set_index("Name")
print(df)

# reset_index
df = df.reset_index()
print(df)
