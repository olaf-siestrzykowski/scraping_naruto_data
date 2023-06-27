import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

base_url = "https://naruto.fandom.com"
url = base_url + "/wiki/Category:Characters"


# Function to scrape character data from a given URL
def scrape_character_data(url):
    response = requests.get(url)

    # Send a request to the URL and create a BeautifulSoup object
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    character_links = soup.find_all("a", class_="category-page__member-link")
    character_data = []

    for link in character_links:
        character_name = link.text.strip()
        character_url = urljoin(base_url, link["href"])

        # Send a request to the character URL and create a BeautifulSoup object
        character_response = requests.get(character_url)
        character_soup = BeautifulSoup(character_response.content, "html.parser")
        infobox_table = character_soup.find("table", class_="infobox")

        if infobox_table:
            # Extract data from the table
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

    return character_data


# Initialize a list to store all character data
all_character_data = []

# Scrape character data from multiple pages until there are no more next pages
while url:
    character_data = scrape_character_data(url)
    all_character_data.extend(character_data)

    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    next_link = soup.find("a", class_="category-page__pagination-next")
    if next_link:
        url = urljoin(base_url, next_link["href"])
    else:
        url = None

# Create a DataFrame from the scraped character data
df = pd.DataFrame(all_character_data)

# Save the DataFrame to a CSV file
df.to_csv("csv's/character_data3.csv", index=False, encoding='utf-8-sig')
