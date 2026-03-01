import pandas as pd
data=pd.read_csv("sample.csv")
single_column=data["Score"]
print(" Single column is printed as follows: \n",single_column)
df=data[["Name","Passed"]]
print("First 3 rows ")
print(df.iloc[0:3])
data.index=["abc","bcd","efg","ghi","ijk"]
print(data.loc["abc"])
filter_data=data[data["Score"]>75]
print("Filtered data on the basis of score >85: \n",filter_data)
double_filter_data=data[(data["Score"]>75) & (data["Passed"]==True)]
sorted_data=double_filter_data.sort_values("Score",ascending=False)
filter_sort_data=data[(data["Score"]>75) & (data["Passed"]==True)].sort_values("Score",ascending=False)
print("High performance students: \n",filter_sort_data)
