import pandas as pd
import plotly.express as plt


# Step 1: Data set loaded
 
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Observation: Dataset loaded successfully with 150 rows and 5 columns
print("Dataset loaded successfully.\n")
# Step 2: Inspect the dataset
print(" Frist five rows")
print(df.head())

print("Lat five rows")
print(df.tail())
print(df.shape)
print(df.columns.tolist())

# Check column summary and any missing value
print("Table summary")
print(df.info())
print("checking for any null values")
print(df.isnull().sum())
#petalLength described
fig_hist = plt.histogram(
    df,
    x="petal_length",
    color="species",
    nbins=30,
    title="Distribution of Petal Length by Species",
    labels={"petal_length": "Petal Length (cm)"},
    barmode="overlay",
    opacity=0.7
)
fig_hist.show()

#Identifying possible outlier
fig_box = plt.box(
    df,
    x="species",
    y="petal_length",
    color="species",
    title="Box Plot of Petal Length by Species (Outlier Detection)",
)
fig_box.show()
# Relationship betwen different variables
fig_scat=plt.scatter(
    df,
    x="petal_length",
    y="petal_width",
    title="Relationship between petal length and petal width across different species",
    color="species"
)
fig_scat.show()

# Insights about different species
df_mean=df.groupby("species").agg(
    {
        "petal_length":"mean",
        "petal_width":"mean",
        "sepal_length":"mean",
        "sepal_width":"mean"
    }
).reset_index()
fig_bar=plt.bar(
    df_mean,
    x="species",
    y=["petal_length", "petal_width", "sepal_length", "sepal_width"],  # list of columns
    barmode="group",
    title="Mean Feature Values by Species"
)
fig_bar.show()
