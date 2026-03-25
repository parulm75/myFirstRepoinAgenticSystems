import streamlit as st
import pandas as pd
import requests

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

st.title("Streamlit Dashboard")
st.subheader("Dashboard preview")
st.dataframe(df.head())
st.write("Posts per user")
st.bar_chart(df_group)
st.write("Post length Distribution")
st.bar_chart(df["posts_length"])
