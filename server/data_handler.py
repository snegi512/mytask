import tornado.web
from sqlalchemy.sql import select
import update_last_req
import os
import sys
dir = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(dir)
import db


class DataHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("login"):
            self.write('401 Unauthorized')
            return
            
        login = str(self.get_secure_cookie("login"))[2:-1]
        update_last_req.update_table(login)

        db_data = db.get_db_data()
        conn = db_data['conn']
        collected_data = db_data['collected_data']
        s = select(collected_data)
        res = conn.execute(s)
        
        out = {'data':[row._mapping for row in res]}
        self.write(str(out))
        
# 401 Unauthorized