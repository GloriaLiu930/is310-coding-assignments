import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://harrypotter.fandom.com/wiki/List_of_deaths"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', class_='wikitable')

table_data = []
for table in tables:
    headers = [header.text.strip() for header in table.find_all('th')]
    rows = table.find_all('tr')

    for row in rows:
        cells = row.find_all(['td', 'th'])
        row_data = [cell.text.strip() for cell in cells]
        table_data.append(row_data)

df = pd.DataFrame(table_data)
df.to_csv('harry_potter_deaths.csv', index=False)

