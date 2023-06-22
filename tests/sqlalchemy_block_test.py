from prefect_sqlalchemy import SqlAlchemyConnector

sqlalchemy_block = 'sqlalchemy-connector-block'

with SqlAlchemyConnector.load(sqlalchemy_block) as connector:
    while True:
        # Repeated fetch* calls using the same operation will
        # skip re-executing and instead return the next set of results
        tables = connector.fetch_many("SHOW TABLES", size=6)
        if len(tables) == 0:
            break
        print(f"LIST OF TABLES: {tables}")
