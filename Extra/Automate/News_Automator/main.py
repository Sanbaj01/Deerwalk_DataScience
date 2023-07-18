import requests


API_KEY = '749c95324cbc41909aab0938fe6aa3b5'
URL = ('https://newsapi.org/v2/top-headlines?')

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_article(query_parameters)

def get_articles_by_query(query):