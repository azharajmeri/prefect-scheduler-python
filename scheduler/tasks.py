from prefect import task, get_run_logger
from prefect_sqlalchemy import SqlAlchemyConnector

from utils.constants import SQLALCHEMY_BLOCK_NAME
from utils.db_utils import create_table, insert_records
from utils.yahoo_fin_utils import get_ticker_news_dict


@task(name="Get Stock News")
def fetch_stock_news_task(ticker):
    logger = get_run_logger()
    try:
        ticker_data = get_ticker_news_dict(ticker)
        if not ticker_data:
            logger.info(f"No news records available for ticker: {ticker}")
            return
        with SqlAlchemyConnector.load(SQLALCHEMY_BLOCK_NAME) as connector:
            create_table(connector)
            insert_records(connector, ticker_data)

        logger.info(f"News records inserted successfully for ticker: {ticker}")
    except Exception as e:
        logger.error(e)
