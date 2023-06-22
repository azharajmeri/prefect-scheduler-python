from prefect import flow

from scheduler.tasks import fetch_stock_news_task


@flow(name="Get Stock News")
def fetch_stock_news_flow(ticker="MSFT"):
    fetch_stock_news_task(ticker=ticker)
