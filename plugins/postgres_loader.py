from sqlalchemy import create_engine


def load(data, table_name):
    user = 'airflow'
    passwd = 'airflow'
    hostname = 'localhost'
    database = 'data_warehouse'

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5436/{database}'

    engine = create_engine(conn_string)
    conn = engine.connect()

    data.to_sql(table_name, con=conn, if_exists='append',
                index=False)

    print("Successfully loaded to Postgres")