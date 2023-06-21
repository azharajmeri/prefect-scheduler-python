from utils.constants import TABLE_QUERY, INSERT_QUERY


def create_table(connector):
    connector.execute(TABLE_QUERY)


def insert_records(connector, records):
    if not records:
        return
    connector.execute_many(
        INSERT_QUERY,
        seq_of_parameters=records,
    )
