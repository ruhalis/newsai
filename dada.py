import requests
from bs4 import BeautifulSoup

# URL of Yahoo Finance news section
url = "https://finance.yahoo.com/news/"

# Fetch the webpage
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract news headlines and links
news_items = soup.find_all('h3', class_='Mb(5px)')

# Print the news
for item in news_items:
    headline = item.text
    link = item.find('a')['href']
    print(f"Headline: {headline}")
    print(f"Link: https://finance.yahoo.com{link}\n")
