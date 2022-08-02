import tornado.web
from sqlalchemy.sql import select, and_
import update_last_req
import os
import sys
dir = os.path.split(os.path.split(__file__)[0])[0]
sys.path.append(dir)
import db

def check_login(login:str, password:str):
    db_data = db.get_db_data()
    conn = db_data['conn']
    users = db_data['users']
    s = select(users).where(and_(users.c.login == login,users.c.password == password))
    res = conn.execute(s)
    return res.rowcount
    

# if __name__ == "__main__":
#     checkLogin("admin", 'admin2')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/api/login" method="POST">'
                   '<label>login</label><br/>'
                   '<input type="text" name="login"><br/>'
                   '<label>password</label><br/>'
                   '<input type="text" name="password"><br/>'
                   '<input type="submit" value="login">'
                   '</form></body></html>')

    def post(self):
        login = self.get_body_argument("login")
        pas =  self.get_argument("password")
        if(check_login(login, pas)):
            update_last_req.update_table(login)
            self.set_secure_cookie("login", login)
            self.set_secure_cookie("password", pas)
            self.redirect("/api/data")
        else:
            self.write("Bad login or password")

