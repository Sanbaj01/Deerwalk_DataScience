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
        f.write(quote.text)
        

# for quote in quotes:
#     print(quote.text)

