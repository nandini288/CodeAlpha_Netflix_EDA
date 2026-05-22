import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#STEP 1 — Load Dataset

df = pd.read_csv(
    "C:/CodeAlpha_Netflix_EDA/dataset/netflix_titles.csv"
)

print(df.head())

#STEP 2 — Explore Dataset Structure

print(df.shape) #shows(rows, columns)

print(df.columns) #shows all column names

print(df.info()) # shows datatypes and missing values


#STEP 3 — Find Missing Values

print(df.isnull().sum()) # shows the no.of missing values in each column


#STEP 4 — Remove Duplicates

print(df.duplicated().sum()) # shows no of duplicate rows are present

df.drop_duplicates(inplace=True) # drop the duplicate row

print(df.shape)


# -------------------------------
# STEP 5: DATA ANALYSIS
# -------------------------------

print(df['type'].value_counts()) # shows Movie VS TV count

print(df['country'].value_counts().head(10)) # shows which country produces more netflix content

print(df['release_year'].value_counts().head(10))



#STEP 6 — VISUALIZATION

sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.show()
# Insight:
# Movies are more common than TV Shows on Netflix.


top_countries = df['country'].value_counts().head(10)

top_countries.plot(kind='bar')

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Shows/Movies")

plt.show()

# Insight:
# United States produces the highest amount of Netflix content.

print("EDA Project Completed Successfully")