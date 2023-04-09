import env
import os
import env
from newsapi import NewsApiClient
from datetime import datetime, timedelta

now = datetime.now()
today = now.strftime("%Y-%m-%d")
yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")

newsapi = NewsApiClient(api_key=os.environ.get('API_KEY'))


def carousel_news(sources , domains):
    all_articles = newsapi.get_everything(
        q="general", sources=sources, domains=domains ,from_param=yesterday, to=today, language="en", sort_by="publishedAt", page=1)
    
    slide_articles = []

    for i in range(0,3):
        slide_articles.append(all_articles['articles'][i])

    return slide_articles

def daily_news():
    pass

# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2023-03-30',
#                                       to='2023-03-12',
#                                       language='en',
#                                       sort_by='',
#                                       page=2)
