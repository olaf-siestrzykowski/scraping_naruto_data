import pandas as pd

df = pd.read_csv("csv's/character_data3.csv")

df = df.apply(lambda x: x.str.replace(r"\[|\]|'", ""))
df = df.apply(lambda x: x.str.replace(r'\\n', ', ', regex=True))
df = df.apply(lambda x: x.str.replace(r'"', '', regex=True))
df = df.applymap(lambda x: ' '.join(x.split()) if isinstance(x, str) else x)

df.loc[~df['Sex'].isin(['Male', 'Female']), 'Sex'] = 'Unknown'

# I want the height, weight and age of the last occurrence to be considered
df['Height'] = df['Height'].str.extract(r'(\d+(?:\.\d+)?) cm$')
df['Weight'] = df['Weight'].str.extract(r'(\d+(?:\.\d+)?) kg$')
df['Age'] = df['Age'].str.extract(r'(\d+)$')

df['Family'] = df['Family'].str.replace(r'^Family, \\t, ', '', regex=True)
df['Nature Type'] = df['Nature Type'].str.replace('Nature Type, , ', '', regex=True)
df['Jutsu'] = df['Jutsu'].str.replace('Jutsu, , , ', '', regex=True)
df['Jutsu'] = df['Jutsu'].str.replace(', , , ', ', ', regex=True)
df['Tools'] = df['Tools'].str.replace('Tools, , , ', '', regex=True)
df['Tools'] = df['Tools'].str.replace(', , , ', ', ', regex=True)
df['Unique Traits'] = df['Unique Traits'].str.replace(r'^Unique Traits, \\t, ', '', regex=True)

# Ninja Rank - take last (in Power BI?)
print(df.columns)

print(df['Unique Traits'].value_counts())

df.to_csv("csv's/character_data4.csv", index=False, encoding='utf-8-sig')

# Questions to answer:

# 1. What nature type is most common? --> "Nature Type in Clans" page

# 2. What is nature type ninjas distribution among all clans? --> "Nature Type in Clans" page

# 3. Can ninjas be fat? --> "Weight (drill)" page

# 4. What are most common jutsus and tools? --> "?" page
