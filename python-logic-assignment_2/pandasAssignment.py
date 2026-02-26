import pandas as pd
df=pd.read_csv("sample.csv")
print("First five rows:   ")
print(df.head())
print("Last five rows:  ")
print(df.tail())
print("Dataset info:  ")
print(df.info())
print("Dataset description:   ")
print(df.describe())
x=df["StudentID"]
new_df=df[["StudentID","Age","Math"]]
filter_df=df[df["Age"]>19]
print("Single column selection :  \n ",x)
print("Multiple column selection datafreame:  \n",new_df)
print("Filtered rows on the basis of age>19:  \n",filter_df)