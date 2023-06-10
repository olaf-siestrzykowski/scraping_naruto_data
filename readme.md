## Naruto Anime - Web Scraping, Data Cleaning and Visualization
In this project: 
- I used **Python (BeautifulSoup)** to webscrape fandom Naruto wiki and get characters data.
- I cleaned the data with **pandas** library and prepared it for export to **Power BI Desktop**
- I reformed one big table to smaller ones and connected them using primary and foreign keys.
- Lastly, I generated visuals to answer the questions.

## Questions to answer:

### 1. What are the biggest clans? 
![Clans](screenshots/naruto_pbi_clans.png)
Biggest clan is the Uchiha, but sadly most of them are dead...
Hyūga clan is 2nd biggest and it is true that it is one of the biggest Konoha's clan in Naruto anime.
### 2. What is nature type ninjas distribution among all clans? 
![Nature Types in Clans](screenshots/naruto_pbi_nature1.png)
When you click hamburger menu, slicer with clan chooser shows up.
![Nature Types - slicer](screenshots/naruto_pbi_nature2.png)

### 3. Are ninjas fit? 
I categorized ninjas into weight groups.
![Weight](screenshots/naruto_pbi_weight1.png)
This chart has drill down option (51-60 kg below).
![Weight 51-60](screenshots/naruto_pbi_weight2.png)
There are no female ninjas above 60 kg's but overall even males seem to have low weight.
Ninjas are known to be light and fast. (I think I might create a BMI rating for this)
### 4. What are most common jutsus and tools? 
Coming soon...

## *Data Structure changes
I started with one big table containing a lot of unleaned data.
![Data Structure START](screenshots/naruto_data1.png)
I performed data cleaning and modeling with creation of new smaller tables basing on <u>one to one</u> or <u>many to many</u> relations.
![Data Structure END](screenshots/naruto_data2.png)

------------------------------------------------
### TODO:
- [x] Integrate dictionary values
- [x] Integrate dictionary keys
- [x] Generate a pandas dataframe object
- [x] Perform data cleansing
- [x] Include next page links in the code
- [x] Develop visually appealing displays

### Pending Tasks:
- [ ] Create additional columns
- [ ] Generate separate tables for data containing commas
- [ ] Develop more visually appealing displays
