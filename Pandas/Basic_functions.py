# Read CSV
df = pd.read_csv("data.csv")

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Neha"],
    "Age": [20, 25, 22, 30],
    "Salary": [30000, 50000, 40000, 70000],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune"]
})

# Head
print(df.head())
print(df.head(2))

# Tail
print(df.tail())
print(df.tail(2))

# Shape
print(df.shape)

# Columns
print(df.columns)

# Data Types
print(df.dtypes)

# Info
df.info()

# Describe
print(df.describe())

# Select One Column
print(df["Age"])

# Select Multiple Columns
print(df[["Name", "Age", "Salary"]])

# loc
print(df.loc[0])
print(df.loc[0:2])
print(df.loc[0:2, ["Name", "Age"]])

# iloc
print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[0:3, 0:2])

# isna
print(df.isna())

# isnull
print(df.isnull())

# notna
print(df.notna())

# Check Missing Values
print(df.isnull().sum())

# dropna
df = df.dropna()
df = df.dropna(axis=0)
df = df.dropna(axis=1)

# fillna
df["Age"] = df["Age"].fillna(25)
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])

# duplicated
print(df.duplicated())
print(df.duplicated().sum())

# drop_duplicates
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["Name"])

# drop
df = df.drop(columns=["City"])
df = df.drop(index=[0, 1])

# rename
df = df.rename(columns={
    "Age": "Years",
    "Salary": "Income"
})

# astype
df["Years"] = df["Years"].astype(float)
df["Years"] = df["Years"].astype(int)
df["Name"] = df["Name"].astype(str)

# to_numeric
df["Income"] = pd.to_numeric(
    df["Income"],
    errors="coerce"
)

# to_datetime
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

# unique
print(df["City"].unique())

# nunique
print(df["City"].nunique())

# value_counts
print(df["City"].value_counts())
print(df["City"].value_counts(normalize=True))

# sort_values
df = df.sort_values("Age")
df = df.sort_values("Age", ascending=False)
df = df.sort_values(
    ["City", "Salary"],
    ascending=[True, False]
)