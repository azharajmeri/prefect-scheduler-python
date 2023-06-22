from prefect.deployments import Deployment

from scheduler.flows import fetch_stock_news_flow


def create_deployment():
    deployment = Deployment.build_from_flow(
        flow=fetch_stock_news_flow,
        name="fetch-stock-news",
        version=1,
        work_queue_name="default",
        work_pool_name="default-agent-pool",
    )

    deployment.apply()
