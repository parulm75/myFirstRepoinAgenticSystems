# 🔹 Sample Data (5–10 Rows)

import pandas as pd
import numpy as np

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
miss_value=df.isnull()
print(miss_value)
df=df.fillna(df["Salary"].mean())
print(df)
df=df.drop(columns=["Temporary_Notes"])
df=df.rename(columns={"Salary":"Annual_salary"})
summary_df=df.groupby("Department").agg({"Annual_salary":"mean","Employee":"count"})
print(summary_df)