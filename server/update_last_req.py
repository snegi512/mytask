from datetime import datetime
from sqlalchemy import update
import os
import sys
dir = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(dir)
import db

def update_table(login:str):
    db_data = db.get_db_data()
    conn = db_data['conn']
    users = db_data['users']
    print(login)
    update_query = update(users).where(users.c.login == login).values(last_request = datetime.now())
    conn.execute(update_query)
