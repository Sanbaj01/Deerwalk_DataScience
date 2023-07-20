import requests
from bs4 import BeautifulSoup

# HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
data = requests.get("https://www.ambitionbox.com/list-of-companies", headers=HEADERS)
soup = BeautifulSoup(data.content, 'html.parser')
companies = soup.find_all('div', class_='company-info-wrapper')
# ratings = soup.find_all('div', class_='rating-wrapper')

for company in companies:
    print(company.text)
    break



