"""
Task 1: Exploratory Data Analysis and Visualization
Dataset: World Bank Population Data
Objective: To understand data structure and visualize population distribution
"""


import pandas as pd
import matplotlib.pyplot as plt


df_1 = pd.read_csv(r"world population\population.csv",skiprows = 4)
df_1 = df_1.loc[:,~df_1.columns.str.contains('^Unnamed')]
print("population review\n",df_1.head(),"\n")
print("shape of population table\n",df_1.shape,"\n")
print("columns in population table\n",df_1.columns,"\n")
print(df_1.isnull().sum(),"\n")
df_1.info()
print("\n")
print(df_1.describe())
print("\n")

df_2 = pd.read_csv(r"world population\country metadata.csv")
df_2 = df_2.loc[:,~df_2.columns.str.contains('^Unnamed')]
print("Country Metadata preview\n",df_2.head(),"\n")
print("country metadata shape\n",df_2.shape,"\n")
print("country metadata columns\n",df_2.columns,"\n")
print(df_2.isnull().sum(),"\n")
df_2.info()
print("\n")



df_3 = pd.read_csv(r"world population\indicator metadata.csv")
df_3 = df_3.loc[:,~df_3.columns.str.contains('^Unnamed')]
print("Indicator Metadata Preview\n",df_3.head(),"\n")
print("indicator metadata shape\n",df_3.shape,"\n")
print("indicator metadata columns\n",df_3.columns,"\n")
print(df_3.isnull().sum(),"\n")
df_3.info()
print("\n")

year_column = df_1.columns[4:]
world_data = df_1[df_1['Country Name']=='World']
world_data[year_column].T.plot(figsize=(10,5))
plt.title("World Population Growth (1960-2023)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()

real_countries = df_2[df_2['Region'].notna()]['Country Code']

year = '2023'
country_only = df_1[df_1['Country Code'].isin(real_countries)]


top_10 = (country_only[['Country Name',year]].dropna().sort_values(by = year, ascending = False).head(10))
plt.figure(figsize=(8,5))
plt.bar(top_10['Country Name'],top_10[year])
plt.xticks(rotation=45)
plt.title("Top 10 most populated countries (2023)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.show()

print(f"The most populated country in {year} is "
      f"{top_10.iloc[0]['Country Name']} with population "
      f"{int(top_10.iloc[0][year]):,}")

