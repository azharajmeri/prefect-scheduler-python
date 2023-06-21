from blocks.sqlalchemy_block import create_sqlalchemy_connector_block
from scheduler.deployments import create_deployment

if __name__ == "__main__":
    create_sqlalchemy_connector_block()
    create_deployment()
