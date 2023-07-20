'''
Webscraping is the process of extracting data from web.
Always ask the right, question?
    for eg: what is the price of house in kathmandu? is not a good question.
            what is the price of house in chabahil, main road, of 3 storey built on 4 aana? is a good question.
Beautiful Soup - tranform the web data(html) into simpler/easier format
                -Beautiful Soup is a library that makes it easy to scrape information from web pages. 
                It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

Assignment - Goodreads -> Romance section ----> print all quotes with authors.
'''
# import requests
# from bs4 import BeautifulSoup


# r = requests.get('https://news.ycombinator.com')

# soup = BeautifulSoup(r.content, 'html.parser')

# news = soup.find_all('span', class_="titleline")

# with open('news.txt', 'w') as f:
#     for item in news:
#         f.write(item.text + '\n')
#         f.write(item.find('a').get('href') + '\n' + '*' * 20 + '\n')
        


#*********************************************************************************************************

import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.goodreads.com/quotes/tag/love')
soup = BeautifulSoup(data.content, 'html.parser')
quotes = soup.find_all('div', class_="quoteText")

with open('quotes.txt', 'w', encoding="utf-8") as f:
    for quote in quotes:
        f.write(quote.text.split('―')[0].strip() + '  - \n')
        f.write(quote.text.split('―')[1].strip() + '\n')
        f.write('*' * 50 + '\n\n')


# for quote in quotes:
    # print(quote.text.split('―')[0].strip())
    # print(quote.text.split('―')[1].strip())
#     break


        







# import requests
# from bs4 import BeautifulSoup

# def scrape_quotes(url):
#     quotes = []
#     headers = {'User-Agent': 'Mozilla/5.0'}  # Some websites require a User-Agent header
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         quote_elements = soup.find_all('div', class_='quoteText')

#         for element in quote_elements:
#             quote_text = element.get_text().strip().split('\n')[0].strip()[1:-1]  # Remove extra characters
#             quotes.append(quote_text)

#     return quotes

# if __name__ == "__main__":
#     url = "https://www.goodreads.com/quotes/tag/love"
#     quotes = scrape_quotes(url)
#     for idx, quote in enumerate(quotes, start=1):
#         print(f"{idx}. {quote}\n")


