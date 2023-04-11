import env
import os
import env
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from user.options import news_categories, news_filter
from .models import NewsArticle

now = datetime.now()
today = now.strftime("%Y-%m-%d")
yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")

newsapi = NewsApiClient(api_key=os.environ.get('API_KEY'))


try:


    def carousel_news(sources, domains ):
        all_articles = newsapi.get_everything(
            q="general", sources=sources, domains=domains, from_param=yesterday, to=today, language="en", sort_by="publishedAt", page=1)

        slide_articles = []

        for i in range(0, 3):
            slide_articles.append(all_articles['articles'][i])

        return slide_articles


    def daily_news(categories, sources, domains , email):

        content = {}

        for category in categories:
            content[category] = {}
            for filter in news_filter:
                content[category][filter] = newsapi.get_everything(
                    q=category, sources=sources, domains=domains, from_param=yesterday, to=today, language="en", sort_by=filter, page=1)

        for classification, value in content.items():
            for sort, results in value.items():
                for l in results['articles']:

                    try:

                        like = NewsArticle.objects.get(
                            title=l['title'])
                        l['likes'] = like.likesCount()
                        l['liked'] = like.userLiked(email)
                        l['saved'] = like.userSaved(email)

                    except:
                        l['likes'] = 0
                        l['liked'] = ''
                        l['saved'] = ''

        return content

except :
    print("API KEY EXHAUSTED")

'''

{
    "general" : {
        "general" : [data] ,
        "buisness" : [data] ,
        "technology" : [data] ,
        "sports" : [data] ,
        "entertainment" : [data] ,
        "health" : [data] ,
        "science" : [data] ,
    }
}

'''

# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2023-03-30',
#                                       to='2023-03-12',
#                                       language='en',
#                                       sort_by='',
#                                       page=2)
