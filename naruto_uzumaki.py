import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
url = "https://naruto.fandom.com/wiki/Naruto_Uzumaki"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the infobox table
infobox_table = soup.find("table", class_="infobox")
name = soup.h1.text.strip()
# Create a dictionary to store the table data
table_data = {'Name': name}

# Extract data from the table
rows = infobox_table.find_all("tr")
for row in rows:
    header = row.find("th")
    if header:
        key = header.text.strip()
        value_element = row.find("td")

        # Check if the value element exists
        if value_element:
            for span in value_element.find_all("span", class_="smwttcontent"):
                span.extract()

            value = value_element.text.strip()
            table_data[key] = value

# Create a pandas DataFrame from the table_data dictionary
df = pd.DataFrame.from_dict(table_data, orient="index", columns=["Value"])

# Print the DataFrame
print(df.loc['Family'][0])
print(df)
