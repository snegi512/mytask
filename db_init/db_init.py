from datetime import datetime
from sqlalchemy import create_engine, select, Table, Column, Integer,  String, MetaData, ForeignKey, true, DateTime
from sqlalchemy_utils import database_exists, create_database


from os.path import abspath, split
import sys
dir = split(split(abspath(__file__))[0])[0]
sys.path.append(dir)
from settings import get_db
DB=get_db()

meta = MetaData()

collected_data = Table('collected_data', meta,
     Column('id', Integer, primary_key=True),
     Column('title', String),
     Column('method_name', String),
     Column('params', String),
)

users = Table('users', meta,
     Column('id', Integer, primary_key=True),
     Column('login', String(250), unique = True, nullable = False),
     Column('password', String(250), nullable = False),
     Column('created_at ', DateTime(), default=datetime.now),
     Column('last_request', DateTime(), default=datetime.now),
)


engine = create_engine(DB, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

meta.create_all(engine)

conn = engine.connect()

ins_user_query = users.insert().values(login = 'admin', password = 'admin')
conn.execute(ins_user_query)


