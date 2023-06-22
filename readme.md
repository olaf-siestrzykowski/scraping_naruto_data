## Naruto Wiki Analysis: Unveiling the Shinobi Secrets
#### In this project: 
- Utilized **Python (BeautifulSoup)** library to scrape data from the fandom Naruto wiki, extracting character information.
- I cleaned the data with **pandas** library ensuring the data was structured appropriately for analysis.
- Prepared the cleaned data for export into Power BI Desktop, a powerful data visualization tool.
- Transformed the data by splitting one large table into smaller ones and establishing relationships between them using primary and foreign keys.
- Leveraged Power BI Desktop to create insightful visuals that provide answers to specific questions regarding the Naruto dataset.
<br/><br/>
Overall, this project involved web scraping, data cleaning, data modeling, and visualization to gain valuable insights into the Naruto characters' data.
### I. Web Scraping:
Code snippets soon!
### II. Data Cleaning:
Code snippets soon!
### III. Visualization - Questions and Findings:
Questions to answer:

### III.1 What are the biggest clans? 
To identify the largest clans in the Naruto universe, I analyzed the data and generated the following chart:
![Clans](screenshots/naruto_pbi_clans.png)
The Uchiha clan emerged as the largest, although it is unfortunate that many of its members have met an untimely fate. <br/><br/>
The Hyūga clan ranked second, aligning with its reputation as one of the prominent clans within Konoha in the Naruto anime.
### III.2 What is nature type ninjas distribution among all clans? 
To understand the distribution of nature types among different clans, I created the following visualization:
![Nature Types in Clans](screenshots/naruto_pbi_nature1.png)
By clicking the hamburger menu, a slicer appears, enabling you to choose specific clans and explore the corresponding nature types:
![Nature Types - slicer](screenshots/naruto_pbi_nature2.png)

### III.3 Are ninjas fit? 
I analyzed the weight distribution among ninjas and categorized them into different weight groups. 
<br/><br/>The following chart showcases the weight distribution:
![Weight](screenshots/naruto_pbi_weight1.png)
The chart includes a drill-down option, allowing a closer look at the weight range of 51-60 kg:
![Weight 51-60](screenshots/naruto_pbi_weight2.png)
Interestingly, there are no female ninjas above 60 kg, and overall, even male ninjas tend to have relatively low weight. 
<br/><br/>
This aligns with the notion that ninjas are known for their agility and speed, emphasizing the importance of being lightweight.

### III.3b BMI Ratings: Assessing Ninja Health
To further assess the health of the ninjas, I calculated their BMI ratings using the European standard. <br/>
BMI was calculated by dividing the mass (kg) by the square of height (m). <br/><br/>
The following chart displays the BMI ratings:
![BMI](screenshots/naruto_BMI_raportv2.png)
However, it is important to note that certain anomalies were observed in the BMI calculations. <br/><br/>
<br/>
For instance, Ōnoki's height is lower than 1m, resulting in an issue with the calculation method. <br/>
<br/>
Additionally, Akamaru, a character classified as a fighting dog, lacks length information, which prevents an accurate BMI assessment.
#### CONCLUSION
Based on the available data, only 4 ninjas appear to be classified as obese, although 2 of them have been eliminated due to calculation issues. This leaves 2 remaining obese ninjas.
<br/><br/>
Moreover, 14 ninjas are classified as overweight, indicating a higher percentage of weight-related concerns.
<br/><br/>
However, it is worth considering that out of the 195 ninjas with available height and weight data, only 16 fall into the overweight or obese categories, which accounts for less than 10% of the dataset.
<br/><br/>
The majority of the ninjas exhibit a healthy BMI ratio, with 104 out of 195 falling within the normal range.
<br/><br/>
Nevertheless, it is intriguing to note that 37.44% of the ninjas are classified as underweight, which may initially raise concerns. 
#### BUT!
It is important to remember that ninjas undergo rigorous training to improve their taijutsu and ninjutsu skills, making physical training a core aspect of their lives.
<br/><br/>
Moreover, considering the context of the Naruto universe within Japanese culture, it is worth noting that Japanese people are known for their consumption of raw food, which contributes to longevity and overall health, even with lower body weight.


### III.4 What are most common jutsus and tools? 
Coming soon...

### IV. Data Structure changes

Initially, the project involved working with a single large table containing uncleaned data.<br/><br/> 
To improve the data structure, I performed data cleaning and modeling, resulting in the creation of smaller tables based on one-to-one, many-to-one, or many-to-many relationships. <br/><br/>
The transformation is depicted below:
![Data Structure START](screenshots/naruto_data1.png)
![Data Structure END](screenshots/naruto_data2.png)
These changes aimed to enhance data organization and facilitate more efficient analysis and visualization.
------------------------------------------------
### TODO:
- [x] Integrate dictionary values
- [x] Integrate dictionary keys
- [x] Generate a pandas dataframe object
- [x] Perform data cleansing
- [x] Include next page links in the code
- [x] Develop visually appealing displays
- [x] Develop more visually appealing displays
- [x] Create additional columns
- [x] Generate separate tables for data containing commas
- [x] BMI ratio (III.3.1.)

### Pending Tasks:
- [ ] Develop EVEN more visually appealing displays!
- [ ] Jutsu and Tools all charts
- [ ] Paste code snippets (points I. and II.)