import pandas as pd

# Read the CSV file (created during the web scraping part)
df = pd.read_csv("csv's/character_data3.csv")

# Remove unwanted characters and whitespace
df = df.apply(lambda x: x.str.replace(r"\[|\]|'", ""))
df = df.apply(lambda x: x.str.replace(r'\\n', ', ', regex=True))
df = df.apply(lambda x: x.str.replace(r'"', '', regex=True))
df = df.applymap(lambda x: ' '.join(x.split()) if isinstance(x, str) else x)

# Set unknown values for 'Sex' column
df.loc[~df['Sex'].isin(['Male', 'Female']), 'Sex'] = 'Unknown'

# Extract numeric values for 'Height', 'Weight', and 'Age'
# Note: Age, Height, and Weight values were collected from different series (Naruto|Naruto Shippuden|Boruto).
# We have considered the most recent occurrence for each character.

df['Height'] = df['Height'].str.extract(r'(\d+(?:\.\d+)?) cm$')
df['Weight'] = df['Weight'].str.extract(r'(\d+(?:\.\d+)?) kg$')
df['Age'] = df['Age'].str.extract(r'(\d+)$')

# Removing specific and unwanted prefixes
df['Family'] = df['Family'].str.replace(r'^Family, \\t, ', '', regex=True)
df['Nature Type'] = df['Nature Type'].str.replace('Nature Type, , ', '', regex=True)
df['Jutsu'] = df['Jutsu'].str.replace('Jutsu, , , ', '', regex=True)
df['Jutsu'] = df['Jutsu'].str.replace(', , , ', ', ', regex=True)
df['Tools'] = df['Tools'].str.replace('Tools, , , ', '', regex=True)
df['Tools'] = df['Tools'].str.replace(', , , ', ', ', regex=True)
df['Unique Traits'] = df['Unique Traits'].str.replace(r'^Unique Traits, \\t, ', '', regex=True)

# Export to CSV file
df.to_csv("csv's/character_data4.csv", index=False, encoding='utf-8-sig')

#print(df.columns)

#print(df['Unique Traits'].value_counts())
