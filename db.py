from settings import get_db
from sqlalchemy import create_engine, Table, MetaData

def get_db_data():
    engine = create_engine(get_db(), echo=False)
    meta = MetaData(engine)
    collected_data = Table('collected_data', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    conn = engine.connect()
    return {
    "engine" : engine,
    "meta" : meta,
    "collected_data" : collected_data,
    "users" : users,
    "conn" : conn,
    }

