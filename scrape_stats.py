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

        # New: Look for the specific table with strength data
        stats_table = character_soup.find("table", class_="wikitable center")

        if stats_table:
            headers = [header.get_text(strip=True) for header in stats_table.find_all('th')]
            headers = headers[:10]
            rows = stats_table.find_all("tr")
            for row in rows[1:]:  # Skip the first row (header row)
                columns = row.find_all(["th", "td"])  # Modified to include both th and td tags
                table_data = {headers[i]: columns[i].text.strip() for i in range(len(headers))}
                character_data.append({"Name": character_name, **table_data})
            print(character_data)
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
df.to_csv("csv's/character_stats.csv", index=False, encoding='utf-8-sig')
