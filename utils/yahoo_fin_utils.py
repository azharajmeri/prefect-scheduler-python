import datetime

from yahoo_fin.news import get_yf_rss


def get_ticker_news(ticker_name):
    # get news
    return get_yf_rss(ticker_name)


def get_ticker_news_dict(ticker_name):
    ticker_news = get_ticker_news(ticker_name)
    return [{
        'guidislink': int(data['guidislink']),
        'link': data['link'],
        'published': datetime.datetime(*data['published_parsed'][:6]),
        'stock_id': ticker_name,
        'summary': data['summary'],
        'title': data['title'],
        'summary_details': data['summary_detail']['value']
    } for data in ticker_news]
