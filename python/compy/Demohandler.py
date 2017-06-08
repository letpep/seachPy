#!/usr/bin/python3
# coding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpclient


class DemoHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://www.baidu.com")
        self.write(response.body)

    def post(self):
        key = self.get_argument("key")
        self.set_status(300, reason=None)
        key = key + "2"
        self.write(key)
