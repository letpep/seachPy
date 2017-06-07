
#!/usr/bin/python3
#coding=utf-8

import os.path
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options

from tornado.options import define, options

define("port", default=8888, help="run port", type=int)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/search", SearchHandler),
            (r"/todo/(\d+)/edit", EditHandler),
            (r"/todo/(\d+)/delete", DeleteHandler),
            (r"/todo/(\d+)/finish", FinishHandler),
        ]
        settings = dict(
            template_path = TEMPLATE_PATH,
            static_path = STATIC_PATH,
            debug = True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        # self.db = torndb.Connection(
        #     host = options.mysql_host,
        #     database = options.mysql_database,
        #     user = options.mysql_user,
        #     password = options.mysql_password
        # )


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('11')
        title = "todo"
        # db = self.application.db
        # todos = db.query("select * from todo order by post_date desc")
        # self.render("index.html", todos=todos, title=title)


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")
        # if not title:
        #     return None
        # db = self.application.db
        # db.execute("insert into todo (title, post_date) values('%s', UTC_TIMESTAMP())",
        #            title)
        # self.redirect("/")


class EditHandler(tornado.web.RequestHandler):
    def get(self, id):
        pass

    def post(self, id):
        pass


class DeleteHandler(tornado.web.RequestHandler):
    def get(self, id):
       pass


class FinishHandler(tornado.web.RequestHandler):
    def get(self, id):
        pass



def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

