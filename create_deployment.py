from blocks.sqlalchemy_block import create_sqlalchemy_connector_block
from scheduler.deployments import create_deployment
from scheduler.tasks import fetch_stock_news_task

if __name__ == "__main__":
    create_sqlalchemy_connector_block()
    create_deployment()
    # fetch_stock_news_task("MSFT")