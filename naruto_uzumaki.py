import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://naruto.fandom.com/wiki/Naruto_Uzumaki"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

infobox_table = soup.find("table", class_="infobox")
name = soup.h1.text.strip()

table_data = {'Name': [name]}

headers = [header.get_text(strip=True) for header in infobox_table.find_all('th')
           if 'mainheader' not in header.get('class', [])]
headers[0] = 'Name'

rows = infobox_table.find_all("tr")

for row in rows[1:]:
    header = row.find("th")
    if header:
        key = header.text.strip()
        value_element = row.find("td")

        if value_element:
            for span in value_element.find_all("span", class_="smwttcontent"):
                span.extract()

            value = value_element.text.strip()
            if key not in table_data:
                table_data[key] = []
            table_data[key].append(value)

df = pd.DataFrame(table_data)

print(df)
