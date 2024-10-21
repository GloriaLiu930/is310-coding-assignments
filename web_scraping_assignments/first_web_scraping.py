import requests
from bs4 import BeautifulSoup

url = "https://www.gutenberg.org/browse/scores/top"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

top_100_section = soup.find(id="books-last1")

book_list = top_100_section.find_next('ol')

book_items = book_list.find_all('li')

for item in book_items:
    title = item.get_text().strip()
    print(title)

