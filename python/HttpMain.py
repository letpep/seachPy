#!/usr/bin/python2
# coding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpclient
from compy.Demohandler import Demohandler
from coreseek.Searchhandler import Searchhandler


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://www.baidu.com")
        self.write(response.body)

    def post(self):
        key = self.get_argument("key")
        key = key + "1"
        self.write(key)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/demo", Demohandler),
        (r"/search", Searchhandler),
    ],
        debug=True

    )


def main():
    app = make_app()
    app.listen(8887)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
