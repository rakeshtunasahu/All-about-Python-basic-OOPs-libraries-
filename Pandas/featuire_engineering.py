# LEVEL 3 — FEATURE ENGINEERING

# get_dummies
df = pd.get_dummies(
    df,
    columns=["Gender", "City"],
    drop_first=True
)

# cut
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 30, 50, 100],
    labels=[
        "Child",
        "Young",
        "Adult",
        "Senior"
    ]
)

# qcut
df["Salary_Group"] = pd.qcut(
    df["Salary"],
    q=4,
    labels=[
        "Low",
        "Medium",
        "High",
        "Very High"
    ]
)

# str.lower
df["Name"] = df["Name"].str.lower()

# str.upper
df["Name"] = df["Name"].str.upper()

# str.strip
df["Name"] = df["Name"].str.strip()

# str.replace
df["Name"] = df["Name"].str.replace(
    "old",
    "new"
)

# str.contains
result = df[
    df["Name"].str.contains(
        "rahul",
        case=False,
        na=False
    )
]
print(result)

# str.split
df["First_Name"] = (
    df["Name"]
    .str.split(" ")
    .str[0]
)

# str.extract
df["Number"] = df["Phone"].str.extract(
    r"(\d+)"
)

# assign
df = df.assign(
    Total=df["Math"] + df["Science"]
)

# insert
df.insert(
    1,
    "Total",
    df["Math"] + df["Science"]
)

