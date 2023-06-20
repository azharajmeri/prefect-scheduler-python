"""
Prefect SQLAlchemy Connector
----------------------------

This module provides code to create a Prefect block that integrates with SQLAlchemy,
allowing you to execute tasks and workflows using SQLAlchemy as the
data access layer. It includes functionalities for connecting to databases,
executing queries, and performing database operations.
"""

import os

from dotenv import load_dotenv
from prefect_sqlalchemy import SqlAlchemyConnector, ConnectionComponents, SyncDriver

load_dotenv()


def create_sqlalchemy_connector_block():
    connector = SqlAlchemyConnector(
        connection_info=ConnectionComponents(
            driver=SyncDriver.MYSQL_MYSQLCONNECTOR,
            username=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=int(os.getenv("DATABASE_PORT")),
            database=os.getenv("DATABASE_NAME"),
        )
    )

    connector.save('sqlalchemy-connector-block')
