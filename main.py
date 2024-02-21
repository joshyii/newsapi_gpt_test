from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='cf918114f212486baa96b6346b621e19')

all_articles = newsapi.get_top_headlines(
                                    category='business',
                                    )


print(count)
print(len(all_articles['articles']))