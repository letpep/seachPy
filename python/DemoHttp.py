#!/usr/bin/python3
#coding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpclient
class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("htt://www.baidu.com")
        self.write(response.body)
    def post(self):
        key = self.get_argument("key")
        self.set_status(300,reason=None)
        self.write(key)
def make_app():
    return tornado.web.Application([
        (r"/",MainHandler)
        ,
    ]

    )
def main():
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()

if __name__=="__main__":
    main()
