import asyncio
import tornado.web
from login_handler import LoginHandler
from data_handler import DataHandler
class MainHandler2(tornado.web.RequestHandler):
    def get(self):
        tornado.ioloop.IOLoop.instance().stop()
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/api/login", LoginHandler),
        (r"/api/data", DataHandler),
    ], cookie_secret="__TODO:12345")

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())