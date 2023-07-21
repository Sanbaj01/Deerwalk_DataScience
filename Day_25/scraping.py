import requests
from bs4 import BeautifulSoup
import pandas as pd

company_name = []
company_rating = []
company_review_count = []
company_type = []

for page in range(1,11):
    # HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    data = requests.get("https://www.ambitionbox.com/list-of-companies", headers=HEADERS)
    soup = BeautifulSoup(data.content, 'html.parser')
    companies = soup.find_all('div', class_='company-info-wrapper')
    # ratings = soup.find_all('div', class_='rating-wrapper')
    for company in companies:
        company_name.append(company.find('h2', class_='company-name').text.strip())
        company_rating.append(company.find('p', class_='rating').text.strip())
        company_review_count.append(company.find('a', class_='review-count').text.strip().split('k')[0].replace('(',''))
        company_type.append(company.find('p', class_='infoEntity').text.strip())
            
company_info = {
    'name' : company_name,
    'ratings' : company_rating,
    'review_count' : company_review_count,
    'type' : company_type
}

df = pd.DataFrame(company_info)
print(df)

# with open('company.txt', 'w') as f:
#     f.write(str(company_info))



