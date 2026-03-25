import pandas as pd
import requests
import matplotlib.pyplot as plt

url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)
data=response.json()
df=pd.DataFrame(data)
df=df.drop(columns="id")
df=df.rename(columns={"userId":"user_id"})
df_group=df.groupby("user_id").count()
df["posts_length"]=df["body"].apply(len)
print(df)
print(df_group)
df_group.plot(kind="bar")
plt.title("Posts Per User")
plt.xlabel("User ID")
plt.ylabel("Number of Posts")
plt.show()
df["posts_length"].hist()

plt.title("Distribution of Post Length")
plt.xlabel("Character Count")
plt.ylabel("Frequency")

plt.show()