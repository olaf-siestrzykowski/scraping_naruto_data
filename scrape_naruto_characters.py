import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

base_url = "https://naruto.fandom.com"
url = base_url + "/wiki/Category:Characters"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

character_links = soup.find_all("a", class_="category-page__member-link")

character_data = []

for link in character_links:
    character_name = link.text.strip()
    character_url = urljoin(base_url, link["href"])

    character_response = requests.get(character_url)
    character_soup = BeautifulSoup(character_response.content, "html.parser")
    infobox_table = character_soup.find("table", class_="infobox")

    table_data = {'Name': [character_name]}

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

    character_data.append({"Name": character_name, **table_data})


df = pd.DataFrame(character_data)
df.to_csv("character_data2.csv", index=False, encoding='utf-8-sig')
